from pharma_docs import documents
import chromadb

# Step 1: Create client
client = chromadb.Client()

# Step 2: Create collection
collection = client.create_collection(name="pharma_docs")

# Step 3: Store documents
for doc in documents:
    collection.add(
        documents=[doc["content"]],
        metadatas=[{"title": doc["title"], "id": doc["id"]}],
        ids=[doc["id"]]
    )

print("✅ Documents stored successfully!")

# Step 4: Test search
query = "What temperature should drugs be stored at?"

results = collection.query(
    query_texts=[query],
    n_results=2
)

print("\nQuery:", query)

for i, doc in enumerate(results["documents"][0]):
    print(f"\nResult {i+1}:")
    print(doc[:300])