import time
from fastapi import HTTPException, APIRouter
from datetime import datetime

from app.pkg.tables.user import user_table
from app.pkg.tables.prepared_response import prepared_response_table, PreparedResponseRow, is_outdated

router = APIRouter()

scenario_lifetime_minutes = 5
timeout_second = 5

@router.get("/user/get_age/{user_id}")
async def handle_get_age(user_id: str, request_id: str):
    if response := get_prepared_scenario(user_id=user_id):
        prepared_response_table[user_id].used_at = datetime.now()

        return response

    if user_age := user_table.get(user_id, None):
        return {"age": user_age}

    raise HTTPException(status_code=404, detail="User not found")

def get_prepared_scenario(user_id: str) -> dict | None:
    prepared_scenario = prepared_response_table.get(user_id)

    if not prepared_scenario:
        return None

    if is_outdated(prepared_scenario):
        return None

    return match_prepared_scenario(target=prepared_scenario)

def match_prepared_scenario(target: PreparedResponseRow) -> dict | None:
    match target.scenario:
        case "TIMEOUT":
            time.sleep(timeout_second)
            return {"message": "Timeout"}

        case "WRONG_AGE":
            return {"age": 500}

        case "HTTP_500":
            raise HTTPException(status_code=500, detail="Internal Server Error")

    return None