---
title: "[Solution] EADDRINUSE — Port Already in Use Fix"
description: "Fix EADDRINUSE when another process is using your port. Find and kill the process, or use a different port."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EADDRINUSE — Port Already in Use

Another process is listening on the requested port.

## Find and Kill

```bash
# Find process on port 3000
lsof -i :3000

# Kill it
kill -9 <PID>

# Or one-liner
fuser -k 3000/tcp
```

## Use a Different Port

```javascript
const server = app.listen(0, () => {
  console.log('Listening on port', server.address().port);
});
```
