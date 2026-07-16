---
title: "HttpClientErrorException"
description: "Spring RestTemplate or WebClient throws when the upstream API returns a 4xx HTTP status code"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["http", "rest-client", "4xx", "webclient", "resttemplate"]
weight: 5
---

This error occurs when Spring's `RestTemplate` or `WebClient` receives a 4xx response from an external API. The default behavior is to throw an exception instead of returning the response.

## Common Causes

- External API returned 400 Bad Request (invalid input)
- Authentication failed (401 Unauthorized)
- Insufficient permissions (403 Forbidden)
- Resource not found (404 Not Found)

## How to Fix

1. Handle 4xx responses with error handling:

```java
try {
    ResponseEntity<User> response = restTemplate.exchange(
        "https://api.example.com/users/{id}",
        HttpMethod.GET,
        null,
        User.class,
        userId
    );
    return response.getBody();
} catch (HttpClientErrorException e) {
    if (e.getStatusCode() == HttpStatus.NOT_FOUND) {
        throw new ResourceNotFoundException("User not found");
    }
    throw e;
}
```

2. Use `RestTemplate` with custom error handler:

```java
restTemplate.setErrorHandler(new ResponseErrorHandler() {
    @Override
    public boolean hasError(ClientHttpResponse response) throws IOException {
        return response.getStatusCode().is4xxClientError();
    }

    @Override
    public void handleError(ClientHttpResponse response) throws IOException {
        // Custom error handling logic
    }
});
```

3. Use `WebClient` for non-blocking requests with error handling:

```java
webClient.get()
    .uri("/users/{id}", userId)
    .retrieve()
    .onStatus(HttpStatusCode::is4xxClientError, response -> {
        return response.bodyToMono(String.class)
            .flatMap(body -> Mono.error(new ResourceNotFoundException(body)));
    })
    .bodyToMono(User.class);
```

## Examples

```java
// 404 from external API
try {
    restTemplate.getForObject("https://api.example.com/users/999", User.class);
} catch (HttpClientErrorException.NotFound e) {
    System.out.println("User not found: " + e.getResponseBodyAsString());
}
```

```text
HttpClientErrorException$NotFound: 404 Not Found: {"error": "User not found"}
```

## Related Errors

- [Transaction error]({{< relref "/frameworks/spring/transaction-error" >}})
