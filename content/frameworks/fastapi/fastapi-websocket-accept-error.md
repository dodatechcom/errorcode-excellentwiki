---
title: "[Solution] FastAPI WebSocket Accept Error"
description: "WebSocket not accepting."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket not accepting.

## Common Causes

Not calling accept.

## How to Fix

Call accept first.

## Example

```python
await websocket.accept()
```
