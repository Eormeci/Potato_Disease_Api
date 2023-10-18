from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class availableClasses(str,Enum):
    turkish ='turkish' 
    american ='american' 
    italian = 'italian'

food_items = {
    'turkish' : ['musakka','karniyarik'],
    'american' : ['hot dog','apple pie'],
    'italian' : ['ravioli','pizza']
}

valid_cuisines = food_items.keys()

@app.get("/getitems/{cuisine}")
async def get_items(cuisine:availableClasses):
    return food_items.get(cuisine)

coupon_code = {
    1 : '%10',
    2 : '%20',
    3 : '%30'
}

@app.get("/getcoupon/{code}")
async def get_items(code:int):
    return {"discount_amount":coupon_code.get(code) }


