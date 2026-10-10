# Handler: validates the request and orchestrates the six-step enterprise sync chain.
from app.features.feature_pipeline.schemas.request import SyncRequest
from app.features.feature_pipeline.services.service_validate import service_validate
from app.features.feature_pipeline.services.service_fetch_pages import service_fetch_pages
from app.features.feature_pipeline.services.service_map_records import service_map_records
def handle_request(body: SyncRequest) -> dict:
    state = service_validate(body.model_dump())
    state = service_fetch_pages(state)
    state = service_map_records(state)
    return state
