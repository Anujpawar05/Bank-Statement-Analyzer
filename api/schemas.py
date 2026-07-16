from pydantic import BaseModel
from typing import Any


class AnalyzeResponse(BaseModel):
    bank_name: str
    metadata: dict[str, Any]
    analysis: dict[str, Any]
    transactions: list[dict[str, Any]]