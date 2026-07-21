---
title: "Room Index Error"
description: "Fix Room database indexing and query performance optimization errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room database queries are slow because of missing or incorrect indexes

## Common Causes

- Frequently queried columns not indexed
- Composite index not defined for multi-column queries
- Index not matching query WHERE clause
- Unused indexes wasting storage

## Fixes

- Add @Index annotation on frequently queried columns
- Use composite index for multi-column queries
- Match index columns to query patterns
- Remove unused indexes

## Code Example

```kotlin
@Entity(
    tableName = "users",
    indices = [
        Index(value = ["email"], unique = true),
        Index(value = ["name", "email"]),  // Composite index
        Index(value = ["created_at"])  // For sorting
    ]
)
data class User(
    @PrimaryKey val id: Long,
    val name: String,
    val email: String,
    @ColumnInfo(name = "created_at") val createdAt: Long
)

// Query benefits from index:
@Query("SELECT * FROM users WHERE name = :name AND email = :email")
suspend fun findByNameAndEmail(name: String, email: String): User?
```

# Index on WHERE clause columns
# Composite index for multi-column queries
# Unique index for unique constraints
# Check query plans with EXPLAIN QUERY PLAN
