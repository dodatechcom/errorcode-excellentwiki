---
title: "[Solution] Express Router Parameter Error — How to Fix"
description: "Fix Express router parameter errors. Resolve route parameter handling, param middleware, and URL matching issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

An Express router parameter error occurs when route parameters are missing, incorrectly named, or when `router.param()` middleware fails to process them. Route parameters are essential for RESTful API design.

## Why It Happens

Express route parameters capture values from the URL path. Errors occur when parameters are not included in the route definition, when `req.params` is accessed before the route matches, when `router.param()` callbacks don't call `next()`, or when parameter names don't match between route definition and param middleware.

## Common Error Messages

```
TypeError: Cannot read property 'id' of undefined
```

```
Error: Route parameter 'userId' not found in req.params
```

```
CastError: Cast to ObjectId failed for value "abc" at path "_id"
```

```
ReferenceError: req.params is not defined
```

## How to Fix It

### 1. Define Routes with Parameters Correctly

Use named parameters in route paths:

```javascript
const express = require('express');
const router = express.Router();

// Single parameter
router.get('/users/:id', (req, res) => {
    const { id } = req.params;
    res.json({ userId: id });
});

// Multiple parameters
router.get('/users/:userId/posts/:postId', (req, res) => {
    const { userId, postId } = req.params;
    res.json({ userId, postId });
});

// Optional parameters with regex
router.get('/users/:id?', (req, res) => {
    const id = req.params.id || 'default';
    res.json({ userId: id });
});
```

### 2. Use router.param() for Parameter Validation

Validate parameters before route handlers:

```javascript
router.param('id', (req, res, next, value) => {
    const id = parseInt(value, 10);
    if (isNaN(id) || id <= 0) {
        return res.status(400).json({ error: 'Invalid ID parameter' });
    }
    req.parsedId = id;
    next();
});

router.get('/users/:id', (req, res) => {
    // req.parsedId is validated and parsed
    User.findById(req.parsedId)
        .then(user => res.json(user))
        .catch(() => res.status(404).json({ error: 'User not found' }));
});
```

### 3. Handle Parameter Errors in Express 5

Express 5 supports async parameter validation:

```javascript
// Express 5 pattern
router.param('id', async (req, res, next, value) => {
    try {
        const item = await Item.findById(value);
        if (!item) {
            return res.status(404).json({ error: 'Item not found' });
        }
        req.item = item;
        next();
    } catch (error) {
        next(error);
    }
});

router.get('/items/:id', (req, res) => {
    res.json(req.item);
});
```

### 4. Use Route Prefixes with Parameters

Structure routes with proper prefixes:

```javascript
const userRouter = express.Router({ mergeParams: true });

userRouter.get('/', (req, res) => {
    // Access params from parent router
    const { organizationId } = req.params;
    res.json({ organizationId });
});

userRouter.get('/:userId', (req, res) => {
    const { organizationId, userId } = req.params;
    res.json({ organizationId, userId });
});

app.use('/organizations/:organizationId/users', userRouter);
```

## Common Scenarios

**Scenario 1: Parameter is undefined in route handler.**
Check that the parameter name in the route definition matches what you access in `req.params`. Parameters are case-sensitive.

**Scenario 2: Optional parameter always returns undefined.**
In Express, `/:id?` makes the parameter optional, but `req.params.id` may not work as expected. Use a regex or check for undefined:

```javascript
router.get('/users/:id?', (req, res) => {
    if (req.params.id === undefined) {
        // List all users
    } else {
        // Get specific user
    }
});
```

**Scenario 3: Parameter middleware doesn't run.**
`router.param()` only applies to routes defined on that specific router instance. Define param middleware before the routes, or use it at the app level.

## Prevent It

1. **Validate parameters early** using `router.param()` or middleware to catch invalid inputs before they reach route handlers.

2. **Use TypeScript** with Express to get type safety for route parameters and catch mismatches at compile time.

3. **Write integration tests** that exercise routes with various parameter combinations, including invalid and missing values.
