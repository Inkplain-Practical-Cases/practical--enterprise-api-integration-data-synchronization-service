"""Record HTTP synchronization boundaries and outcomes to a real SQLite store."""
import asyncio
import time
from starlette.middleware.base import BaseHTTPMiddleware
from app.providers.provider_record_request_audit import provider_record_request_audit
class RequestAuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request,call_next):
        started=time.perf_counter()
        response=await call_next(request)
        path=getattr(request.scope.get("route"),"path",request.url.path)
        await asyncio.to_thread(provider_record_request_audit,request.method,path,response.status_code,(time.perf_counter()-started)*1000)
        return response
