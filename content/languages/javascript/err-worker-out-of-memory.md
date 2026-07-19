---
title: "[Solution] Worker Thread Out of Memory — Heap Limit in Node.js Worker Threads"
description: "Fix out of memory errors in Node.js worker threads. Set per-worker heap limits and manage thread pool size."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Worker Thread Out of Memory

Worker threads share the same process memory limits by default.

## Fix

```javascript
const { Worker } = require('worker_threads');

const worker = new Worker('./heavy-task.js', {
  workerData: { maxHeapSize: 1024 * 1024 * 512 }
});
```

```bash
# Increase heap per worker
node --max-old-space-size=4096 worker-main.js
```

## Reduce Pool Size

```javascript
const os = require('os');
const poolSize = Math.max(1, os.cpus().length - 1);
```
