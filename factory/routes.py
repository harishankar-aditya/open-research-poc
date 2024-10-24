from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


from api import open_research


app = FastAPI()

app.include_router(
    open_research.router,
    prefix="/api/genai",
    tags=["Fetch Supplier alternatives, pros, cons and G2 ratings"],
)
