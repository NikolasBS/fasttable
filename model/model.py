from pydantic import BaseModel
from typing import List

class trading_pairs_table(BaseModel):
    symbol: List[str] | None = None
    priceChangePercent: List[float] | None = None
    lastPriceChangePercent: List[float] | None = None
    volume: List[float] | None = None
    weightedAvgPrice: List[float] | None = None