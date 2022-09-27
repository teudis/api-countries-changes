from pydantic import BaseModel

from typing import List

class Intinerary(BaseModel):    
    destinations: List[str]

    class Config:
        schema_extra = {
        "example": {        
        "destinations": ["cuba", "panama", "colombia", "germany", "spain"]
        
           }
        }

class IntineraryComplex(BaseModel):
    amount: float
    coin: str
    destinations: List[str]
    