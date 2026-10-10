# Idempotent record upsert — one service with a single bounded responsibility.
# Simulate downstream idempotent upsert using an ID-keyed dictionary.
def service_upsert_records(state: dict) -> dict:
    state["persisted"] = {record["external_id"]: record for record in state["mapped"]}
    state["upsert_count"] = len(state["persisted"])
    return state
