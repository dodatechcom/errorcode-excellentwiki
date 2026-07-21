---
title: "[Solution] Spring WebClient Timeout Error"
description: "Fix Spring WebClient timeout errors when HTTP requests take too long or connections are refused."
frameworks: ["spring"]
error-types: ["timeout-error"]
severities: ["error"]
---

WebClient timeout errors occur when HTTP requests exceed the configured timeout or the remote server is not responding.

## Common Causes

- Default timeout too short for external API
- Connection pool exhausted
- DNS resolution timeout
- Response body too large to download in time
- Network latency too high

## How to Fix

### Configure Timeouts

```java
@Configuration
public class WebClientConfig {
    @Bean
    public WebClient webClient() {
        HttpClient httpClient = HttpClient.create()
            .responseTimeout(Duration.ofSeconds(10))
            .option(ChannelOption.CONNECT_TIMEOUT_MILLIS, 5000)
            .doOnConnected(conn -> conn
                .addHandlerLast(new ReadTimeoutHandler(10, TimeUnit.SECONDS))
                .addHandlerLast(new WriteTimeoutHandler(10, TimeUnit.SECONDS))
            );

        return WebClient.builder()
            .clientConnector(new ReactorClientHttpConnector(httpClient))
            .defaultHeader("Accept", "application/json")
            .build();
    }
}
```

### Add Timeout to Individual Requests

```java
webClient.get()
    .uri("/api/data")
    .retrieve()
    .bodyToMono(Data.class)
    .timeout(Duration.ofSeconds(5))
    .retry(3)
    .subscribe();
```

### Handle Timeout Errors

```java
public Mono<Data> fetchData() {
    return webClient.get()
        .uri("/api/data")
        .retrieve()
        .bodyToMono(Data.class)
        .timeout(Duration.ofSeconds(5))
        .onErrorResume(TimeoutException.class, e -> {
            log.warn("Request timed out");
            return Mono.empty();
        });
}
```

## Examples

```java
// Bug -- no timeout
WebClient client = WebClient.create();
client.get()
    .uri("/slow-api")
    .retrieve()
    .bodyToMono(String.class)
    .subscribe();  // May hang forever

// Fix -- add timeout
client.get()
    .uri("/slow-api")
    .retrieve()
    .bodyToMono(String.class)
    .timeout(Duration.ofSeconds(10))
    .subscribe();
```
