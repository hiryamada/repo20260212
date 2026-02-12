from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """現在時刻(UTC)を返すエンドポイント"""
    current_time = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return {"current_time": current_time}
