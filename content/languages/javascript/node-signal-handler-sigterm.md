---
title: "[Solution] Node.js SIGTERM Handler — Graceful Shutdown Fix"
description: "Fix Node.js not handling SIGTERM for graceful shutdown. Add signal handlers for SIGTERM and SIGINT."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Node.js SIGTERM Handler

```javascript
process.on('SIGTERM', () => {
  console.log('SIGTERM received — shutting down gracefully');
  server.close(() => {
    db.close();
    process.exit(0);
  });
  // Force exit after timeout
  setTimeout(() => process.exit(1), 10000);
});

process.on('SIGINT', () => {
  process.emit('SIGTERM');
});
```
