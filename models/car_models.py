from typing import Optional, List

from pydantic import BaseModel, Field


class Car(BaseModel):
    id: str = Field(description="Uniquie Id for the vehicle listing")
    title: str = Field (description="title of the vehicle listing")
    make: str = Field(description="Brand of manufacturer of the car")
    model: str = Field(description=" Model of the car")
    year: str = Field(description="Model year of the car")
    mileage: Optional[int] = Field(default=None, description="mileage of car")
    price:float = Field(description="price of the car")

class CarAnalysis(BaseModel):
    key_insights: str = Field(description="Key insights about the car deals")
    buyer_types: str = Field(description="suggested buyer types")
    summary : str = Field(description="2-3 sentence summary")
    best_average_price: str = Field(description=" Best average price to buy")

class CarDealsResponse(BaseModel):
    cars: List[Car] = Field(description="List of car details available")
    analysis: CarAnalysis = Field(description="AI generated analysis of the listings")