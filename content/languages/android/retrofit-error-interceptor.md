---
title: "Retrofit Error Interceptor"
description: "Add Retrofit error interceptor for centralized HTTP error handling in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit does not handle HTTP errors properly, returning empty body on error

## Common Causes

- Retrofit returns successful response for 4xx/5xx
- Server error body not parsed into response
- Network interceptor not logging errors
- Error response not wrapped in Result class

## Fixes

- Throw exceptions in error interceptor for non-2xx responses
- Use Response<T>.errorBody() to parse error
- Add custom interceptor to handle common errors
- Wrap API calls in sealed Result class

## Code Example

```kotlin
class ErrorInterceptor : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val response = chain.proceed(chain.request())
        if (!response.isSuccessful) {
            val errorBody = response.body?.string()
            when (response.code) {
                401 -> throw UnauthorizedException(errorBody)
                404 -> throw NotFoundException(errorBody)
                500 -> throw ServerException(errorBody)
                else -> throw HttpException(response.code, errorBody)
            }
        }
        return response
    }
}
```

# Add interceptor to OkHttp client:
val client = OkHttpClient.Builder()
    .addInterceptor(ErrorInterceptor())
    .build()
