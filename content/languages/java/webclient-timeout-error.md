---
title: "[Solution] WebClient ReadTimeoutException Fix"
description: "Fix WebClient ReadTimeoutException. Configure timeouts, use connection pooling, and implement retry strategies for reactive HTTP clients."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# WebClient ReadTimeoutException Fix

A `ReadTimeoutException` is thrown when WebClient's HTTP request times out waiting for data from the server. This is common in reactive Spring WebFlux applications.

## What This Error Means

Common messages:

- `io.netty.handler.timeout.ReadTimeoutException: Read timed out`
- `reactor.netty.http.client.PrematureCloseException: Connection closed while receiving response`
- `WebClientRequestException: ReadTimeoutException`

Netty's underlying channel timed out waiting for the server to send response data. This typically indicates a slow upstream service or misconfigured timeout values.

## Common Causes

```java
// Cause 1: No timeout configured
WebClient client = WebClient.create("https://slow-api.example.com");
client.get()
    .retrieve()
    .bodyToMono(String.class)
    .block();  // May hang indefinitely

// Cause 2: Read timeout too short
HttpClient httpClient = HttpClient.create()
    .responseTimeout(Duration.ofSeconds(5));  // Too short

// Cause 3: Connection pool exhausted
// All connections in use, waiting for pool to free up

// Cause 4: Server streaming response is too slow
Flux<DataBuffer> stream = client.get()
    .retrieve()
    .bodyToFlux(DataBuffer.class);  // Server sends data slowly
```

## How to Fix

### Fix 1: Configure timeout on HttpClient

```java
HttpClient httpClient = HttpClient.create()
    .connectTimeout(Duration.ofSeconds(5))
    .responseTimeout(Duration.ofSeconds(30));

WebClient client = WebClient.builder()
    .clientConnector(new ReactorClientHttpConnector(httpClient))
    .baseUrl("https://api.example.com")
    .build();
```

### Fix 2: Set per-request timeout

```java
WebClient client = WebClient.create();

Mono<String> result = client.get()
    .uri("/slow-endpoint")
    .retrieve()
    .bodyToMono(String.class)
    .timeout(Duration.ofSeconds(30));
```

### Fix 3: Configure connection pool

```java
HttpClient httpClient = HttpClient.create()
    .connectionProvider(ConnectionProvider.builder("my-pool")
        .maxConnections(200)
        .maxIdleTime(Duration.ofSeconds(20))
        .maxLifeTime(Duration.ofSeconds(60))
        .pendingAcquireTimeout(Duration.ofSeconds(30))
        .build())
    .connectTimeout(Duration.ofSeconds(5))
    .responseTimeout(Duration.ofSeconds(30));

WebClient client = WebClient.builder()
    .clientConnector(new ReactorClientHttpConnector(httpClient))
    .build();
```

### Fix 4: Implement retry with backoff

```java
WebClient client = WebClient.create();

Mono<String> result = client.get()
    .uri("/endpoint")
    .retrieve()
    .bodyToMono(String.class)
    .timeout(Duration.ofSeconds(30))
    .retryWhen(Retry.backoff(3, Duration.ofSeconds(2))
        .filter(ex -> ex instanceof ReadTimeoutException));
```

### Fix 5: Use exchange strategies for large responses

```java
ExchangeStrategies strategies = ExchangeStrategies.builder()
    .codecs(cfg -> cfg.defaultCodecs().maxInMemorySize(16 * 1024 * 1024))
    .build();

WebClient client = WebClient.builder()
    .exchangeStrategies(strategies)
    .build();
```

## Related Errors

- {{< relref "webclient-timeout" >}} — WebClient general timeout error.
- {{< relref "resttemplate-timeout" >}} — RestTemplate timeout error.
