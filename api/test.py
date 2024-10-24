import logging
import os

from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Body, HTTPException
from typing import Optional
from dotenv import load_dotenv

from utils.utils import convert_to_standard_types

if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)


router = APIRouter()


class BenchmarkingModel(BaseModel):
    """
    Defines a Pydantic model for a benchmarking request. This model includes the following fields:

    - `po_id`: The ID of the purchase order being benchmarked.
    - `supplier`: The name of the supplier being benchmarked.
    - `description`: An optional description of the benchmarking request.
    - `other_info`: Any other optional information related to the benchmarking request.
    """
    
    load_dotenv()
    po_id: str
    supplier: str
    description: str = ""
    timeout: int | str = os.getenv("gpt_timeout", 10)
    other_info: Optional[str] = None


@router.post("/negotiation-benchmarks/")
async def benchmarks(body_param: BenchmarkingModel = Body(...)):
    """
    Defines an API endpoint for handling benchmarking requests for supplier negotiations.
    This endpoint accepts a `BenchmarkingModel` object as the request body,
    which includes the supplier name, an optional description, and other optional information.
    The endpoint calls the `alternatives_and_g2_score` function from the
    `logic_functions.supplier_benchmarking` module to process the benchmarking request.
    If the response has a status code of 200, the endpoint returns the converted response.
    Otherwise, it raises an `HTTPException` with the appropriate status code and detail.
    """
    logging.info(body_param)
    response = {"message": "Hello","status_code": 200} #alternatives_and_g2_score(body_param=body_param)
    if response["status_code"] == 200:
        return convert_to_standard_types(response)
    else:
        raise HTTPException(
            status_code=response["status_code"],
            detail=convert_to_standard_types(response),
        )