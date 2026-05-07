from datetime import datetime
from fastapi import HTTPException, APIRouter

from app.pkg.tables.user import user_table


router = APIRouter()

@router.put("/user/set_age/{user_id}")
async def handle_set_age(user_id: str, date: str):
    if user_id not in user_table:
        raise HTTPException(status_code=404, detail="User not exists")

    birth_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()

    years = today.year - birth_date.year
    # Корректировка, если день рождения еще не наступил в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1

    user_table[user_id] = years

    return {user_id: user_id, "age": user_table.get(user_id, None)}