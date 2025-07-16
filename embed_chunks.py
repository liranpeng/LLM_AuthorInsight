import os
from pathlib import Path
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document


# Input directory
chunks_dir = Path("chunks")

# Read all chunk files
documents = []
for file in sorted(chunks_dir.iterdir()):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
        metadata = {"source": file.name}
        documents.append(Document(page_content=text, metadata=metadata))

print(f"✅ Loaded {len(documents)} chunks for embedding.")

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create and persist Chroma DB
db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="chroma_db"
)

db.persist()
print("✅ Chroma DB created and embeddings stored in 'chroma_db/'")

