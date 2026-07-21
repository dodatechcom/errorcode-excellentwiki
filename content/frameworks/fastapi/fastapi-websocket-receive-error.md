---
title: "[Solution] FastAPI WebSocket Receive Error"
description: "WebSocket receive failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket receive failing.

## Common Causes

Not awaiting.

## How to Fix

Use await.

## Example

```python
data = await websocket.receive_text()
```
