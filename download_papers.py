import os
import requests
from pathlib import Path
from semantic_scholar_client import search_author, get_author_papers

def save_abstract(paper, index):
    title = paper.get('title', 'Untitled')
    abstract = paper.get('abstract') or 'No abstract available.'
    filename = f"{index:04d}_{sanitize_filename(title)}.txt"
    path = Path("papers") / filename
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Title: {title}\n\n")
        f.write(f"Abstract:\n{abstract}\n")
    print(f"✅ Saved abstract: {filename}")

def download_pdf(url, paper, index):
    title = paper.get('title', 'Untitled')
    filename = f"{index:04d}_{sanitize_filename(title)}.pdf"
    path = Path("papers") / filename
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"✅ Downloaded PDF: {filename}")

def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in " ._-" else "_" for c in name)[:100]

if __name__ == "__main__":
    author_name = input("Enter author name: ")
    authors = search_author(author_name, limit=3)
    print("Found authors:")
    for idx, a in enumerate(authors):
        print(f"{idx+1}. {a['name']} (ID: {a['authorId']})")

    selection = int(input("Select author number: ")) - 1
    author_id = authors[selection]['authorId']

    papers = get_author_papers(author_id, limit=100)
    print("\nProcessing papers...")

    for idx, p in enumerate(papers, start=1):
        oa = p.get('openAccessPdf')
        url = oa['url'] if oa and oa.get('url') else None

        if url and url.strip():
            try:
                download_pdf(url, p, idx)
            except Exception as e:
                print(f"⚠️ Failed to download PDF, saving abstract instead: {e}")
                save_abstract(p, idx)
        else:
            save_abstract(p, idx)

    print("\n✅ All papers processed.")

