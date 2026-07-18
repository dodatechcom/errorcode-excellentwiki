---
title: "[Solution] Express Middleware next() Not Called Error — How to Fix"
description: "Fix Express middleware next() errors. Resolve middleware not calling next, request hanging, and middleware chain issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

An Express middleware next() not called error occurs when a middleware function fails to invoke `next()`, causing the request to hang indefinitely. Middleware must either send a response or call `next()` to proceed.

## Why It Happens

Express processes middleware sequentially. Each middleware must call `next()` to pass control to the next middleware or route handler. The error occurs when a middleware forgets to call `next()`, when an exception is thrown without error handling, when async middleware doesn't handle promise rejections, or when middleware conditionally skips `next()`.

## Common Error Messages

```
Error: Headers have already been sent
```

```
ERR_HTTP_HEADERS_SENT: Cannot set headers after they are sent to the client
```

```
TimeoutError: Request timed out after 30000ms
```

```
Error [ERR_HTTP_HEADERS_SENT]: Cannot set headers after they are sent
```

## How to Fix It

### 1. Always Call next() or Send a Response

Every middleware must complete the request cycle:

```javascript
// Good: calls next() to continue
function loggingMiddleware(req, res, next) {
    console.log(`${req.method} ${req.url}`);
    next();  // Always call next
}

// Good: sends response without calling next
function authMiddleware(req, res, next) {
    if (!req.user) {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    next();  // Only called if user is authenticated
}

// Bad: request hangs
function brokenMiddleware(req, res, next) {
    if (req.user) {
        // Missing next() here!
    }
}
```

### 2. Handle Async Middleware Properly

Wrap async middleware with try-catch:

```javascript
async function asyncMiddleware(req, res, next) {
    try {
        const data = await fetchData();
        req.data = data;
        next();
    } catch (error) {
        next(error);  // Pass errors to Express error handler
    }
}

// Or use express-async-errors for automatic handling
require('express-async-errors');

app.get('/data', async (req, res) => {
    const data = await fetchData();
    res.json(data);
});
```

### 3. Use Express Error Handler

Create a centralized error handler:

```javascript
// Error handling middleware (must have 4 parameters)
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(err.status || 500).json({
        error: {
            message: err.message || 'Internal Server Error',
            ...(process.env.NODE_ENV === 'development' && { stack: err.stack }),
        },
    });
});

// Custom error class
class AppError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.statusCode = statusCode;
        this.isOperational = true;
    }
}

// Usage in middleware
function requireAuth(req, res, next) {
    if (!req.session.userId) {
        throw new AppError('Authentication required', 401);
    }
    next();
}
```

### 4. Ensure Middleware Order Is Correct

Register middleware before routes that need it:

```javascript
const express = require('express');
const app = express();

// Global middleware (runs on every request)
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());
app.use(helmet());

// Route-specific middleware
app.use('/api', apiKeyMiddleware);
app.use('/admin', adminAuthMiddleware);

// Routes
app.use('/api', apiRoutes);
app.use('/admin', adminRoutes);

// Error handler (must be last)
app.use(errorHandler);
```

## Common Scenarios

**Scenario 1: Request hangs with no response.**
This is the classic symptom of a missing `next()`. Use request logging middleware to identify which middleware is the last to execute before the hang.

**Scenario 2: Double response error.**
Calling both `res.send()` and `next()` causes "headers already sent" error. Use `return` to exit after sending a response.

**Scenario 3: Async middleware fails silently.**
Unhandled promise rejections in async middleware don't automatically call `next(error)`. Always wrap async code in try-catch.

## Prevent It

1. **Use linting rules** to enforce that middleware functions call `next()` or send a response.

2. **Test middleware in isolation** by creating mock req/res/next objects.

3. **Use `express-async-errors`** to automatically catch async errors in middleware.
