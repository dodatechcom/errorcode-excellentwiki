---
title: "[Solution] FastAPI WebSocket Protocol Error"
description: "WebSocket protocol error."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket protocol error.

## Common Causes

Wrong protocol.

## How to Fix

Use ws:// or wss://.

## Example

```python
@app.websocket('/ws')
async def ws(websocket: WebSocket):
    await websocket.accept()
```
