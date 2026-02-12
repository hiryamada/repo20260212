from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Hello Worldを返すエンドポイント"""
    return {"message": "Hello World"}
