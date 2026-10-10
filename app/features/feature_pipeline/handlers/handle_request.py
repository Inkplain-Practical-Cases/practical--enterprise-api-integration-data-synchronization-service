# Application handler: orchestrates the single-purpose validation service.
from app.features.feature_pipeline.schemas.request import SyncRequest
from app.features.feature_pipeline.services.service_validate import service_validate
def handle_request(body: SyncRequest) -> dict:
    # Convert the validated contract to the service boundary.
    return service_validate(body.model_dump())
