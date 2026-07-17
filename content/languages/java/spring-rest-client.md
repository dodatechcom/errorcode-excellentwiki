---
title: "[Solution] ResourceAccessException Timeout — Spring REST Client Fix"
description: "Fix ResourceAccessException when Spring REST client times out. Configure timeouts and connection pooling."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring", "rest-client", "timeout", "http-client", "resource-access"]
weight: 5
---

# ResourceAccessException Timeout — Spring REST Client Fix

A `ResourceAccessException` is thrown when a Spring REST client (RestTemplate or WebClient) cannot complete a request due to connection or read timeout.

## What This Error Means

Common message:

- `ResourceAccessException: I/O error on GET request`

## Common Causes

```java
// Cause 1: No timeout configured
RestTemplate restTemplate = new RestTemplate();

// Cause 2: Default timeout too low for slow services

// Cause 3: Connection pool exhaustion
```

## How to Fix

### Fix 1: Configure RestTemplate timeouts

```java
@Bean
public RestTemplate restTemplate() {
    SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
    factory.setConnectTimeout(5000);
    factory.setReadTimeout(10000);
    return new RestTemplate(factory);
}
```

### Fix 2: Configure WebClient timeouts

```java
@Bean
public WebClient webClient() {
    HttpClient httpClient = HttpClient.create()
        .option(ChannelOption.CONNECT_TIMEOUT_MILLIS, 5000)
        .responseTimeout(Duration.ofSeconds(10));

    return WebClient.builder()
        .clientConnector(new ReactClientHttpConnector(httpClient))
        .build();
}
```

## Related Errors

- {{< relref "resttemplate-timeout" >}} — ResourceAccessException timeout
- {{< relref "webclient-timeout" >}} — WebClientRequestException timeout
- {{< relref "resttemplate" >}} — RestClientResponseException
