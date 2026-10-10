# Reconcile synchronized state — one service with a single bounded responsibility.
# Compare upstream IDs to downstream IDs after the upsert.
def service_reconcile(state: dict) -> dict:
    upstream = {row["id"] for row in state["records"]}
    downstream = set(state["persisted"])
    state["reconciliation"] = {"missing": sorted(upstream-downstream), "extra": sorted(downstream-upstream), "matched": len(upstream & downstream)}
    return state
