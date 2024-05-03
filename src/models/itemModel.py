from pydantic import BaseModel


class Postcode(BaseModel):
    lat: float
    lon: float

class DataRequest(BaseModel):
    bucket: str
    blob: str

class RequestModel(BaseModel):
    start: int
    end: int