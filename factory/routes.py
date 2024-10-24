from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


from api import test

from api.test import router
app = FastAPI()

app.include_router(
    test.router,
    prefix="/api/genai",
    tags=["Fetch Supplier alternatives, pros, cons and G2 ratings"],
)
