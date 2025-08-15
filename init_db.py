from datetime import date
from schema.database import Base, engine, SessionLocal
from schema import models

def init_data():
    # テーブル作成
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # 既にデータがあればスキップ
        if db.query(models.Ki).count() > 0:
            print("データはすでに存在します。")
            return

        # サンプルデータ
        kis = [
            models.Ki(ki_number=1, start_date=date(2023, 4, 1), end_date=date(2024, 3, 31)),
            models.Ki(ki_number=2, start_date=date(2024, 4, 1), end_date=date(2025, 3, 31)),
            models.Ki(ki_number=3, start_date=date(2025, 4, 1), end_date=date(2026, 3, 31)),
        ]

        db.add_all(kis)
        db.commit()
        print("初期データの登録が完了しました。")
    finally:
        db.close()

if __name__ == "__main__":
    init_data()
