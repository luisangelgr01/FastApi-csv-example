from fastapi import APIRouter, HTTPException
from schemas.csv_schema import CSVRecord
from services.csv_service import get_record_by_id

router = APIRouter()

CSV_FILE_PATH = "example.csv"

@router.get("/records/{record_id}", response_model=CSVRecord)
async def read_record(record_id: int):
    record = get_record_by_id(CSV_FILE_PATH, record_id)
    if record:
        return record
    raise HTTPException(status_code=404, detail="No existe ese usuario")