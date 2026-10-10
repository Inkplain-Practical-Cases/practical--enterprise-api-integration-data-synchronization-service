# Validate and map external records — one service with a single bounded responsibility.
# Transform upstream records to the canonical downstream API contract.
def service_map_records(state: dict) -> dict:
    state["mapped"] = [{"external_id": x["id"], "quantity": int(x["qty"])} for x in state["records"]]
    return state
