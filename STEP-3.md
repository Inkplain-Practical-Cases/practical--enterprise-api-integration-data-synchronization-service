# Step 3 of 6 — Validate and map external records

## Capability
# Transform upstream records to the canonical downstream API contract.
def service_map_records(state: dict) -> dict:
    state["mapped"] = [{"external_id": x["id"], "quantity": int(x["qty"])} for x in state["records"]]
    return state


## Run and verify
`pip install -r requirements.txt && pytest -q`

## Diagram
See STEP-3.crd. The final `.inkp` is created after Stage 2.
