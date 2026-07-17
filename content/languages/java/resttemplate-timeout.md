---
title: "[Solution] ResourceAccessException — RestTemplate Timeout Fix"
description: "Fix ResourceAccessException when RestTemplate connection or read times out. Configure timeouts for HTTP client."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ResourceAccessException — RestTemplate Timeout Fix

A `ResourceAccessException` is thrown when RestTemplate cannot establish a connection or the read times out. This is a wrapper around `java.net.SocketTimeoutException`.

## What This Error Means

Common message:

- `ResourceAccessException: I/O error on GET request for "url": Read timed out`

## Common Causes

```java
// Cause 1: Default timeout too low
RestTemplate restTemplate = new RestTemplate();
// Default timeout: 30 seconds

// Cause 2: Slow upstream service
restTemplate.getForObject("https://slow-api.example.com/data", String.class);

// Cause 3: Connection pool exhausted
// Too many concurrent requests
```

## How to Fix

### Fix 1: Configure timeouts with SimpleClientHttpRequestFactory

```java
SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
factory.setConnectTimeout(5000);  // 5 seconds
factory.setReadTimeout(10000);    // 10 seconds

RestTemplate restTemplate = new RestTemplate(factory);
```

### Fix 2: Configure Apache HttpClient

```java
HttpComponentsClientHttpRequestFactory factory =
    new HttpComponentsClientHttpRequestFactory();

CloseableHttpClient httpClient = HttpClients.custom()
    .setConnectionTimeToLive(30, TimeUnit.SECONDS)
    .setDefaultRequestConfig(RequestConfig.custom()
        .setConnectTimeout(5000)
        .setSocketTimeout(10000)
        .setConnectionRequestTimeout(3000)
        .build())
    .build();

factory.setHttpClient(httpClient);
RestTemplate restTemplate = new RestTemplate(factory);
```

## Related Errors

- {{< relref "webclient-timeout" >}} — WebClientRequestException timeout
- {{< relref "resttemplate" >}} — RestClientResponseException
- {{< relref "connection-timeout" >}} — Connection timeout
