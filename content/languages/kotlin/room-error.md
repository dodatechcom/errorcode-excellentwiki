---
title: "[Solution] Kotlin Room Database Error Fix"
description: "Fix Room database errors in Kotlin. Learn why Room operations fail and how to handle Android database issues."
languages: ["kotlin"]
severities: ["error"]
error-types: ["database-error"]
weight: 5
---

## What This Error Means

A Room database error occurs when Room ORM operations fail. This can happen due to schema issues, query errors, or migration problems.

## Common Causes

- Missing @Database annotation
- Query syntax errors
- Missing migration
- Entity not properly defined

## How to Fix

```kotlin
// WRONG: Missing annotations
class UserDao {
    fun getAll(): List<User> = // ...
}

// CORRECT: Add Room annotations
@Dao
interface UserDao {
    @Query("SELECT * FROM users")
    fun getAll(): List<User>
}
```

```kotlin
// WRONG: Schema changed without migration
// Version 1 -> 2: Added email column
// No migration defined

// CORRECT: Add migration
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE users ADD COLUMN email TEXT")
    }
}
```

## Examples

```kotlin
// Example 1: Entity
@Entity(tableName = "users")
data class User(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    @ColumnInfo(name = "name") val name: String,
    @ColumnInfo(name = "email") val email: String
)

// Example 2: DAO
@Dao
interface UserDao {
    @Query("SELECT * FROM users")
    fun getAll(): Flow<List<User>>

    @Insert
    suspend fun insert(user: User)

    @Delete
    suspend fun delete(user: User)
}

// Example 3: Database
@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

## Related Errors

- [CoreData persistence error](coredata-error) — CoreData error
- [Exposed ORM error](exposed-error) — Exposed error
- [Realm database error](realm-error-swift) — Realm error
