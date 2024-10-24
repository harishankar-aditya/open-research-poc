import uvicorn


from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


from factory.routes import app












# Define a health check route without any path parameters
@app.get("/", status_code=status.HTTP_200_OK)
async def alive(request: Request):
    """
    Provides a health check endpoint that returns a JSON response with a status of "OK".
    This endpoint can be used to check the health and availability of the application.
    """
    return JSONResponse(content={"status": "OK and Alive!"})


# Define a health check route without any path parameters
@app.get("/api/genai/health-check/", status_code=status.HTTP_200_OK)
async def health_check(request: Request):
    """
    Provides a health check endpoint that returns a JSON response with a status of "OK".
    This endpoint can be used to check the health and availability of the application.
    """
    return JSONResponse(content={"status": "OK and Healthy!"})


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
