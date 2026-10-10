# Step 2 of 6 — Fetch cursor pages

## Capability
# Simulated cursor pagination: local provider fixture with two pages.
def service_fetch_pages(state: dict) -> dict:
    pages = [[{"id": "a", "qty": 1}], [{"id": "b", "qty": 2}]]
    state["records"] = [item for page in pages for item in page]
    state["pages_fetched"] = len(pages)
    return state


## Run and verify
`pip install -r requirements.txt && pytest -q`

## Diagram
See STEP-2.crd. The final `.inkp` is created after Stage 2.
