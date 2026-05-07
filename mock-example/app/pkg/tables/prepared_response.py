from dataclasses import dataclass
from datetime import datetime

scenario_lifetime_minutes = 5

@dataclass
class PreparedResponseRow:
    scenario: str
    created_at: datetime
    used_at: datetime | None = None


prepared_response_table: dict[str, PreparedResponseRow] = {
    "user-id-1": PreparedResponseRow(scenario="TIMEOUT", created_at=datetime.now()),
    "user-id-2": PreparedResponseRow(scenario="WRONG_AGE", created_at=datetime.now()),
    "user-id-3": PreparedResponseRow(scenario="HTTP_500", created_at=datetime.now()),
}

def is_outdated(prepared_scenario: PreparedResponseRow) -> bool:
    if prepared_scenario.used_at:
        return True

    created_at: datetime = prepared_scenario.created_at
    if created_at.replace(minute=created_at.minute + scenario_lifetime_minutes) < datetime.now():
        return True

    return False