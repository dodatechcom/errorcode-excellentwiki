---
title: "Room Reactive Query Error"
description: "Fix Room reactive query errors with Flow and LiveData observation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room reactive queries do not update when data changes in database

## Common Causes

- Query does not return Flow or LiveData
- InvalidateTracker not watching correct table
- Multiple queries not properly scoped
- Flow not collected with lifecycle awareness

## Fixes

- Return Flow<List<T>> or LiveData from Room query
- Room auto-invalidates on table changes
- Use collectAsStateWithLifecycle in Compose
- Configure invalidation tracker if needed

## Code Example

```kotlin
@Dao
interface UserDao {
    // This auto-updates when users table changes
    @Query("SELECT * FROM users WHERE active = 1")
    fun getActiveUsers(): Flow<List<User>>

    // This auto-updates when joined tables change
    @Query("SELECT * FROM users JOIN posts ON users.id = posts.authorId")
    fun getUsersWithPosts(): Flow<List<UserWithPosts>>
}

// In ViewModel:
val activeUsers = userDao.getActiveUsers()
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())

// In Compose:
val users by activeUsers.collectAsStateWithLifecycle()
```

# Room InvalidationTracker watches table changes
# Flow re-emits when table data changes
# Use WhileSubscribed(5000) for graceful cleanup
