---
title: "SQLite Constraint Error"
description: "Fix SQLite constraint violation errors when inserting or updating records"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
SQLite throws constraint exception on INSERT or UPDATE operations

## Common Causes

- PRIMARY KEY constraint violated on duplicate insert
- UNIQUE constraint violated by duplicate value
- NOT NULL constraint violated by null value
- FOREIGN KEY constraint violated by invalid reference

## Fixes

- Use INSERT OR REPLACE for upsert operations
- Check for existing records before inserting
- Ensure required fields have non-null values
- Verify foreign key references exist in parent table

## Code Example

```kotlin
// WRONG: throws on duplicate
db.insert("users", null, values)

// CORRECT: replace on conflict
db.insertWithOnConflict("users", null, values,
    SQLiteDatabase.CONFLICT_REPLACE)

// Or use INSERT OR IGNORE:
db.execSQL("INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)",
    arrayOf(1, "John"))

// With Room:
@Insert(onConflict = OnConflictStrategy.REPLACE)
suspend fun insertUser(user: User)
```

# CONFLICT_REPLACE: delete old, insert new
# CONFLICT_IGNORE: skip if exists
# CONFLICT_ROLLBACK: abort transaction
# CONFLICT_ABORT: cancel current statement
