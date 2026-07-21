---
title: "SQLite Migration Error"
description: "Fix SQLite database schema migration errors in Android upgrades"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Database upgrade fails because schema migration SQL is incorrect

## Common Causes

- ALTER TABLE syntax incompatible with SQLite
- Column type change not supported directly
- Migration SQL does not account for existing data
- Database version number not incremented

## Fixes

- Use CREATE TABLE AS SELECT for complex migrations
- Back up data, recreate table, restore for type changes
- Test migration with real data
- Increment DATABASE_VERSION constant

## Code Example

```kotlin
private const val DATABASE_VERSION = 2

override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
    if (oldVersion < 2) {
        // Add column with default value
        db.execSQL("ALTER TABLE users ADD COLUMN email TEXT DEFAULT ''")
    }
    if (oldVersion < 3) {
        // Complex migration: recreate table
        db.execSQL("CREATE TABLE users_new (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
        db.execSQL("INSERT INTO users_new (id, name, email) SELECT id, name, COALESCE(email, '') FROM users")
        db.execSQL("DROP TABLE users")
        db.execSQL("ALTER TABLE users_new RENAME TO users")
    }
}
```

# SQLite ALTER TABLE limitations:
# - Can ADD COLUMN
# - Can RENAME table
# - Cannot DROP COLUMN (before 3.35.0)
# - Cannot change column type
