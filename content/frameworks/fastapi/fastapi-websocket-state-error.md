---
title: "[Solution] FastAPI WebSocket State Error"
description: "WebSocket in wrong state."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket in wrong state.

## Common Causes

Not accepted.

## How to Fix

Accept first.

## Example

```python
await websocket.accept()
await websocket.send_text('hello')
```
