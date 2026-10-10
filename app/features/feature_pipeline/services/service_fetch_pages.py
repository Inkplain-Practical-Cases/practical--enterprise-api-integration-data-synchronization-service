# Fetch cursor pages — one service with a single bounded responsibility.
# Simulated cursor pagination: local provider fixture with two pages.
def service_fetch_pages(state: dict) -> dict:
    pages = [[{"id": "a", "qty": 1}], [{"id": "b", "qty": 2}]]
    state["records"] = [item for page in pages for item in page]
    state["pages_fetched"] = len(pages)
    return state
