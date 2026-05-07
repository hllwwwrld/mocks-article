from typing import Any

import fastapi

from app.api.business import create, set_age, get_age

class BusinessService:
    server: fastapi.FastAPI
    user_table: dict[str, int | None]
    prepared_scenario_table: dict[str, dict[str, Any]]

    def __init__(self, server: fastapi.FastAPI, user_table: dict, prepared_scenario_table: dict):
        self.server = server
        self.user_table = user_table
        self.prepared_scenario_table = prepared_scenario_table

        server.include_router(create.router)
        server.include_router(set_age.router)
        server.include_router(get_age.router)