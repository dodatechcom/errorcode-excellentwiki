---
title: "[Solution] Uncaught Exception in Node.js — Global Error Handler"
description: "Handle uncaught exceptions in Node.js with process.on('uncaughtException') and prevent process crashes."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Uncaught Exception Handler

## Setup

```javascript
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
});
```

## Best Practice

Log the error, then exit after a brief delay to allow I/O flushing:

```javascript
process.on('uncaughtException', (err) => {
  console.error(err);
  process.exitCode = 1;
  setTimeout(() => process.exit(1), 1000);
});
```
