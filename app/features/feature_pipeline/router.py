# Thin HTTP door: delegates the request to the injected handler.
from fastapi import APIRouter
from app.features.feature_pipeline.handlers.handle_request import handle_request
from app.features.feature_pipeline.schemas.request import SyncRequest
router = APIRouter()
@router.post("/sync")
def submit(body: SyncRequest):
    return handle_request(body)
