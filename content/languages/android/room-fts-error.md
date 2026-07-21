---
title: "Room FTS Error"
description: "Fix Room Full-Text Search (FTS) entity configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room FTS entity does not support full-text search queries

## Common Causes

- FTS entity not properly annotated
- Virtual table not created in migration
- FTS match query syntax incorrect
- FTS entity does not match main entity schema

## Fixes

- Annotate FTS entity with @Fts4 or @Fts3
- Create FTS virtual table in database migration
- Use FTS match syntax: column :query
- Ensure FTS entity columns match FTS entity

## Code Example

```kotlin
@Fts4
@Entity(tableName = "users_fts")
data class UserFts(
    @ColumnInfo(name = "name") val name: String,
    @ColumnInfo(name = "email") val email: String
)

// Query using FTS:
@Query("SELECT * FROM users WHERE rowid IN (SELECT rowid FROM users_fts WHERE users_fts MATCH :query)")
suspend fun searchUsers(query: String): List<User>
```

# @Fts4: full-text search (recommended)
# @Fts3: older FTS version
# FTS queries use MATCH operator
# Results joined with main table by rowid
