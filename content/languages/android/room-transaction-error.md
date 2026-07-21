---
title: "Room Transaction Error"
description: "Fix Room database transaction errors and concurrency issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room transactions fail or produce inconsistent data due to concurrency issues

## Common Causes

- Multiple writes without transaction causing race condition
- Long-running transaction blocking main thread
- Nested transactions not supported
- Transaction not properly handling exceptions

## Fixes

- Use @Transaction annotation on methods performing multiple operations
- Run transactions on background thread with suspend
- Use @Transaction with suspend for coroutines
- Handle exceptions within transaction block

## Code Example

```kotlin
@Dao
interface UserDao {
    @Transaction
    suspend fun transferUsers(fromOrg: Long, toOrg: Long) {
        val users = getUsersByOrgOnce(fromOrg)
        users.forEach { user ->
            updateUser(user.copy(orgId = toOrg))
        }
    }

    @Query("SELECT * FROM users WHERE orgId = :orgId")
    suspend fun getUsersByOrgOnce(orgId: Long): List<User>
}
```

# Never run Room operations on main thread
# Use suspend functions with coroutines
# Use @Transaction for multi-step operations
