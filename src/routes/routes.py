from fastapi import APIRouter, HTTPException, Query
from src.models.itemModel import RequestModel
from src.services.getDataProcess import read_root
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
async def get_data(request_model: RequestModel):
    try:
        start = request_model.start
        end = request_model.end

        results = read_root(start, end)
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))