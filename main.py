from fastapi import FastAPI
from routers import ki
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 許可するオリジン（アクセス元）を指定
origins = [
    "*", # 全てのオリジンからのアクセスを許可する設定。開発環境でのみ使用を推奨。
    # "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # 許可するオリジンのリスト
    allow_credentials=True, # クッキーなどの資格情報の送信を許可
    allow_methods=["*"], # 全てのHTTPメソッド（GET, POSTなど）を許可
    allow_headers=["*"], # 全てのHTTPヘッダーを許可
)

app.include_router(ki.router)
