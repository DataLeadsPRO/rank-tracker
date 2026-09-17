import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://data.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('Rank Tracker API')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "rank_check",
    "method": "POST",
    "path": "/rank/check",
    "description": "V1 Rank Check"
  },
  {
    "name": "rank_trackers_create",
    "method": "POST",
    "path": "/rank/trackers/create",
    "description": "V1 Rank Trackers Create"
  },
  {
    "name": "rank_trackers_list",
    "method": "POST",
    "path": "/rank/trackers/list",
    "description": "V1 Rank Trackers List"
  },
  {
    "name": "rank_trackers_results",
    "method": "POST",
    "path": "/rank/trackers/results",
    "description": "V1 Rank Trackers Results"
  },
  {
    "name": "rank_trackers_check_now",
    "method": "POST",
    "path": "/rank/trackers/check-now",
    "description": "V1 Rank Trackers Check Now"
  },
  {
    "name": "rank_trackers_delete",
    "method": "POST",
    "path": "/rank/trackers/delete",
    "description": "V1 Rank Trackers Delete"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
