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

Built by Pranaya Khunteta
Email: pranayakhunteta@gmail.com
