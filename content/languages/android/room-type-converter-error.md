---
title: "Room TypeConverter Error"
description: "Fix Room TypeConverter errors when storing custom types in database"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room fails to compile because it cannot convert a field type to/from database storage

## Common Causes

- Custom class not convertible to storable type
- TypeConverter not registered with @TypeConverters
- Converter methods not static or companion object methods
- Null safety not handled in converter

## Fixes

- Create TypeConverter class with @TypeConverters annotation
- Register converters at Database or Entity level
- Ensure converter handles null values
- Convert custom types to primitives or strings

## Code Example

```kotlin
class DateConverter {
    @TypeConverter
    fun fromTimestamp(value: Long?): Date? = value?.let { Date(it) }

    @TypeConverter
    fun toTimestamp(date: Date?): Long? = date?.time
}

@Database(entities = [User::class], version = 1)
@TypeConverters(DateConverter::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

# Convert complex objects to JSON string:
@TypeConverter
fun fromList(value: List<String>): String = Gson().toJson(value)

@TypeConverter
fun toList(value: String): List<String> =
    Gson().fromJson(value, Array<String>::class.java).toList()
