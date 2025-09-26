from urllib import response

from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/users/{item_id}")
def get_user(item_id: int, response: Response):
    response.status_code = 200
    return {
    "name": "John Doe",
    "user_id": item_id
    }

fastapi_app = FastAPI()
fastapi_app.setup()

print(fastapi_app)
from lession_4_tests.banking.src.v1.account import Account
