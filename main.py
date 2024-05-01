from fastapi import FastAPI
from src.routes.routes import router as routes_router


app = FastAPI()


app.include_router(routes_router)