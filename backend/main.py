from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.ingest import ingest_file
from src.query import ask
import shutil, os

class AskRequest(BaseModel):
    query: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ingest_file")
async def ingest_file_endpoint(file: UploadFile = File(...)):
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    ingest_file(temp_path)
    os.remove(temp_path)
    return {"message": f"{file.filename} ingested successfully"}

@app.post("/ask")
def ask_endpoint(body: AskRequest):
    answer = ask(body.query)
    print(answer)
    return {"message": answer}

@app.get("/")
def home():
    return {"message": "docquery API is running"}