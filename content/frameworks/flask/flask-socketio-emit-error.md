---
title: "[Solution] Flask SocketIO Emit Error"
description: "emit not reaching clients."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

emit not reaching clients.

## Common Causes

Wrong event.

## How to Fix

Use correct name.

## Example

```python
@sio.on('connect')
def h(): emit('status', {'msg': 'Connected'})
```
