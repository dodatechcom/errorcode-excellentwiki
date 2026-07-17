---
title: "[Solution] Room Migration Error Fix"
description: "Fix Room database migration errors when schema changes aren't handled."
languages: ["kotlin"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["room", "migration", "database", "schema", "kotlin"]
weight: 5
---

# Room: Migration Error Fix

A Room migration error occurs when the database schema changes without a proper migration path.

## What This Error Means

Room tracks database schema versions. When you modify entities and increment the version, Room needs a migration to alter the existing database. Missing migrations cause crashes.

## Common Causes

- Entity changed without migration
- Version number not incremented
- Migration SQL has errors
- Missing fallback strategy

## How to Fix

### 1. Add proper migrations

```kotlin
// CORRECT: Define migration
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE users ADD COLUMN email TEXT NOT NULL DEFAULT ''")
    }
}

database = Room.databaseBuilder(context, AppDatabase::class.java, "app.db")
    .addMigrations(MIGRATION_1_2)
    .build()
```

### 2. Auto-generate migrations

```bash
# CORRECT: Use Room auto-migration (Room 2.4+)
@Database(
    version = 2,
    entities = [User::class],
    autoMigrations = [
        AutoMigration(from = 1, to = 2)
    ]
)
```

### 3. Use destructive fallback for dev

```bash
# CORRECT: Fallback for development
database = Room.databaseBuilder(context, AppDatabase::class.java, "app.db")
    .fallbackToDestructiveMigration()
    .build()
```

### 4. Test migrations

```kotlin
// CORRECT: Test migration with Room testing
@RunWith(AndroidJUnit4::class)
class MigrationTest {
    @Test
    fun testMigration1To2() {
        val db = MigrationTestHelper.createDatabase(
            Room.databaseBuilder(context, AppDatabase::class.java, "test.db")
                .addMigrations(MIGRATION_1_2)
                .build()
        )
        // Verify data survived migration
    }
}
```

## Related Errors

- [Exposed Error](exposed-error-v2) — database errors
- [Room Error]({{< relref "/languages/kotlin/room-error" >}}) — general Room errors
- [Hilt Error](hilt-error-v2) — dependency injection
