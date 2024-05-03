from fastapi import APIRouter, HTTPException, Query
from src.models.itemModel import Postcode
#from src.services.getDataProcess import read_table_from_bigquery
from src.services.getDataProcess import read_root
from src.services.getPostcode import get_postcodes1
from src.database.gcp import read_csv
import os
from typing import Dict

router = APIRouter()

database_name = os.getenv('DATABASE_NAME')
table_db = os.getenv('TABLE_DB')
project_id= os.getenv('PROJECT_NAME')


@router.get("/m1")
def process_data(bucket: str = Query(...), blob: str = Query(...)):
    return read_csv(bucket, blob)


@router.post("/m2")
async def get_data(data: Dict[str, int]):
    try:
        start = data.get('start')
        end = data.get('end')
        if start is None or end is None:
            raise HTTPException(status_code=400, detail="The 'start' and 'end' parameters are required.")

        results = read_root()
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


