from pharma_docs import documents
import chromadb
from groq import Groq
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Chroma setup
client = chromadb.Client()
collection = client.create_collection(name="pharma_docs")

# Store documents (run once logic)
for doc in documents:
    collection.add(
        documents=[doc["content"]],
        metadatas=[{"title": doc["title"]}],
        ids=[doc["id"]]
    )

def ask_question(question):
    # Step 1: Retrieve
    results = collection.query(
        query_texts=[question],
        n_results=2
    )

    context = "\n\n".join(results["documents"][0])

    # Step 2: Generate answer using context
    response = client_groq.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a pharma expert. Answer ONLY from provided context."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ]
    )

    return response.choices[0].message.content

# Chat loop
while True:
    q = input("\nAsk something (or 'quit'): ")
    if q.lower() == "quit":
        break

    answer = ask_question(q)
    print("\nAnswer:\n", answer)