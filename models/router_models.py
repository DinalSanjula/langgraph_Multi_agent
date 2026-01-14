import operator
from typing import TypedDict, Annotated, List, Literal

from langchain_core.messages import AnyMessage
from pydantic import BaseModel,Field


class ExtractedEntities:
    cars: List[str]= Field(default_factory=list)
    cryptocurrencies : List[str] = Field(default_factory=list)


class RouteDecision(BaseModel):
    route : Literal["car_agent","crypto_agent","general"] = Field(
        description="The agent to route to based on the user's question ")
    reasoning : str = Field(description=" Brief explanation of why this route was chosen")
    extracted_entities : ExtractedEntities = Field(
        description="Key Entities extracted from the question")


class AgentState(TypedDict):

    messages: Annotated[List[AnyMessage], operator.add]
    question : str
    route : str
    reasoning : str
    extracted_entities : dict
    final_response : dict | str
