---
title: "ResourceAccessException - REST client timeout"
description: "Spring throws ResourceAccessException when a REST client request fails due to connection or timeout issues"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring's REST client (RestTemplate, WebClient, RestClient) encounters a connection failure or timeout while making an HTTP request. It throws `ResourceAccessException`.

## Common Causes

- Target service is unreachable or down
- Connection timeout configured too aggressively
- DNS resolution failure for the target host
- SSL/TLS handshake failure
- Network proxy blocking the connection

## How to Fix

1. Configure timeouts for RestTemplate:

```java
@Bean
public RestTemplate restTemplate() {
    SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
    factory.setConnectTimeout(Duration.ofSeconds(5));
    factory.setReadTimeout(Duration.ofSeconds(10));
    return new RestTemplate(factory);
}
```

2. Configure timeouts for WebClient:

```java
@Bean
public WebClient webClient() {
    HttpClient httpClient = HttpClient.create()
        .responseTimeout(Duration.ofSeconds(10))
        .option(ChannelOption.CONNECT_TIMEOUT_MILLIS, 5000);

    return WebClient.builder()
        .clientConnector(new ReactorClientHttpConnector(httpClient))
        .build();
}
```

3. Add retry logic for transient failures:

```java
@Service
public class ExternalApiService {

    private final WebClient webClient;

    public Mono<ExternalResponse> callExternalApi(String id) {
        return webClient.get()
            .uri("/api/external/{id}", id)
            .retrieve()
            .bodyToMono(ExternalResponse.class)
            .timeout(Duration.ofSeconds(5))
            .retryWhen(Retry.backoff(3, Duration.ofSeconds(1))
                .filter(throwable -> throwable instanceof ResourceAccessException));
    }
}
```

## Examples

```java
restTemplate.getForObject("http://down-service/api/data", String.class);
// ResourceAccessException: I/O error on GET http://down-service/api/data
```

## Related Errors

- [Gateway error]({{< relref "/frameworks/spring/spring-cloud-gateway-error" >}})
- [Retry error]({{< relref "/frameworks/spring/spring-retry-error" >}})
