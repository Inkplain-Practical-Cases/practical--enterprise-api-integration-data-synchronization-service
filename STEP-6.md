# Step 6 of 6 — Reconcile synchronized state

## Capability
# Compare upstream IDs to downstream IDs after the upsert.
def service_reconcile(state: dict) -> dict:
    upstream = {row["id"] for row in state["records"]}
    downstream = set(state["persisted"])
    state["reconciliation"] = {"missing": sorted(upstream-downstream), "extra": sorted(downstream-upstream), "matched": len(upstream & downstream)}
    return state


## Run and verify
`pip install -r requirements.txt && pytest -q`

## Diagram
See STEP-6.crd. The final `.inkp` is created after Stage 2.
