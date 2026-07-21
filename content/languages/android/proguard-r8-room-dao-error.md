---
title: "Room DAO ProGuard Error"
description: "Fix ProGuard R8 errors with Room database DAO classes in release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room queries fail in release build because R8 removed DAO implementation classes

## Common Causes

- Room DAO interface obfuscated by R8
- TypeConverter classes removed
- Database entity fields renamed
- Room-generated implementation class stripped

## Fixes

- Keep all Room-related classes in proguard rules
- Keep TypeConverter classes explicitly
- Use @TypeConverters annotation
- Keep entity fields unchanged

## Code Example

```kotlin
# Room ProGuard rules
-keep class * extends androidx.room.RoomDatabase
-keep @androidx.room.Entity class *
-keep @androidx.room.Dao class *
-dontwarn androidx.room.paging.**

# TypeConverters
-keep class com.example.db.converters.** { *; }
-keepclassmembers class * {
    @androidx.room.* <fields>;
}
```

# Room automatically provides rules if using
# room-rxjava2 or room-ktx dependencies
# Check: implementation "androidx.room:room-runtime:2.6.1" 
