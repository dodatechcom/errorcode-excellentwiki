---
title: "Retrofit Flow Integration Error"
description: "Fix Retrofit and Kotlin Flow integration for streaming API responses"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit does not properly stream responses when used with Kotlin Flow

## Common Causes

- Response body not streamed correctly
- Flow collection cancelled mid-stream
- Streaming annotation missing on endpoint
- Connection not properly managed in long-running Flow

## Fixes

- Use @Streaming for large file downloads
- Collect Flow in lifecycle scope
- Use @Body with Flow for streaming upload
- Handle connection timeouts for long streams

## Code Example

```kotlin
// Streaming download
@Streaming
@GET("large-file.zip")
suspend fun downloadFile(@Url url: String): ResponseBody

// In ViewModel:
viewModelScope.launch {
    val responseBody = apiService.downloadFile(url)
    val inputStream = responseBody.byteStream()
    // Process stream...
}

// Flow-based API:
interface ApiService {
    @GET("events")
    fun getEventStream(): Flow<Event>
}
```

# @Streaming prevents loading entire response into memory
# Use for large files or streaming responses
# Handle connection cancellation gracefully
