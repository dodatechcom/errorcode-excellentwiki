---
title: "[Solution] TypeORM: Entity Not Found Fix"
description: "Fix TypeORM EntityNotFoundError when querying entities that don't exist. Handle missing records, query builders, and find options."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["typeorm", "database", "orm", "entity", "postgresql"]
weight: 5
---

# TypeORM: Entity Not Found

This error occurs when TypeORM methods like `findOneOrFail` or `createQueryBuilder` cannot find the requested entity in the database. It is an intentional error to signal missing records.

## What This Error Means

Common error messages:

- `EntityNotFoundError: Could not find any entity of type "User" matching: { id: 999 }`
- `EntityNotFoundError: Could not find any entity of type "Post"`
- `NotFoundError: No results for query: SELECT ... WHERE "id" = $1`

TypeORM throws `EntityNotFoundError` (which extends `NotFoundError`) when `findOneOrFail` returns no results.

## Common Causes

```javascript
// Cause 1: findOneOrFail with non-existent ID
const user = await AppDataSource.getRepository(User).findOneOrFail({
  where: { id: 999 },
});

// Cause 2: QueryBuilder returns empty
const user = await AppDataSource.getRepository(User)
  .createQueryBuilder('user')
  .where('user.email = :email', { email: 'nobody@example.com' })
  .getOneOrFail();

// Cause 3: ID from URL parameter is wrong
const userId = parseInt(req.params.id); // NaN from bad input
const user = await UserRepository.findOneOrFail({ where: { id: userId } });

// Cause 4: Soft-deleted records excluded by default
const user = await UserRepository.findOneOrFail({
  where: { id: userId },
  withDeleted: false,
});

// Cause 5: Conditions don't match any record
const user = await UserRepository.findOneOrFail({
  where: { email: 'wrong@email.com', status: 'active' },
});
```

## How to Fix

### Fix 1: Use findOne instead of findOneOrFail

```javascript
const user = await UserRepository.findOne({ where: { id } });
if (!user) {
  return res.status(404).json({ error: 'User not found' });
}
return user;
```

### Fix 2: Wrap findOneOrFail in try/catch

```javascript
try {
  const user = await UserRepository.findOneOrFail({ where: { id } });
  return user;
} catch (err) {
  if (err instanceof EntityNotFoundError) {
    return null;
  }
  throw err;
}
```

### Fix 3: Validate ID before querying

```javascript
app.get('/users/:id', async (req, res) => {
  const id = parseInt(req.params.id);
  if (isNaN(id)) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }

  const user = await UserRepository.findOne({ where: { id } });
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }
  res.json(user);
});
```

### Fix 4: Use findMany for collections

```javascript
const users = await UserRepository.find({
  where: { status: 'active' },
});
// Returns empty array instead of throwing
```

### Fix 5: Include soft-deleted records if needed

```javascript
const user = await UserRepository.findOne({
  where: { id },
  withDeleted: true,
});
```

## Examples

```
EntityNotFoundError: Could not find any entity of type "User" matching: {
  "where": { "id": 999 }
}
    at new EntityNotFoundError (src/error/EntityNotFoundError.ts:11:9)
    at EntityRepository.findOneOrFail (src/repository/Repository.ts:142:15)
```

```javascript
// Fix: create a helper function
async function findByIdOrThrow(repo, id, entityType) {
  const entity = await repo.findOne({ where: { id } });
  if (!entity) {
    const err = new Error(`${entityType} with id ${id} not found`);
    err.status = 404;
    throw err;
  }
  return entity;
}

const user = await findByIdOrThrow(UserRepository, userId, 'User');
```

## Related Errors

- [Prisma Error V2]({{< relref "/languages/javascript/prisma-error-v2" >}}) — PrismaClientKnownRequestError
- [Mongoose CastError V2]({{< relref "/languages/javascript/mongoose-cast-error-v2" >}}) — CastError to ObjectId
- [Bull Queue Error V2]({{< relref "/languages/javascript/bull-queue-error-v2" >}}) — job processing failed
