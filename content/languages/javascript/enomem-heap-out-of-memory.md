---
title: "[Solution] JavaScript Heap Out of Memory — FATAL ERROR: CALL_AND_RETRY_LAST Allocation Failed"
description: "Fix JavaScript heap out of memory errors in Node.js. Increase max-old-space-size, optimize code, and stream large data."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# JavaScript Heap Out of Memory

Node.js runs out of V8 heap memory.

## Quick Fix

```bash
node --max-old-space-size=4096 script.js

# Or via environment variable
export NODE_OPTIONS='--max-old-space-size=4096'
```

## Better Fixes

- Stream large files instead of reading all into memory
- Use `--max-old-space-size` in CI for builds
- Profile memory usage with `--inspect`

```javascript
// Stream large files
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: fs.createReadStream('large-file.txt'),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  // Process line by line
});
```
