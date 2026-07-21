---
title: "SQLite Database Locked Error"
description: "Fix Android SQLite database locked errors from concurrent access"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
SQLite throws database is locked exception because of concurrent write attempts

## Common Causes

- Multiple threads accessing same database connection
- Write transaction left open by previous operation
- Database closed while query still executing
- Content provider and direct access conflicting

## Fixes

- Use WAL mode for concurrent read/write
- Ensure database is not closed during active queries
- Use a single database connection per thread
- Use Room for proper connection management

## Code Example

```kotlin
// Enable WAL mode for better concurrency
val db = dbHelper.writableDatabase
db.execSQL("PRAGMA journal_mode=WAL;")

// Close database properly
try {
    db.beginTransaction()
    // ... operations
    db.setTransactionSuccessful()
} finally {
    db.endTransaction()
    // Do NOT close database here - let SQLite handle it
}
```

# WAL mode allows concurrent reads + single write
# Room handles connection pooling automatically
# Never close database in normal operation
