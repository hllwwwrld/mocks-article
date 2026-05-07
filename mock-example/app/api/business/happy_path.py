from fastapi import APIRouter

router = APIRouter()

@router.post("/check/{user_id}")
async def handle_check(_: str):
    return {"success": True} # по умолчанию не проводим никаких дополнительных операций, сразу отвечаем успехом