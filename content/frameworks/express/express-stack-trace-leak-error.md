---
title: "[Solution] Express Error Stack Trace Leak Error"
description: "Fix Express error stack trace leaks that expose internal application details to clients in production."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An error stack trace leak in Express occurs when the full error stack is sent in the response, exposing internal file paths, library versions, and code structure to attackers.

## Common Causes

- Error handler sends `err.stack` in the response body
- Default Express error handler sends stack in development mode
- Third-party middleware logs errors with full stack traces to stdout
- `NODE_ENV` not set to `production`, enabling verbose errors
- Error objects contain sensitive data in their properties

## How to Fix

1. Create a production-safe error handler:

```javascript
app.use((err, req, res, next) => {
  const isDev = process.env.NODE_ENV !== 'production';

  console.error(err.stack); // Log server-side only

  res.status(err.status || 500).json({
    error: {
      message: isDev ? err.message : 'Internal Server Error',
      ...(isDev && { stack: err.stack, code: err.code })
    }
  });
});
```

2. Sanitize error objects before logging:

```javascript
function sanitizeError(err) {
  const sanitized = { message: err.message, name: err.name };
  if (process.env.NODE_ENV === 'production') {
    delete sanitized.stack;
  } else {
    sanitized.stack = err.stack;
  }
  return sanitized;
}

app.use((err, req, res, next) => {
  console.error(JSON.stringify(sanitizeError(err)));
  res.status(500).json({ error: 'Internal Server Error' });
});
```

3. Use a structured logging library with level filtering:

```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.NODE_ENV === 'production' ? 'error' : 'debug',
  format: winston.format.json(),
  transports: [new winston.transports.File({ filename: 'error.log' })]
});

app.use((err, req, res, next) => {
  logger.error({
    message: err.message,
    stack: process.env.NODE_ENV !== 'production' ? err.stack : undefined,
    requestId: req.id
  });
  res.status(500).json({ error: 'Internal Server Error' });
});
```

## Examples

```javascript
// Vulnerable: sends stack to client
app.use((err, req, res, next) => {
  res.status(500).json({
    error: err.message,
    stack: err.stack // Exposes /app/src/services/db.js:42
  });
});

// Fixed: only send message in production
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: process.env.NODE_ENV === 'production'
      ? 'Internal Server Error'
      : err.message
  });
});
```

```text
Error: connect ECONNREFUSED 127.0.0.1:5432
    at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1141:16)
```
