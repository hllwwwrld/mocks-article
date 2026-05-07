from datetime import datetime

from fastapi import HTTPException, APIRouter

from app.pkg.tables.prepared_response import prepared_response_table, PreparedResponseRow, is_outdated

router = APIRouter()

class PrepareResponseBody:
    scenario: str
    request_id: str

@router.post("/support/prepare_response")
async def handle_prepare_response(body: PrepareResponseBody):
    prepared_resp = prepared_response_table.get(body.request_id)
    if not is_outdated(prepared_resp):
        raise HTTPException(status_code=404, detail=f"scenario for id {body.request_id} already created")

    prepared_response_table[body.request_id] = PreparedResponseRow(scenario=body.scenario, created_at=datetime.now())

    return {"success": True}