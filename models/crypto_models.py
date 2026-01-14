from typing import List, Literal

from pydantic import BaseModel, Field


class MarketFactor(BaseModel):
    factor: str = Field(description="Name or short description of the market factor influencing the coin ( e.g ETF Approvals, Regulation news)")
    impact : str = Field(description="Explanation of how this factor affects the coins price or sentiment")

class CryptoInsight(BaseModel):
    prediction : str = Field(description="Specific prediction or insights about the cin's possible price movement or market behavior")
    confident : int = Field (...,ge=0,le=100,description="Confidence level (0-100) indicating how strongly the prediction is supported")

class CryptoAnalysis(BaseModel):
    coin:str = Field(description="cryptocurrency name or symbol being analysed (e.g. 'BTC,'ETH')")
    summery:str = Field(description= "Overall short market summary describing the current market state for the coin")
    sentiment: Literal["bullish", "neutral", "bearish"] = Field(description="Overall market sentiment for the coin based on current data")
    key_factors:List[MarketFactor] = Field(description="List of major market factors that are currently influence this cryptocurrency")
    insights: List[CryptoInsight] = Field(description="List of insights and predictions for this coin with confidence scores")

class CryptoAnalysisResponse(BaseModel):
    analysis: List[CryptoAnalysis] = Field(description="List of crypto for each cryptocurrency")

class CryptoRequest(BaseModel):
    coins : List[str]

class CryptoComparison(BaseModel):
    winner: str
    summery: str
    reasons: List[str]

class CryptoCompareResponse(BaseModel):
    comparisons : CryptoComparison