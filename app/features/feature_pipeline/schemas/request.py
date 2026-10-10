# Input contract: Pydantic validates fields at the external boundary.
from pydantic import BaseModel, Field
class SyncRequest(BaseModel):
    tenant_id: str = Field(min_length=1)
    source_id: str = Field(min_length=1)
