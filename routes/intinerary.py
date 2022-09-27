from typing import List
from fastapi import APIRouter, HTTPException, status
from fastapi import Body
from models.intinerary import Intinerary

from countryinfo import CountryInfo

intineraty_router = APIRouter(
    tags=["Destiny"]
)

@intineraty_router.post("/")
async def exchange_intinerary(travel : Intinerary = Body(...)):
    country_origen = travel.destinations[0]
    country_destiny = travel.destinations[-1]
    
    info_country_final = CountryInfo(country_destiny)  
    currency_end = info_country_final.currencies()
 

    currencies = []
    change_currencies = []
    try:    

        for current in travel.destinations:
            c = CountryInfo(current)  
            currency = c.currencies()         
            currencies.append(currency)
        
        for country in range(0,len(travel.destinations)-1):
            country_name = travel.destinations[country]            
            c = CountryInfo(country_name)
            currency_current = c.currencies() 
            if currency_current != currency_end:
                next_country_name = travel.destinations[country + 1]
                c = CountryInfo(next_country_name)
                next_current = c.currencies()
                change = "Change:" + str(currency_current[0]) + " to " + str(next_current[0])
                change_currencies.append(change)

        destiny = {"source":country_origen, "destiny": country_destiny, "currencies_by_countries": currencies, "changes": change_currencies}
        return destiny
    except KeyError:
        raise HTTPException(status_code=404, detail="Country not found, review the name")
