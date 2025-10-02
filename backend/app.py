from fastapi import FastAPI, UploadFile
import uvicorn
import shutil
import os

from utils.pdf_reader import extract_text_from_pdf
from utils.embeddings import get_embeddings

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "AI Document Chatbot Backend Running"}

@app.post("/upload")
async def upload_file(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Extract text
    extracted_text = extract_text_from_pdf(file_path)
    
    # Generate embeddings (just first 200 chars to test)
    preview_text = extracted_text[:200]
    embedding = get_embeddings(preview_text)
    
    return {
        "filename": file.filename,
        "text_preview": preview_text,
        "embedding_length": len(embedding.tolist())
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF