import uvicorn
import fastapi

from app.api.business.service import BusinessService
from app.pkg.tables.prepared_response import prepared_scenario_table
from app.pkg.tables.user import user_table

if __name__ == "__main__":
    app: fastapi.FastAPI = fastapi.FastAPI()
    business_service = BusinessService(
        server=app, user_table=user_table, prepared_scenario_table=prepared_scenario_table
    )

    uvicorn.run(app, host="0.0.0.0", port=8000)