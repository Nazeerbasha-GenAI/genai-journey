import os
import chromadb
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# ─────────────────────────────────────
# STEP 1 — Your pharma documents
# ─────────────────────────────────────
documents = [
    {
        "id": "SOP-001",
        "title": "Drug Storage and Handling SOP",
        "content": """
        Standard Operating Procedure: Drug Storage and Handling
        Document ID: SOP-001 — Version 2.1
        Department: Pharma Operations, Roche Bengaluru

        TEMPERATURE REQUIREMENTS
        - Cold chain products must be stored between 2-8 degrees Celsius
        - Room temperature products must be stored between 15-25 degrees Celsius
        - Frozen products must be stored at -20 degrees Celsius or below
        - Temperature must be monitored and logged every 4 hours

        HANDLING REQUIREMENTS
        - All personnel must wear appropriate PPE when handling drug products
        - Products must never be exposed to direct sunlight
        - Damaged packaging must be immediately reported and quarantined
        - FIFO (First In First Out) principle must always be followed

        DOCUMENTATION
        - All storage temperature logs must be maintained for 5 years
        - Any deviation from storage conditions must be reported within 2 hours
        - Monthly audit of storage areas is mandatory
        """
    },
    {
        "id": "SOP-002",
        "title": "Adverse Event Reporting SOP",
        "content": """
        Standard Operating Procedure: Adverse Event Reporting
        Document ID: SOP-002 — Version 3.0
        Department: Pharmacovigilance, Roche Bengaluru

        DEFINITIONS
        - Adverse Event (AE): Any undesirable medical occurrence in a patient
        - Serious Adverse Event (SAE): AE resulting in death or hospitalization
        - Unexpected Adverse Event: AE not listed in current product labeling

        REPORTING TIMELINES
        - Fatal or life threatening SAEs must be reported within 7 calendar days
        - All other SAEs must be reported within 15 calendar days
        - Non-serious AEs must be reported within 30 calendar days
        - Follow-up information must be submitted within 15 days of receipt

        REPORTING PROCESS
        - All AEs must be logged in Biovia Nextlab system immediately
        - Medical reviewer must assess causality within 24 hours
        - Regulatory submission must follow ICH E2A guidelines
        """
    },
    {
        "id": "SOP-003",
        "title": "Clinical Trial Data Management SOP",
        "content": """
        Standard Operating Procedure: Clinical Trial Data Management
        Document ID: SOP-003 — Version 1.5
        Department: Clinical Operations, Roche Bengaluru

        DATA COLLECTION STANDARDS
        - All clinical data must be collected using validated electronic systems
        - Source data must be traceable, legible, and contemporaneous
        - Data entry must be completed within 24 hours of patient visit
        - All data fields must be completed or reasons for missing data documented

        DATA VALIDATION
        - Automated edit checks must be applied to all data entries
        - Manual review of flagged data must be completed within 48 hours
        - Query resolution must be documented with audit trail
        - Database lock requires sign-off from data manager and statistician

        DATA SECURITY
        - All clinical data must be encrypted at rest and in transit
        - Access to clinical data is role-based and approved by IT security
        - Data backup must occur daily with off-site storage
        - Data retention period is 15 years post study completion
        """
    },
    {
        "id": "DRUG-001",
        "title": "Metformin Product Information",
        "content": """
        Product Information: Metformin Hydrochloride
        Document ID: DRUG-001 — Category: Antidiabetic

        MECHANISM OF ACTION
        - Reduces hepatic glucose production
        - Improves insulin sensitivity in peripheral tissues
        - Does not cause hypoglycemia when used as monotherapy

        DOSAGE
        - Initial dose: 500mg twice daily with meals
        - Maintenance dose: 1500-2000mg per day in divided doses
        - Maximum dose: 2550mg per day

        CONTRAINDICATIONS
        - Renal impairment with eGFR below 30 mL/min
        - Hepatic impairment
        - History of lactic acidosis

        STORAGE
        - Store at room temperature 15-25 degrees Celsius
        - Shelf life: 36 months from manufacture date
        """
    },
    {
        "id": "DRUG-002",
        "title": "Amoxicillin Product Information",
        "content": """
        Product Information: Amoxicillin Trihydrate
        Document ID: DRUG-002 — Category: Antibiotic

        MECHANISM OF ACTION
        - Inhibits bacterial cell wall synthesis
        - Binds to penicillin binding proteins
        - Bactericidal activity is time-dependent

        INDICATIONS
        - Upper and lower respiratory tract infections
        - Urinary tract infections
        - Skin and soft tissue infections
        - Dental infections and prophylaxis

        DOSAGE
        - Adults: 250-500mg three times daily
        - Children: 25-50mg per kg per day in divided doses
        - Duration: typically 5-10 days

        STORAGE
        - Store below 25 degrees Celsius
        - Oral suspension must be refrigerated after reconstitution
        - Use reconstituted suspension within 14 days
        """
    }
]

# ─────────────────────────────────────
# STEP 2 — Set up ChromaDB
# ─────────────────────────────────────

# Create a ChromaDB client — stores data locally on your laptop
chroma_client = chromadb.Client()

# Create a collection — like a table in a database
# ChromaDB's default embedding function handles text → numbers automatically
collection = chroma_client.create_collection(name="pharma_docs")

# Add all documents to ChromaDB
collection.add(
    documents=[doc["content"] for doc in documents],
    metadatas=[{"id": doc["id"], "title": doc["title"]} for doc in documents],
    ids=[doc["id"] for doc in documents]
)

print(f"Loaded {len(documents)} pharma documents into ChromaDB")
print("Database ready!\n")

# ─────────────────────────────────────
# STEP 3 — Search function
# ─────────────────────────────────────

def search_docs(question, n_results=2):
    """Search ChromaDB for most relevant documents"""
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )
    return results["documents"][0]

# ─────────────────────────────────────
# STEP 4 — RAG answer function
# ─────────────────────────────────────

def ask(question):
    """Find relevant docs then ask AI to answer from them"""

    # Step A — find relevant documents
    relevant_docs = search_docs(question)

    # Step B — build context from retrieved docs
    context = "\n\n---\n\n".join(relevant_docs)

    # Step C — send context + question to AI
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """You are a pharma expert assistant for Roche Bengaluru.
Answer questions using ONLY the provided document context.
If the answer is not in the context, say 'This information is not in the provided documents.'
Always mention which document your answer comes from."""
            },
            {
                "role": "user",
                "content": f"""Context from pharma documents:
{context}

Question: {question}

Answer based on the documents above:"""
            }
        ]
    )

    answer = response.choices[0].message.content

    print(f"Question: {question}")
    print(f"\nAnswer: {answer}")
    print("\n" + "=" * 50 + "\n")

# ─────────────────────────────────────
# STEP 5 — Test your RAG system
# ─────────────────────────────────────

ask("What is the temperature requirement for cold chain products?")
ask("How many days do I have to report a serious adverse event?")
ask("What is the maximum daily dose of Metformin?")
ask("How long must clinical data be retained?")