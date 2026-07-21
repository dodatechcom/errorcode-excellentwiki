---
title: "SQLite Cursor Error"
description: "Fix SQLite Cursor errors when reading data from database queries"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Cursor throws exception or returns incorrect data when reading query results

## Common Causes

- Cursor not closed after use causing leak
- Column index accessed by name instead of index
- Cursor positioned before first row
- Null value not handled when reading column

## Fixes

- Use use{} block to auto-close cursor
- Use getColumnIndexOrThrow for safe column access
- Move cursor to first row before reading
- Check for null before reading column values

## Code Example

```kotlin
// WRONG: manual close
val cursor = db.query("users", null, null, null, null, null, null)
val name = cursor.getString(cursor.getColumnIndex("name"))
cursor.close()  // May not close on exception!

// CORRECT: auto-close with use
val cursor = db.query("users", null, null, null, null, null, null)
cursor.use { c ->
    while (c.moveToNext()) {
        val name = c.getString(c.getColumnIndexOrThrow("name"))
        val age = c.getInt(c.getColumnIndexOrThrow("age"))
    }
}
```

# Use cursor.use { } for auto-close
# getColumnIndexOrThrow for safe access
# moveToNext() iterates through rows
# Always check null before reading
