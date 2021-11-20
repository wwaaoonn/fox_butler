from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel  # リクエストbodyを定義するために必要

import myclass

app = FastAPI()


class UserName(BaseModel):
    first_name: str
    last_name: str


class User(BaseModel):
    user_id: int
    user_name: UserName


@app.post("/")
async def create_response(payload: myclass.Payload):
    encoded_payload = jsonable_encoder(payload)
    print(type(encoded_payload))
    return JSONResponse(content=encoded_payload)


@app.get("/test")
async def get_user():
    return {
        "user_id": 0,
        "user_name": {
            "first_name": "Taro",
            "last_name": "Sato"
        }
    }


@app.post("/test")
async def create_user(user: User):
    return user
