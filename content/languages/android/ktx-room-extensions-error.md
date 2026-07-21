---
title: "Room KTX Error"
description: "Fix Room KTX coroutine and Flow extension errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room KTX extensions do not provide expected coroutine or Flow support

## Common Causes

- Room KTX dependency not added
- DAO method not marked as suspend
- Flow not emitting from Room query
- Coroutines dispatcher not set for Room operations

## Fixes

- Add room-ktx dependency
- Mark DAO methods with suspend keyword
- Use Flow<List<T>> return type for reactive queries
- Room automatically uses background thread for suspend

## Code Example

```kotlin
dependencies {
    implementation "androidx.room:room-ktx:2.6.1"
    kapt "androidx.room:room-compiler:2.6.1"
}

@Dao
interface UserDao {
    // One-shot suspend query
    @Query("SELECT * FROM users WHERE id = :id")
    suspend fun getUserById(id: Long): User?

    // Reactive Flow query
    @Query("SELECT * FROM users ORDER BY name")
    fun getAllUsers(): Flow<List<User>>
}

// In ViewModel:
val users = userDao.getAllUsers()
    .catch { emit(emptyList()) }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())
```

# suspend: runs on background thread automatically
# Flow: emits updates on data changes
# stateIn: converts Flow to StateFlow for Compose
