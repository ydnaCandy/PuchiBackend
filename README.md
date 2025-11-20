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

### fastAPIの起動

```bash
poetry run uvicorn main:app --reload
```

## DBセットアップ

### 期の初期テーブル作成

```bash
poetry run python init_db.py
```


## Dockerコンテナを使ったデプロイ

```bash
fastapi-app/
├── main.py
├── init_db.py
├── entrypoint.sh
├── router/
│   └── __init__.py
├── crud/
│   └── __init__.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

### requirements.txtの出力

```bash
pip freeze > requirements.txt
```


### コンテナ準備

#### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```


#### ファイルコピー

```bash
scp Dockerfile [user]@[ip_address]:/home/[user]/docker/fastapi-app
scp requirements.txt [user]@[ip_address]:/home/[user]/docker/fastapi-app
scp main.py [user]@[ip_address]:/home/[user]/docker/fastapi-app
scp init_db.py [user]@[ip_address]:/home/[user]/docker/fastapi-app


scp -r crud [user]@[ip_address]:/home/[user]/docker/fastapi-app
scp -r routers [user]@[ip_address]:/home/[user]/docker/fastapi-app
scp -r schema [user]@[ip_address]:/home/[user]/docker/fastapi-app

chmod +x entrypoint.sh
```


#### composeの作成
```bash
version: "3.9"

services:
  fastapi:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: fastapi
    ports:
      - "30080:8000"
    volumes:
      - .:/app
    restart: always
```


### コンテナの起動

```bash
docker compose up -d --build
```

#### 起動確認
- ブラウザでアクセス: http://<ホストIP>:30080/  
- Swagger UI: http://<ホストIP>:30080/docs  

```bash
docker ps
docker logs -f fastapi
```



