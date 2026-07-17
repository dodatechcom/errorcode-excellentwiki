---
title: "[Solution] PrismaClientKnownRequestError Fix"
description: "Fix PrismaClientKnownRequestError with specific error codes. Handle P2002 unique constraint, P2025 not found, and other Prisma database errors."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["prisma", "database", "orm", "postgresql", "mysql"]
weight: 5
---

# PrismaClientKnownRequestError

This error occurs when Prisma encounters a known database error during a query. Prisma wraps database-level errors with specific error codes that describe the exact issue.

## What This Error Means

Common error messages:

- `PrismaClientKnownRequestError: Unique constraint failed on the fields: (email)`
- `PrismaClientKnownRequestError: Record to update not found.`
- `PrismaClientKnownRequestError: Record to delete does not exist.`
- `PrismaClientKnownRequestError: Foreign key constraint failed.`
- `Error code: P2002`, `P2014`, `P2025`, `P2003`

Each Prisma error has a unique code. The most common are P2002 (unique constraint), P2014 (required relation), P2025 (record not found), and P2003 (foreign key).

## Common Causes

```javascript
// Cause 1: P2002 - Unique constraint violation
await prisma.user.create({
  data: { email: 'alice@example.com' }, // already exists
});

// Cause 2: P2014 - Required relation missing
await prisma.post.create({
  data: { title: 'Hello' }, // authorId is required
});

// Cause 3: P2025 - Record not found for update/delete
await prisma.user.update({
  where: { id: 999 }, // doesn't exist
  data: { name: 'Bob' },
});

// Cause 4: P2003 - Foreign key constraint
await prisma.post.create({
  data: {
    title: 'Post',
    authorId: 999, // user 999 doesn't exist
  },
});

// Cause 5: P2012 - Missing required argument
await prisma.user.create({
  data: {}, // name is required
});
```

## How to Fix

### Fix 1: Handle P2002 unique constraint

```javascript
try {
  const user = await prisma.user.create({
    data: { email: 'alice@example.com' },
  });
} catch (err) {
  if (err.code === 'P2002') {
    const field = err.meta?.target?.join(', ');
    console.error(`Duplicate value for: ${field}`);
    // Return existing record or use upsert
  }
  throw err;
}
```

### Fix 2: Use upsert for create-or-update

```javascript
const user = await prisma.user.upsert({
  where: { email: 'alice@example.com' },
  update: { name: 'Alice Updated' },
  create: { email: 'alice@example.com', name: 'Alice' },
});
```

### Fix 3: Handle P2025 not found

```javascript
try {
  const user = await prisma.user.update({
    where: { id: userId },
    data: { name: 'Bob' },
  });
} catch (err) {
  if (err.code === 'P2025') {
    return res.status(404).json({ error: 'User not found' });
  }
  throw err;
}
```

### Fix 4: Validate foreign keys before creating

```javascript
async function createPost(data) {
  const authorExists = await prisma.user.findUnique({
    where: { id: data.authorId },
  });

  if (!authorExists) {
    throw new Error('Author does not exist');
  }

  return prisma.post.create({ data });
}
```

### Fix 5: Use a generic error handler

```javascript
function handlePrismaError(err) {
  if (err.code === 'P2002') {
    return { status: 409, message: 'Resource already exists' };
  }
  if (err.code === 'P2025') {
    return { status: 404, message: 'Resource not found' };
  }
  if (err.code === 'P2003') {
    return { status: 400, message: 'Invalid reference' };
  }
  if (err.code === 'P2014') {
    return { status: 400, message: 'Missing required relation' };
  }
  return { status: 500, message: 'Database error' };
}
```

## Examples

```
PrismaClientKnownRequestError: Unique constraint failed on the fields: (`email`)
    at PrismaClient._request (node_modules/.prisma/client/runtime/index.js:...)
    at async createUser (src/services/user.js:10:18)
```

```javascript
// Fix: catch and handle gracefully
app.post('/users', async (req, res) => {
  try {
    const user = await prisma.user.create({ data: req.body });
    res.status(201).json(user);
  } catch (err) {
    const { status, message } = handlePrismaError(err);
    res.status(status).json({ error: message });
  }
});
```

## Related Errors

- [Prisma Error]({{< relref "/languages/javascript/prisma-error" >}}) — basic Prisma error
- [Mongoose Validation Error V2]({{< relref "/languages/javascript/mongoose-validation-error-v2" >}}) — validation error
- [TypeORM Error V2]({{< relref "/languages/javascript/typeorm-error-v2" >}}) — entity not found
