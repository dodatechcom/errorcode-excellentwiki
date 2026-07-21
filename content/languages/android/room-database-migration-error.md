---
title: "Room Migration Error"
description: "Fix Room database migration errors when upgrading schema versions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room database crashes on upgrade because migration is missing or incorrect

## Common Causes

- Migration path not defined for new schema version
- SQL in migration does not match new schema
- TypeConverter changed without migration
- Fallback to destructive migration not configured

## Fixes

- Add Migration(oldVersion, newVersion) with SQL statements
- Test migration with Room migration testing library
- Use autoMigration for simple schema changes
- Configure fallbackToDestructiveMigration as last resort

## Code Example

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE users ADD COLUMN email TEXT NOT NULL DEFAULT ''")
    }
}

Room.databaseBuilder(context, AppDatabase::class.java, "app-db")
    .addMigrations(MIGRATION_1_2)
    .build()
```

# Test migrations
@RunWith(AndroidJUnit4::class)
class MigrationTest {
    @Test
    fun migrate1To2() {
        val db = Helper.createDatabase(db, 1)
        Helper.runMigrationsAndValidate(db, "app-db", 2, MIGRATION_1_2)
    }
}
