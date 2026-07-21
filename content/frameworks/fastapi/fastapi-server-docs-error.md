---
title: "[Solution] FastAPI Server Docs Error"
description: "Server info not in docs."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Server info not in docs.

## Common Causes

Not configured.

## How to Fix

Set servers.

## Example

```python
app = FastAPI(servers=[{'url': 'https://api.example.com', 'description': 'Prod'}])
```
