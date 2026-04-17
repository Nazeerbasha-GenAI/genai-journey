import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Conversation history
conversation_history = []

# System prompt — pharma expert role
system_prompt = """You are a helpful pharmaceutical expert assistant 
working with the Roche pharma ops team in Bengaluru. 

You help with:
- Drug information and clinical data
- Pharma operations and SOPs
- Clinical trials and regulatory questions
- Data analysis in pharma context

If a question is NOT related to pharma, respond with:
"I am a pharma specialist and cannot help with that. 
Please ask me anything about drugs, clinical trials, or pharma ops."

Always be clear, concise and professional."""

def chat(user_input):
    """Send a message and get a response from the AI"""
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Send full history to AI
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt}
        ] + conversation_history
    )
    
    # Get AI reply
    ai_reply = response.choices[0].message.content
    
    # Add AI reply to history
    conversation_history.append({
        "role": "assistant",
        "content": ai_reply
    })
    
    return ai_reply

def summarize():
    """Ask the AI to summarize the conversation so far"""
    if len(conversation_history) == 0:
        print("No conversation to summarize yet.")
        return
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Summarize this pharma conversation in 3 bullet points."},
        ] + conversation_history
    )
    
    print("\nConversation Summary:")
    print("-" * 40)
    print(response.choices[0].message.content)
    print("-" * 40)

def show_menu():
    """Show available commands"""
    print("\nCommands:")
    print("  'quit'     — exit the chatbot")
    print("  'summary'  — summarize conversation so far")
    print("  'clear'    — start a fresh conversation")
    print("-" * 40)

def main():
    """Main chatbot loop"""
    
    # Greeting
    print("\n" + "=" * 40)
    print("   Roche Pharma Expert Chatbot")
    print("=" * 40)
    print("Hello! I am your pharma expert assistant.")
    print("I can help with drugs, clinical trials,")
    print("SOPs, and pharma operations.")
    show_menu()
    
    # Main loop
    while True:
        user_input = input("\nYou: ").strip()
        
        # Skip empty input
        if not user_input:
            continue
        
        # Handle commands
        if user_input.lower() == "quit":
            print("\nChatbot: Goodbye! Stay pharma focused! 💊")
            break
            
        elif user_input.lower() == "summary":
            summarize()
            
        elif user_input.lower() == "clear":
            conversation_history.clear()
            print("\nChatbot: Conversation cleared. Starting fresh!")
            
        else:
            # Normal pharma question
            print("\nChatbot: ", end="", flush=True)
            reply = chat(user_input)
            print(reply)
            print("-" * 40)

# Run the chatbot
if __name__ == "__main__":
    main()
