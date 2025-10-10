from fastapi import FastAPI, Request, Response
import uvicorn

app = FastAPI()
@app.get("/users/{item_id}")
def get_user(item_id: int, response: Response):
    response.status_code = 200
    return {
        "name": "John Doe",
        "user_id": item_id
        }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)