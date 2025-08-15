from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLiteのDBファイルパス
SQLALCHEMY_DATABASE_URL = "sqlite:///./ki.db"

# SQLiteではスレッドチェックを切る必要あり
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# セッション生成
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# モデルの基底クラス
Base = declarative_base()

# DBセッション取得用の関数（FastAPIのDependsで使う）
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
