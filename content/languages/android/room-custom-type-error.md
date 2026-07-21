---
title: "Room Custom Type Error"
description: "Fix Room custom type adapter errors for complex object serialization"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room cannot persist custom type because adapter is missing or incorrect

## Common Causes

- TypeConverter registered but not applied to field
- Converter returns null for non-null type
- Complex nested type not handled by converter
- Converter using deprecated APIs

## Fixes

- Apply @TypeConverters at Entity or Database level
- Handle null values in converter methods
- Create composite converters for nested types
- Use modern TypeConverter API

## Code Example

```kotlin
class DateConverter {
    @TypeConverter
    fun toTimestamp(date: Date?): Long? = date?.time

    @TypeConverter
    fun fromTimestamp(value: Long?): Date? = value?.let { Date(it) }
}

class ListConverter {
    @TypeConverter
    fun fromList(list: List<String>): String = list.joinToString(",")

    @TypeConverter
    fun toList(value: String): List<String> =
        if (value.isBlank()) emptyList() else value.split(",")
}

@Database(entities = [User::class], version = 1)
@TypeConverters(DateConverter::class, ListConverter::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

# Register converters at Database level
# Or per-entity: @TypeConverters(Converters::class) on @Entity
# Convert complex types to primitives or strings
