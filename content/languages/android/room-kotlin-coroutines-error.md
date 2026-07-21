---
title: "Room Coroutines Error"
description: "Fix Room database coroutine integration errors for async database operations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room database operations fail when called from coroutines

## Common Causes

- Room query not marked as suspend
- Room DAO not using Flow return type
- Database operation on wrong dispatcher
- Room database not built with allowMainThreadQueries for testing only

## Fixes

- Add suspend keyword to DAO methods
- Use Flow<List<T>> for reactive queries
- Run Room operations on Dispatchers.IO
- Never use allowMainThreadQueries in production

## Code Example

```kotlin
@Dao
interface UserDao {
    // Suspend function for one-shot queries
    @Query("SELECT * FROM users WHERE id = :id")
    suspend fun getUserById(id: Long): User?

    // Flow for reactive queries
    @Query("SELECT * FROM users ORDER BY name")
    fun getAllUsers(): Flow<List<User>>

    // Transaction with coroutines
    @Transaction
    suspend fun replaceAll(users: List<User>) {
        deleteAll()
        insertAll(users)
    }

    @Query("DELETE FROM users")
    suspend fun deleteAll()

    @Insert
    suspend fun insertAll(users: List<User>)
}
```

# suspend: one-shot coroutine query
# Flow: reactive, auto-updates on data change
# Both run off main thread automatically
