---
title: "Room Type Parameter Error"
description: "Fix Room type parameter and generic type errors in DAO queries"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room DAO queries fail because of unsupported generic type parameters

## Common Causes

- Generic type in DAO not supported by Room
- List<T> return type not properly handled
- TypeConverter not handling generic types
- Raw query returning wrong type

## Fixes

- Use concrete types in DAO method parameters
- Use @TypeConverters for generic containers
- Return Flow<List<Entity>> for reactive queries
- Use @RawQuery with SupportSQLiteQuery for complex queries

## Code Example

```kotlin
// WRONG: generic type not supported
@Query("SELECT * FROM items WHERE type = :type")
suspend fun <T> getByType(type: String): List<T>

// CORRECT: concrete type
@Query("SELECT * FROM items WHERE type = :type")
suspend fun getByType(type: String): List<Item>

// For polymorphic queries:
@Query("SELECT * FROM items")
fun getAllItems(): Flow<List<ItemEntity>>

// TypeConverter for generic container:
class StringListConverter {
    @TypeConverter
    fun fromList(list: List<String>): String = list.joinToString(",")
    @TypeConverter
    fun toList(value: String): List<String> = value.split(",")
}
```

# Room does not support generic DAO methods
# Use concrete entity types
# Use TypeConverters for complex types
