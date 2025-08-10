# PuchiBackend

## Setup env 


```bash
poetry init
poetry add fastapi uvicorn sqlalchemy pydantic aiosqlite
```

```bash
# ディレクトリ作成
mkdir crud schema routers
touch main.py init_db.py
touch crud/__init__.py schema/__init__.py routers/__init__.py
```

## 実行

```bash
# 期の初期テーブル作成
poetry run python init_db.py

```