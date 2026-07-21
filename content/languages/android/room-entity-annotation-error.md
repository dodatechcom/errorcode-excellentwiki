---
title: "Room Entity Annotation Error"
description: "Fix Room @Entity annotation errors for database table configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room build fails because entity class has incorrect or missing annotations

## Common Causes

- @Entity missing on data class
- primaryKeys not defined for composite key
- indices not specified for frequently queried columns
- foreignKeys missing for relational tables

## Fixes

- Add @Entity(tableName = "table_name") to data class
- Define primaryKeys array for composite primary keys
- Add @Index on frequently queried columns
- Define foreignKeys with proper onDelete/onUpdate actions

## Code Example

```kotlin
@Entity(
    tableName = "users",
    indices = [Index(value = ["email"], unique = true)],
    foreignKeys = [ForeignKey(
        entity = Org::class,
        parentColumns = ["id"],
        childColumns = ["orgId"],
        onDelete = ForeignKey.CASCADE
    )]
)
data class User(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val name: String,
    val email: String,
    val orgId: Long
)
```

# Verify entity matches SQL schema
# Use @ColumnInfo to customize column names
# Add @Ignore for fields not in database
