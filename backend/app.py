from fastapi import FastAPI, UploadFile
import uvicorn


app = FastAPI()


@app.get("/")
def root():
return {"message": "AI Document Chatbot Backend Running"}


@app.post("/upload")
async def upload_file(file: UploadFile):
return {"filename": file.filename, "status": "received"}


if __name__ == "__main__":
uvicorn.run(app, host="0.0.0.0", port=8000)