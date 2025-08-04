import fitz 
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = r"C:\Users\Pranaya\Desktop\AmlgoChatBot\data\Ai Training Document.pdf"
    if not os.path.exists(pdf_path):
        print("PDF not found. Check the file name and path.")
    else:
        text = extract_text_from_pdf(pdf_path)
        print(" PDF loaded successfully! First 500 characters:\n")
        print(text[:500])
