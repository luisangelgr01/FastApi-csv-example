from pydantic import BaseModel

class CSVRecord(BaseModel):
    id: int
    nombre: str
    startdate: str
    email: str
    dept: str