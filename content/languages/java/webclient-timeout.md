---
title: "[Solution] WebClientRequestException — WebClient Timeout Fix"
description: "Fix WebClientRequestException when WebClient connection or read times out. Configure timeouts and resilience."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring", "webclient", "reactive", "timeout", "webclient-request"]
weight: 5
---

# WebClientRequestException — WebClient Timeout Fix

A `WebClientRequestException` is thrown when WebClient cannot establish a connection or the read times out. It wraps `java.net.ConnectException` and `java.net.SocketTimeoutException`.

## What This Error Means

Common message:

- `WebClientRequestException: Connection refused`
- `WebClientRequestException: Read timed out`

## Common Causes

```java
// Cause 1: No timeout configured
webClient.get()
    .uri("https://slow-api.example.com/data")
    .retrieve()
    .bodyToMono(String.class)
    .subscribe();  // No timeout set

// Cause 2: Connection pool exhaustion
// Too many concurrent requests
```

## How to Fix

### Fix 1: Configure WebClient with timeouts

```java
HttpClient httpClient = HttpClient.create()
    .option(ChannelOption.CONNECT_TIMEOUT_MILLIS, 5000)
    .responseTimeout(Duration.ofSeconds(10))
    .doOnConnected(conn ->
        conn.addHandlerLast(new ReadTimeoutHandler(10, TimeUnit.SECONDS))
            .addHandlerLast(new WriteTimeoutHandler(10, TimeUnit.SECONDS)));

ReactClientHttpConnector connector = new ReactClientHttpConnector(httpClient);

WebClient webClient = WebClient.builder()
    .clientConnector(connector)
    .build();
```

### Fix 2: Add per-request timeout

```java
webClient.get()
    .uri("https://api.example.com/data")
    .retrieve()
    .bodyToMono(String.class)
    .timeout(Duration.ofSeconds(5))
    .subscribe();
```

### Fix 3: Add retry

```java
webClient.get()
    .uri("https://api.example.com/data")
    .retrieve()
    .bodyToMono(String.class)
    .retryWhen(Retry.backoff(3, Duration.ofSeconds(1))
        .filter(ex -> ex instanceof WebClientRequestException))
    .subscribe();
```

## Related Errors

- {{< relref "resttemplate-timeout" >}} — ResourceAccessException timeout
- {{< relref "webclient" >}} — WebClientResponseException
- {{< relref "resttemplate" >}} — RestClientResponseException
