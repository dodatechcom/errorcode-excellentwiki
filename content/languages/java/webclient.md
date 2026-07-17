---
title: "[Solution] WebClientResponseException — WebClient Error Fix"
description: "Fix WebClientResponseException when WebClient receives HTTP error responses. Handle reactive error responses properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# WebClientResponseException — WebClient Error Fix

A `WebClientResponseException` is thrown when WebClient receives an HTTP response with a 4xx or 5xx status code. It extends `HttpClientErrorException` or `HttpServerErrorException`.

## What This Error Means

Common messages:

- `401 Unauthorized`
- `502 Bad Gateway`

## Common Causes

```java
// Cause 1: No error handling in reactive chain
webClient.get()
    .uri("/api/data")
    .retrieve()
    .bodyToMono(String.class)
    .subscribe();  // Throws WebClientResponseException on error

// Cause 2: Missing error status handling
webClient.get()
    .uri("/api/data")
    .retrieve()
    .bodyToFlux(Data.class)
    .subscribe(data -> processData(data));
    // 4xx/5xx not handled
```

## How to Fix

### Fix 1: Use onStatus for error handling

```java
webClient.get()
    .uri("/api/data")
    .retrieve()
    .onStatus(HttpStatusCode::is4xxClientError, response ->
        response.bodyToMono(String.class)
            .map(body -> new ClientErrorException(response.statusCode(), body)))
    .onStatus(HttpStatusCode::is5xxServerError, response ->
        response.bodyToMono(String.class)
            .map(body -> new ServerErrorException(response.statusCode(), body)))
    .bodyToMono(String.class)
    .subscribe();
```

### Fix 2: Use exchange for full control

```java
webClient.get()
    .uri("/api/data")
    .exchangeToMono(response -> {
        if (response.statusCode().is2xxSuccessful()) {
            return response.bodyToMono(String.class);
        } else {
            return response.bodyToMono(String.class)
                .flatMap(body -> Mono.error(new CustomException(body)));
        }
    })
    .subscribe();
```

## Related Errors

- {{< relref "resttemplate" >}} — RestClientResponseException
- {{< relref "webclient-timeout" >}} — WebClientRequestException timeout
- {{< relref "resttemplate-timeout" >}} — ResourceAccessException timeout
