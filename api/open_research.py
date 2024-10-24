import os
import logging


from fastapi import APIRouter
from pydantic import BaseModel,Enum
from fastapi import Body, HTTPException
from typing import Optional
from enum import Enum


from utils.utils import convert_to_standard_types


if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)


router = APIRouter()


class OpenResearchPayload(BaseModel):
    from dotenv import load_dotenv
    load_dotenv()

    _id: str
    query: str
    model: str = ""

    class ResearchFormat(str, Enum):
        long = "long"
        short = "short"
    research_format: ResearchFormat = ResearchFormat.long

    class ResearchType(str, Enum):
        academic = "academic"
        business = "business"
    research_type: ResearchType = ResearchType.business

    other_info: Optional[str] = None


@router.post("/open-research/")
async def benchmarks(body_param: OpenResearchPayload = Body(...)):

    logging.info(body_param)
    response = {"message": "Hello","status_code": 200} #alternatives_and_g2_score(body_param=body_param)
    if response["status_code"] == 200:
        return convert_to_standard_types(response)
    else:
        raise HTTPException(
            status_code=response["status_code"],
            detail=convert_to_standard_types(response),
        )