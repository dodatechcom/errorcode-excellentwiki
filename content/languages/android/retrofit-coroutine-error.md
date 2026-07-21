---
title: "Retrofit Coroutine Error"
description: "Fix Retrofit coroutine integration errors for suspend functions in API interfaces"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit suspend functions fail with coroutine-related errors

## Common Causes

- Suspend function not returning Response type
- Coroutine scope not properly structured
- Cancellation not propagating to Retrofit call
- Using callbacks with coroutines incorrectly

## Fixes

- Use suspend keyword on Retrofit interface methods
- Use viewModelScope for UI-triggered requests
- Retrofit handles cancellation automatically for suspend
- Replace Callback with suspend and try/catch

## Code Example

```kotlin
// CORRECT suspend interface
interface ApiService {
    @GET("users")
    suspend fun getUsers(): Response<List<User>>
}

// In ViewModel:
viewModelScope.launch {
    try {
        val response = apiService.getUsers()
        if (response.isSuccessful) {
            _uiState.value = UiState.Success(response.body()!!)
        } else {
            _uiState.value = UiState.Error(response.message())
        }
    } catch (e: IOException) {
        _uiState.value = UiState.Error("Network error")
    }
}
```

# Use Response<T> for status code access
# Use body directly if you trust 2xx responses
# Wrap in try/catch for network exceptions
