---
title: "Retrofit URL Error"
description: "Fix Retrofit base URL and endpoint path configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit requests fail with 404 or wrong URL because of path configuration

## Common Causes

- Base URL does not end with /
- Endpoint path starts with / instead of relative path
- URL path segment encoded incorrectly
- Base URL changed but old URL cached

## Fixes

- Ensure base URL ends with trailing slash
- Use relative paths in @GET annotations
- Use @Path for dynamic URL segments
- Clear OkHttp cache after URL changes

## Code Example

```kotlin
// WRONG:
val retrofit = Retrofit.Builder()
    .baseUrl("https://api.example.com")  // Missing /
    .build()

// CORRECT:
val retrofit = Retrofit.Builder()
    .baseUrl("https://api.example.com/")  // Trailing /
    .build()

interface ApiService {
    @GET("users/list")  // Relative path
    suspend fun getUsers(): List<User>

    @GET("users/{id}")  // Dynamic path
    suspend fun getUser(@Path("id") userId: Long): User
}
```

# @Path replaces {id} in URL
# @Query adds ?key=value parameters
# @Url allows full custom URL per request
