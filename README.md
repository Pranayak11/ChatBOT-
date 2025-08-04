#  PDF Question Answering Chatbot

This is a document-based chatbot that lets you ask questions about the contents of any uploaded PDF file. It uses natural language processing to find the most relevant answers based on the document.

---

##  What It Does

- Upload a PDF
- Breaks it into smaller readable parts (chunking)
- Converts those parts into numeric vectors (embeddings)
- Stores and searches them efficiently
- Uses a language model to answer user queries based on the content
- Streams the answer and shows source chunks

---

##  How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Start Ollama and load the model
bash
Copy
Edit
ollama pull mistral
3. Run the chatbot
bash
Copy
Edit
streamlit run app.py


 Folder Structure
bash
Copy
Edit
project/
│
├── app.py                  # Streamlit UI
├── data/                   # Uploaded PDFs
├── chroma_db/              # Vector database
├── chunks/                 # Text chunks
├── notebooks/              # Preprocessing/testing
├── requirements.txt        # Dependencies
├── README.md               # Project info

 How It Works
Read PDF – Text is extracted using PyPDF2.

Chunking – Text is split into chunks of 500 characters with 100-character overlap.

Embedding – Each chunk is embedded using HuggingFace (all-MiniLM-L6-v2).

Vector DB – Stored using Chroma for fast similarity search.

Retrieval – Top relevant chunks are fetched based on the question.

Generation – A local LLM (Mistral) forms the answer using those chunks.

 Features
Works offline

Real-time streaming answers

Context-aware responses

Clean UI with a sidebar and document stats

Shows source text used in the answer



 Tech Stack
Task	Tool
PDF Reading	PyPDF2
Chunking	LangChain Text Splitter
Embeddings	HuggingFace MiniLM
Vector DB	Chroma
LLM	Mistral (via Ollama)
Frontend	Streamlit

 Author
Built by Pranaya Khunteta
Email: pranayakhunteta@gmail.com
