from pydantic import BaseModel
import uvicorn
import os
from fastapi import FastAPI, File, UploadFile
from pdfminer.high_level import extract_text
import io

app = FastAPI()

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
     # Convert the async UploadFile to a synchronous BytesIO
    contents = await file.read()
    bytes_io = io.BytesIO(contents)

    # Use pdfminer to extract text from the PDF
    text = extract_text(bytes_io)

    # Return the first 200 characters of the extracted text
    preview_text = text[:200]  # Adjust this value as needed
    return {"filename": file.filename, "text_preview": preview_text}

if __name__ == "__main__":
        uvicorn.run(app)
