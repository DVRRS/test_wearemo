from pydantic import BaseModel


class Postcode(BaseModel):
    lat: float
    lon: float
