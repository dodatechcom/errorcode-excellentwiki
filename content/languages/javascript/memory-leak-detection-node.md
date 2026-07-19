---
title: "[Solution] Memory Leak Detection in Node.js — Heap Snapshot & Profiling"
description: "Detect and fix memory leaks in Node.js using heap snapshots, process.memoryUsage(), and Chrome DevTools."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Memory Leak Detection in Node.js

## Monitor Memory

```javascript
setInterval(() => {
  const used = process.memoryUsage();
  console.log({
    rss: Math.round(used.rss / 1024 / 1024) + 'MB',
    heap: Math.round(used.heapUsed / 1024 / 1024) + 'MB',
  });
}, 10000);
```

## Take Heap Snapshot

```bash
# Via Chrome DevTools
node --inspect script.js
# Open chrome://inspect

# Programmatic snapshot
node --heapsnapshot-signal=SIGUSR2 script.js
```

## Common Leak Sources

- Global arrays that grow
- Event listeners not removed
- Closures capturing large objects
- Timers not cleared
