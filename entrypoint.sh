#!/bin/sh
# DB 初期化
python init_db.py

# FastAPI 起動
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
