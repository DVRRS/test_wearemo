from fastapi import APIRouter
from src.models.itemModel import Postcode
from src.services.getPostcode import get_postcodes1

router = APIRouter()

path = "db-load-challenge-test/"

@router.get("/m1/{path}")
def load_data(path):
    return "acá irá la carga del archivo a la bd"


@router.post("/test")
def get_postcod(data: Postcode):
    closest_postcode = get_postcodes1(data.lat, data.lon)
    return {"For the Lat": data.lat, "and the Lon": data.lon, "the postcode is": closest_postcode}

@router.post("/m2")
def process_data(data: Postcode):
    return {"Message": "acá irá la salida del postcode"}