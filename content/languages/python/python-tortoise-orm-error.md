---
title: "[Solution] Python Tortoise ORM Error — How to Fix"
description: "Fix Python Tortoise ORM errors. Resolve query failures, migration issues, and connection pool errors."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Tortoise ORM Error

A `tortoise.exceptions.IntegrityError` or `OperationalError` occurs when Tortoise ORM fails to execute queries due to constraint violations, missing model registrations, or connection issues.

## Why It Happens

Tortoise ORM is an async Python ORM. Errors arise when models are not registered before querying, when unique constraints are violated, when foreign key references point to non-existent records, or when the database connection is not properly initialized.

## Common Error Messages

- `IntegrityError: UNIQUE constraint failed: users.email`
- `OperationalError: relation "users" does not exist`
- `ConfigurationError: No DB associated with model`
- `IntegrityError: FOREIGN KEY constraint failed`

## How to Fix It

### Fix 1: Initialize Tortoise properly

```python
from tortoise import Tortoise, run_async
from tortoise.models import Model
from tortoise import fields

# Wrong — querying before initialization
# class User(Model):
#     name = fields.CharField(max_length=100)
# await User.all()  # ConfigurationError

# Correct — initialize before querying
async def init():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["__main__"]},
    )
    await Tortoise.generate_schemas()

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=255, unique=True)

run_async(init())
```

### Fix 2: Handle unique constraint errors

```python
import asyncio
from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.exceptions import IntegrityError

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=255, unique=True)

    class Meta:
        table = "users"

async def create_user():
    try:
        user = await User.create(name="Alice", email="alice@example.com")
        print(f"Created: {user.id}")
    except IntegrityError as e:
        print(f"User already exists: {e}")
        user = await User.get(email="alice@example.com")
        print(f"Found existing: {user.name}")

# Run with proper init
async def main():
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()
    await create_user()

asyncio.run(main())
```

### Fix 3: Use proper query patterns

```python
import asyncio
from tortoise import Tortoise, fields
from tortoise.models import Model

class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    author = fields.ForeignKeyField("models.User", related_name="posts")

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)

    class Meta:
        table = "users"

async def query_posts():
    # Use select_related for joins
    posts = await Post.all().select_related("author")
    for post in posts:
        print(f"{post.title} by {post.author.name}")

    # Use prefetch_related for reverse relations
    users = await User.all().prefetch_related("posts")
    for user in users:
        print(f"{user.name} has {len(user.posts)} posts")
```

## Common Scenarios

- **Model not registered** — Querying a model that was not added to the Tortoise config modules.
- **Unique constraint** — Creating duplicate records that violate unique constraints.
- **Foreign key missing** — Referencing a related object that does not exist in the database.

## Prevent It

- Always call `Tortoise.init()` and `generate_schemas()` before any database operations.
- Wrap `create()` calls in try/except `IntegrityError` to handle duplicate records gracefully.
- Use `select_related()` and `prefetch_related()` to avoid N+1 query problems.

## Related Errors

- [IntegrityError](/languages/python/integrity-error/) — database constraint violated
- [OperationalError](/languages/python/operationalerror/) — database operation failed
- [ConfigurationError](/languages/python/config-error/) — Tortoise not initialized
