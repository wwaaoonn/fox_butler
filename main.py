from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


import myclass
import myfunction

app = FastAPI()


@app.get("/")
async def say_hello():
    return {"Hello": "World"}


@app.post("/")
async def create_response(payload: myclass.Payload):
    encoded_payload = jsonable_encoder(payload)
    request_type = myfunction.get_request_type(encoded_payload)
    callback_id = myfunction.get_callback_id(encoded_payload, request_type)
    print(callback_id)
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
async def create_user(user: myclass.User):
    return user
