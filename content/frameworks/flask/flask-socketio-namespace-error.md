---
title: "[Solution] Flask SocketIO Namespace Error"
description: "Namespace not connecting."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Namespace not connecting.

## Common Causes

Wrong path.

## How to Fix

Use correct namespace.

## Example

```python
@sio.on('msg', namespace='/chat')
def h(d): emit('resp', d, namespace='/chat')
```
