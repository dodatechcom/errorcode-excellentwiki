---
title: "OkHttp Timeout Error"
description: "Fix OkHttp connection and read timeout errors in Android network requests"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
OkHttp requests fail with SocketTimeoutException or timeout errors

## Common Causes

- Default timeout too short for slow connections
- Server taking too long to respond
- Large file download exceeding timeout
- DNS resolution taking too long

## Fixes

- Increase connect, read, and write timeouts
- Use separate timeouts for downloads
- Configure DNS with shorter lookup timeout
- Implement retry logic with backoff

## Code Example

```kotlin
val client = OkHttpClient.Builder()
    .connectTimeout(30, TimeUnit.SECONDS)
    .readTimeout(60, TimeUnit.SECONDS)
    .writeTimeout(60, TimeUnit.SECONDS)
    .callTimeout(120, TimeUnit.SECONDS)  // Total request timeout
    .build()
```

# For large downloads, use Streaming:
@Streaming
@GET
suspend fun downloadFile(@Url url: String): ResponseBody

# Or set per-call timeout:
val request = Request.Builder()
    .url(url)
    .build()
client.newCall(request).execute()
