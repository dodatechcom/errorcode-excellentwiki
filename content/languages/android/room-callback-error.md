---
title: "Room Callback Error"
description: "Fix Room database callback and migration listener errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room database callbacks do not fire or fire at wrong time

## Common Causes

- RoomDatabase.Callback not registered
- onCreate not called after migration
- Callback running on main thread causing ANR
- Prepopulate data callback not working

## Fixes

- Register callback with addCallback on Room builder
- Use onOpen for post-migration work
- Move callback operations to background thread
- Use RoomDatabase.Callback with onCreate

## Code Example

```kotlin
val database = Room.databaseBuilder(context, AppDatabase::class.java, "app-db")
    .addCallback(object : RoomDatabase.Callback() {
        override fun onCreate(db: SupportSQLiteDatabase) {
            super.onCreate(db)
            // Prepopulate data
            CoroutineScope(Dispatchers.IO).launch {
                database.userDao().insertAll(prepopulatedUsers)
            }
        }

        override fun onOpen(db: SupportSQLiteDatabase) {
            super.onOpen(db)
            // Called every time database opens
        }
    })
    .build()
```

# onCreate: first database creation
# onOpen: every database open
# onDestructiveMigration: after destructive migration
