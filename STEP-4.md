# Step 4 of 6 — Idempotent record upsert

## Capability
# Simulate downstream idempotent upsert using an ID-keyed dictionary.
def service_upsert_records(state: dict) -> dict:
    state["persisted"] = {record["external_id"]: record for record in state["mapped"]}
    state["upsert_count"] = len(state["persisted"])
    return state


## Run and verify
`pip install -r requirements.txt && pytest -q`

## Diagram
See STEP-4.crd. The final `.inkp` is created after Stage 2.
