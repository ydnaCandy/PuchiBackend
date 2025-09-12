from fastapi import APIRouter, HTTPException

router = APIRouter()

# 秒を基準にした単位変換表
time_units = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 86400
}

@router.get("/converttime/{value}/{from_unit}/{to_unit}")
def convert_time(value: float, from_unit: str, to_unit: str):
    # 対応していない単位ならエラー
    if from_unit not in time_units or to_unit not in time_units:
        raise HTTPException(status_code=400, detail="Unsupported unit")

    # まず秒にしてから目的の単位に変換
    value_in_seconds = value * time_units[from_unit]
    result = value_in_seconds / time_units[to_unit]

    return {
        "input": f"{value} {from_unit}",
        "output": f"{result} {to_unit}"
    }
