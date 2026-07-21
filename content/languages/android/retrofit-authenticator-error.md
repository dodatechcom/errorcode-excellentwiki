---
title: "Retrofit Authenticator Error"
description: "Fix Retrofit Authenticator interface for automatic token refresh on 401"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit Authenticator does not refresh tokens correctly causing infinite loops

## Common Causes

- Authenticator called on every 401 causing loop
- Token refresh endpoint itself returning 401
- Authenticator not returning new Request
- Synchronized token refresh not implemented

## Fixes

- Add flag to prevent recursive 401 handling
- Verify refresh endpoint returns 200
- Return new Request with fresh token
- Use mutex for concurrent token refresh

## Code Example

```kotlin
class TokenAuthenticator(
    private val tokenProvider: () -> String
) : Authenticator {
    override fun authenticate(route: Route?, response: Response): Request? {
        // Prevent infinite loop on refresh failure
        if (response.code == 401 && response.request.header("Authorization")?.startsWith("Bearer") == true) {
            val newToken = tokenProvider()
            if (newToken.isNotEmpty()) {
                return response.request.newBuilder()
                    .header("Authorization", "Bearer $newToken")
                    .build()
            }
        }
        return null  // Return null to give up
    }
}

val client = OkHttpClient.Builder()
    .authenticator(TokenAuthenticator { getNewToken() })
    .build()
```

# Authenticator called on 401 response
# Return null to stop retry loop
# Check request already has auth header to prevent loop
