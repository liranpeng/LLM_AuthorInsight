import os
from pathlib import Path
import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Input directory
papers_dir = Path("papers")

# Output directory
chunks_dir = Path("chunks")
chunks_dir.mkdir(exist_ok=True)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        return f.read()

def process_file(file_path):
    if file_path.suffix == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_path.suffix == ".txt":
        return extract_text_from_txt(file_path)
    else:
        return None

if __name__ == "__main__":
    # Load and process each file
    all_documents = []
    for file in sorted(papers_dir.iterdir()):
        text = process_file(file)
        if text:
            all_documents.append({"source": file.name, "text": text})
            print(f"✅ Loaded {file.name} ({len(text)} chars)")
        else:
            print(f"⚠️ Skipped unsupported file: {file.name}")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    all_chunks = []
    for doc in all_documents:
        splits = splitter.split_text(doc["text"])
        for i, chunk in enumerate(splits):
            chunk_record = {
                "source": doc["source"],
                "chunk_index": i,
                "text": chunk
            }
            all_chunks.append(chunk_record)

    # Save chunks as text files
    for chunk in all_chunks:
        fname = f"{chunk['source']}_chunk_{chunk['chunk_index']:02d}.txt"
        path = chunks_dir / fname
        with open(path, "w", encoding="utf-8") as f:
            f.write(chunk["text"])

    print(f"\n✅ Created {len(all_chunks)} chunks in {chunks_dir}/")

