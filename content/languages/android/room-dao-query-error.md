---
title: "Room DAO Query Error"
description: "Fix Room DAO query errors with SQL syntax and return types"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room DAO queries fail to compile because of SQL errors or wrong return type

## Common Causes

- SQL query has syntax error
- Return type does not match query result
- Missing @Query annotation on method
- Using LiveData or Flow return type without proper setup

## Fixes

- Verify SQL query syntax matches Room requirements
- Match return type to query columns
- Add @Query, @Insert, @Update, or @Delete annotation
- Add room-ktx dependency for Flow/LiveData support

## Code Example

```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM users WHERE id = :userId")
    suspend fun getUser(userId: Long): User?

    @Query("SELECT * FROM users WHERE orgId = :orgId ORDER BY name")
    fun getUsersByOrg(orgId: Long): Flow<List<User>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUser(user: User): Long

    @Update
    suspend fun updateUser(user: User)

    @Delete
    suspend fun deleteUser(user: User)
}
```

# SQL must use table name from @Entity
# Column names must match @Entity fields
# Use :paramName for query parameters
