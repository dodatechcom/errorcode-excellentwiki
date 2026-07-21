---
title: "Retrofit Annotation Error"
description: "Fix Retrofit API interface annotation errors for HTTP method declarations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit service interface methods fail because of incorrect annotations

## Common Causes

- Missing @GET, @POST, @PUT, or @DELETE annotation
- URL path does not match server endpoint
- @Body used with GET request
- Wrong Content-Type for @FormUrlEncoded

## Fixes

- Add correct HTTP method annotation to every interface method
- Verify URL path matches server API documentation
- Use @Query or @Field for GET parameters, @Body for JSON
- Add @FormUrlEncoded with @Field for form data

## Code Example

```kotlin
interface ApiService {
    // Correct GET with query parameter
    @GET("users")
    suspend fun getUsers(@Query("page") page: Int): List<User>

    // Correct POST with JSON body
    @POST("users")
    suspend fun createUser(@Body user: CreateUserRequest): User

    // Correct POST with form data
    @FormUrlEncoded
    @POST("login")
    suspend fun login(
        @Field("email") email: String,
        @Field("password") password: String
    ): LoginResponse
}
```

# Common annotations:
# @GET, @POST, @PUT, @PATCH, @DELETE, @HEAD, @OPTIONS
# @Query, @Field, @Body, @Path, @Header, @Headers
# @FormUrlEncoded, @Multipart, @Streaming
