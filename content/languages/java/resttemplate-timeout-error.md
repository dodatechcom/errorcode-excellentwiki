---
title: "[Solution] RestTemplate ResourceAccessException Timeout Fix"
description: "Fix RestTemplate timeout errors. Configure connection and read timeouts, use connection pooling, and handle network failures."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# RestTemplate ResourceAccessException Timeout Fix

A `ResourceAccessException` wrapping a `SocketTimeoutException` is thrown when RestTemplate's HTTP request exceeds the configured timeout waiting for a response.

## What This Error Means

Common messages:

- `ResourceAccessException: I/O error on GET request for "/api/data": Read timed out`
- `SocketTimeoutException: Read timed out`
- `SocketTimeoutException: Connect timed out`
- `ResourceAccessException: Timeout on GET request`

The HTTP client underlying RestTemplate timed out waiting to connect to the server or receive a response. This indicates network latency, server overload, or missing timeout configuration.

## Common Causes

```java
// Cause 1: No timeout configured (uses OS defaults — very long)
RestTemplate restTemplate = new RestTemplate();
restTemplate.getForObject("https://slow-api.example.com/data", String.class);
// May hang for minutes

// Cause 2: Connect timeout too short
HttpComponentsClientHttpRequestFactory factory =
    new HttpComponentsClientHttpRequestFactory();
factory.setConnectTimeout(500);  // 500ms — too aggressive
RestTemplate restTemplate = new RestTemplate(factory);

// Cause 3: Read timeout too short for large response
factory.setReadTimeout(1000);  // 1 second — too short for large payload

// Cause 4: Connection pool exhausted
// All connections checked out, new request waits
```

## How to Fix

### Fix 1: Configure timeouts explicitly

```java
HttpComponentsClientHttpRequestFactory factory =
    new HttpComponentsClientHttpRequestFactory();
factory.setConnectTimeout(5000);   // 5 seconds to connect
factory.setReadTimeout(30000);     // 30 seconds to read response

RestTemplate restTemplate = new RestTemplate(factory);
```

### Fix 2: Use Apache HttpClient with fine-grained control

```java
HttpClient httpClient = HttpClientBuilder.create()
    .setConnectionTimeToLive(60, TimeUnit.SECONDS)
    .setMaxConnTotal(20)
    .setMaxConnPerRoute(10)
    .setDefaultRequestConfig(RequestConfig.custom()
        .setConnectTimeout(5000)
        .setSocketTimeout(30000)
        .setConnectionRequestTimeout(3000)
        .build())
    .build();

HttpComponentsClientHttpRequestFactory factory =
    new HttpComponentsClientHttpRequestFactory(httpClient);
RestTemplate restTemplate = new RestTemplate(factory);
```

### Fix 3: Handle timeouts with error handling

```java
try {
    String response = restTemplate.getForObject("https://api.example.com/data", String.class);
} catch (ResourceAccessException e) {
    if (e.getCause() instanceof SocketTimeoutException) {
        log.error("Request timed out: {}", e.getMessage());
    }
    throw e;
}
```

### Fix 4: Use retry with RestTemplate

```java
RetryTemplate retryTemplate = new RetryTemplate();
retryTemplate.setRetryPolicy(new SimpleRetryPolicy(3));

String result = retryTemplate.execute(context -> {
    return restTemplate.getForObject("https://api.example.com/data", String.class);
});
```

### Fix 5: Set timeouts per-request

```java
HttpComponentsClientHttpRequestFactory factory =
    new HttpComponentsClientHttpRequestFactory();

// Override per-request
Map<String, Object> params = new HashMap<>();
HttpComponentsClientHttpRequestFactory requestFactory =
    new HttpComponentsClientHttpRequestFactory();
requestFactory.setConnectTimeout(3000);
requestFactory.setReadTimeout(10000);

RestTemplate restTemplate = new RestTemplate(requestFactory);
```

## Related Errors

- {{< relref "resttemplate-timeout" >}} — RestTemplate general timeout error.
- {{< relref "webclient-timeout" >}} — WebClient timeout error.
