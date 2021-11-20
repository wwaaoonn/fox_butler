from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


import myclass

app = FastAPI()


def get_request_type(dictionary):
    """
    リクエストタイプを取得する．

    Parameters
    ----------
    dictionary: dict
        payloadをdict型にエンコードしたもの．

    Returns
    ----------
    request_type: str
        リクエストタイプ．
    """
    request_type = ""
    try:
        request_type = dictionary["type"]
    except KeyError as e:
        print("catch KeyError: ", e)
    return request_type


def get_callback_id(dictionary, request_type):
    """
    コールバックIDを取得する．

    Parameters
    ----------
    dictionary: dict
        payloadをdict型にエンコードしたもの．
    request_type: str
        リクエストタイプ．

    Returns
    ----------
    callback_id: str
        コールバックID．
    """
    if request_type == "shortcut":
        callback_id = dictionary["callback_id"]
    elif request_type == "view_submission":
        callback_id = dictionary["view"]["callback_id"]
    else:
        callback_id = ""
    return callback_id


@app.get("/")
async def say_hello():
    return {"Hello": "World"}


@app.post("/")
async def create_response(payload: myclass.Payload):
    encoded_payload = jsonable_encoder(payload)
    request_type = get_request_type(encoded_payload)
    callback_id = get_callback_id(encoded_payload, request_type)
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
