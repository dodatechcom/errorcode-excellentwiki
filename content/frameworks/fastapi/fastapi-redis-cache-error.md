---
title: "[Solution] FastAPI Redis Cache Error"
description: "Redis connection failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Redis connection failing.

## Common Causes

Redis not running.

## How to Fix

Check connection.

## Example

```python
import redis
r = redis.Redis(host='localhost', port=6379)
```
