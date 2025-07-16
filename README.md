# 📄 Author Papers Q&A Chatbot

This project builds an **LLM-powered retrieval-augmented chatbot** that answers questions based on a scientist’s papers.

It demonstrates:
- Automated paper retrieval via [Semantic Scholar API](https://api.semanticscholar.org/)
- PDF and abstract ingestion
- Embedding creation with OpenAI embeddings
- Chroma vector database for semantic search
- Streamlit app for interactive Q&A

---

## 🎯 Features

✅ Search for an author by name  
✅ Download open-access PDFs or save abstracts  
✅ Split documents into manageable chunks  
✅ Embed chunks into a vector store  
✅ Answer questions in real-time based on retrieved content  
✅ Show sources for each answer  

---

## 🛠️ Tech Stack

- Python
- LangChain
- OpenAI Embeddings
- Chroma
- Streamlit
- PyMuPDF (for PDF parsing)

---

## 🚀 Quickstart

**1️⃣ Clone the repo**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

**2️⃣ Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

*Example `requirements.txt`:*
```
langchain
langchain-community
langchain-openai
chromadb
openai
streamlit
PyMuPDF
```

**4️⃣ Set your OpenAI API key**
```bash
export OPENAI_API_KEY="sk-..."
```

**5️⃣ Search and download papers**
```bash
python download_papers.py
```
Follow prompts to pick an author and fetch papers.

**6️⃣ Ingest papers and split into chunks**
```bash
python ingest_papers.py
```

**7️⃣ Create embeddings and store in Chroma**
```bash
python embed_chunks.py
```

**8️⃣ Launch the chatbot**
```bash
streamlit run qa_app.py
```
Open [http://localhost:8501](http://localhost:8501) to ask questions.

---

## 💡 Example Questions

- *What is the role of stratocumulus clouds in climate modeling?*
- *How does machine learning improve parameterizations?*
- *What are key uncertainties in aerosol-cloud interactions?*

---

## 📂 Project Structure

```
.
├── download_papers.py
├── ingest_papers.py
├── embed_chunks.py
├── qa_app.py
├── papers/            # Downloaded PDFs and abstracts
├── chunks/            # Chunked text files
├── chroma_db/         # Vector DB
└── README.md
```

---

## 📝 Acknowledgements

- [Semantic Scholar](https://api.semanticscholar.org/)
- [OpenAI](https://platform.openai.com/)
- [LangChain](https://python.langchain.com/)
- [Streamlit](https://streamlit.io/)

---

## 📜 License

MIT License.

