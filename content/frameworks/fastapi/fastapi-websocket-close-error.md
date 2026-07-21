---
title: "[Solution] FastAPI WebSocket Close Error"
description: "WebSocket not closing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket not closing.

## Common Causes

Not calling close.

## How to Fix

Call close.

## Example

```python
await websocket.close()
```
