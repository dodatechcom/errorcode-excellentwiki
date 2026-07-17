---
title: "[Solution] sea-orm Entity Not Found Error Fix"
description: "Fix sea-orm entity not found errors. Handle missing entities, relationship loading, and query result handling."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# sea-orm Entity Not Found Error

Fix sea-orm entity not found errors. Handle missing entities, relationship loading, and query result handling.

## What This Error Means

sea-orm entity not found errors occur when a query that expects exactly one result returns none:

```
EntityNotFound: "Entity not found: User"
CustomError: record not found
```

## Common Causes

```rust
// Cause 1: Querying for an entity that does not exist
let user = User::find_by_id(999).one(&db).await?.unwrap(); // None

// Cause 2: Filtering returns no matching rows
let user = User::find()
    .filter(user::Column::Email.eq("nobody@example.com"))
    .one(&db).await?.unwrap(); // None

// Cause 3: Relationship not loaded
// Cause 4: Table is empty after migration
```

## How to Fix

### Fix 1: Handle Option properly

```rust
use sea_orm::*;

async fn get_user(db: &DatabaseConnection, user_id: i64) -> Result<user::Model, DbErr> {
    User::find_by_id(user_id)
        .one(db)
        .await?
        .ok_or(DbErr::Custom("User not found".to_owned()))
}
```

### Fix 2: Use find_with_related for relationship queries

```rust
async fn get_user_with_posts(db: &DatabaseConnection, user_id: i64) -> Result<(), DbErr> {
    let user = User::find_by_id(user_id)
        .find_with_related(Post)
        .all(db)
        .await?;

    if user.is_empty() {
        return Err(DbErr::Custom("User not found".to_owned()));
    }

    let (user, posts) = &user[0];
    println!("User: {}, Posts: {}", user.name, posts.len());
    Ok(())
}
```

### Fix 3: Use find_or_err for cleaner code

```rust
async fn get_user(db: &DatabaseConnection, user_id: i64) -> Result<user::Model, DbErr> {
    User::find_by_id(user_id)
        .one(db)
        .await?
        .ok_or(DbErr::RecordNotFound("User not found".to_owned()))
}
```

## Examples

```rust
use sea_orm::*;

async fn example(db: DatabaseConnection) -> Result<(), DbErr> {
    // Insert a user first
    let user = user::ActiveModel {
        name: Set("Alice".to_owned()),
        email: Set("alice@example.com".to_owned()),
        ..Default::default()
    };

    let inserted = user.insert(&db).await?;

    // Now query it back
    let found = User::find_by_id(inserted.id)
        .one(&db)
        .await?;

    match found {
        Some(user) => println!("Found user: {}", user.name),
        None => println!("User not found"),
    }

    Ok(())
}
```

## Related Errors

- [Sea-ORM Error]({{< relref "/languages/rust/sea-orm-error" >}}) — sea-orm error
- [Diesel Error]({{< relref "/languages/rust/diesel-error" >}}) — diesel error
- [SQLx Error]({{< relref "/languages/rust/sqlx-error-v2" >}}) — sqlx error
