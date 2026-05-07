from fastapi import HTTPException, APIRouter

from app.pkg.tables.user import user_table

router = APIRouter()

@router.post("/user/create/{user_id}")
async def handle_create(user_id: str):
    if user_id in user_table:
        raise HTTPException(status_code=400, detail="User already exists")

    user_table[user_id] = None

    return {"success": True}