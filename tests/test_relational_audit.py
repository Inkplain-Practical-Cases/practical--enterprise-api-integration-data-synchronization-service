"""Check synchronized HTTP request/event SQLite parent-child links."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit
def test_sync_audit_database(tmp_path):
    path=str(tmp_path/"sync.sqlite3")
    rid=provider_record_request_audit("POST","/sync",200,5.2,path)
    with sqlite3.connect(path) as c:
        assert c.execute("SELECT COUNT(*) FROM sync_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert c.execute("SELECT COUNT(*) FROM sync_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert c.execute("PRAGMA foreign_key_check").fetchall()==[]
