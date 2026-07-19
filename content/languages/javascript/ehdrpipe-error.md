---
title: "[Solution] EHDRPIPE — Broken Pipe Error in Node.js"
description: "Fix EHDRPIPE broken pipe errors when writing to a closed pipe or process."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EHDRPIPE — Broken Pipe Error

Occurs when writing to a pipe whose read end has been closed.

## Common Scenario

```bash
# Pipe broken
node script.js | grep something
# If grep exits early, node gets EPIPE
```

## Fix

```javascript
process.stdout.on('error', (err) => {
  if (err.code === 'EPIPE') process.exit(0);
  throw err;
});
```
