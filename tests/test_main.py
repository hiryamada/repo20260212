from datetime import datetime

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root():
    """ルートエンドポイントが現在時刻を返すことをテスト"""
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert "current_time" in payload

    # ISO 8601形式(UTC)で返ることを確認
    parsed = datetime.fromisoformat(payload["current_time"].replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
