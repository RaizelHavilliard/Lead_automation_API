from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

from services.processor import process_csv, CLEAN_FILE_PATH

app = FastAPI(title="Lead Processing Automation API")

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        stats = process_csv(file_path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return stats


@app.get("/download")
def download_clean_file():
    if not CLEAN_FILE_PATH.exists():
        raise HTTPException(status_code=404, detail="No processed file available")

    return FileResponse(
        CLEAN_FILE_PATH,
        media_type="text/csv",
        filename="clean_leads.csv"
    )
