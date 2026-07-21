---
title: "[Solution] FastAPI WebSocket Send Error"
description: "WebSocket send failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket send failing.

## Common Causes

Connection closed.

## How to Fix

Check connection.

## Example

```python
await websocket.send_text('response')
```
