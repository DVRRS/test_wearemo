from fastapi import APIRouter, HTTPException, Query
from src.models.itemModel import Postcode
from src.services.getPostcode import get_postcodes1
from src.database.gcs import read_csv

router = APIRouter()

path = "db-load-challenge-test/"

@router.get("/m1")
def process_data(bucket: str = Query(...), blob: str = Query(...)):
    return read_csv(bucket, blob)

@router.post("/test")
def get_postcod(data: Postcode):
    closest_postcode = get_postcodes1(data.lat, data.lon)
    return {"For the Lat": data.lat, "and the Lon": data.lon, "the postcode is": closest_postcode}

@router.post("/m2")
def process_data(data: Postcode):
    return {"Message": "acá irá la salida del postcode"}