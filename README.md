# PDF Question Answering Chatbot

This is a simple, local chatbot that answers questions based on the content of any uploaded PDF file. It reads the document, splits it into chunks, stores the information, and uses a local LLM to generate accurate answers.

---

## What It Does

- Upload a PDF from the interface
- Splits the content into chunks (with overlap) for better context
- Converts those chunks into vector embeddings
- Stores the vectors in a local Chroma database
- Uses a local model (Mistral via Ollama) to answer your question
- Displays the streamed answer and the top source chunks

---
<img width="1922" height="760" alt="image" src="https://github.com/user-attachments/assets/8e8bc9fb-5cc4-4000-97df-c414a496bbed" />

## How to Run

```bash
pip install -r requirements.txt
ollama pull mistral
streamlit run app.py
```
---

## How It Works
PDF Reading: Done with PyPDF2

Chunking: Uses LangChain's recursive splitter (chunk size = 500, overlap = 100)
Embeddings: Via HuggingFace model all-MiniLM-L6-v2
Vector DB: Stored locally in Chroma
Retrieval: Relevant chunks selected based on user query
LLM Response: Mistral (runs locally via Ollama)
Interface: Streamlit with styled layout and sidebar info

---

## Features
Runs completely offline (after setup)
Fast and contextual answers
Shows relevant source chunks
Clean, minimal UI with branding
Uses open-source tools only

---

## Tech Stack

  | Function    | Tool                    |
| ----------- | ----------------------- |
| PDF Parsing | PyPDF2                  |
| Chunking    | LangChain Text Splitter |
| Embeddings  | HuggingFace MiniLM      |
| Vector DB   | Chroma                  |
| LLM         | Mistral via Ollama      |
| Frontend    | Streamlit               |


---

Built by Pranaya Khunteta
Email: pranayakhunteta@gmail.com
