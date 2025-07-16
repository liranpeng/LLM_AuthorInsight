import requests

SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1"

def search_author(author_name, limit=1):
    """
    Search for an author by name.
    Returns list of matching authors with their IDs.
    """
    url = f"{SEMANTIC_SCHOLAR_API}/author/search"
    params = {"query": author_name, "limit": limit}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data["data"]

def get_author_papers(author_id, limit=5):
    """
    Get papers for a given author ID.
    Returns list of papers with metadata.
    """
    fields = ",".join([
        "title",
        "abstract",
        "year",
        "venue",
        "url",
        "openAccessPdf"
    ])
    url = f"{SEMANTIC_SCHOLAR_API}/author/{author_id}/papers"
    params = {"limit": limit, "fields": fields}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data["data"]

if __name__ == "__main__":
    author_name = input("Enter author name: ")
    authors = search_author(author_name, limit=3)
    print("Found authors:")
    for idx, a in enumerate(authors):
        print(f"{idx+1}. {a['name']} (ID: {a['authorId']})")

    selection = int(input("Select author number: ")) - 1
    author_id = authors[selection]['authorId']


    papers = get_author_papers(author_id, limit=50)
    print("\nTop papers:")
    for p in papers:
        title = p.get('title', 'No title')
        year = p.get('year', 'No year')
        abstract = p.get('abstract') or 'No abstract available'
        oa = p.get('openAccessPdf')
        url = oa['url'] if oa and oa.get('url') else "No PDF available"
        print(f"- {year}: {title}\n  PDF: {url}\n  Abstract: {abstract[:200]}...\n")
