---
title: "[Solution] RestClientResponseException — RestTemplate Error Fix"
description: "Fix RestClientResponseException when RestTemplate receives HTTP error responses. Handle 4xx and 5xx status codes properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring", "rest-template", "http-client", "rest-api", "restclient-response"]
weight: 5
---

# RestClientResponseException — RestTemplate Error Fix

A `RestClientResponseException` is thrown when `RestTemplate` receives an HTTP response with a 4xx or 5xx status code. It includes the status code, response body, and headers.

## What This Error Means

Common message:

- `401 Unauthorized`
- `500 Internal Server Error`

## Common Causes

```java
// Cause 1: No error handler configured
RestTemplate restTemplate = new RestTemplate();
ResponseEntity<String> response = restTemplate.getForEntity(
    "https://api.example.com/data", String.class);
// Throws RestClientResponseException on 4xx/5xx

// Cause 2: Authentication missing
restTemplate.getForObject("https://api.example.com/protected", String.class);
```

## How to Fix

### Fix 1: Use error handler

```java
RestTemplate restTemplate = new RestTemplate();
restTemplate.setErrorHandler(new DefaultResponseErrorHandler() {
    @Override
    public void handleError(ClientHttpResponse response) throws IOException {
        if (response.getStatusCode().is5xxServerError()) {
            // Handle server error
        } else if (response.getStatusCode().is4xxClientError()) {
            // Handle client error
        }
    }
});
```

### Fix 2: Use exchange for full control

```java
RestTemplate restTemplate = new RestTemplate();
ResponseEntity<String> response = restTemplate.exchange(
    "https://api.example.com/data",
    HttpMethod.GET,
    null,
    String.class
);

if (response.getStatusCode().is2xxSuccessful()) {
    // Process response
} else {
    // Handle error
}
```

## Related Errors

- {{< relref "webclient" >}} — WebClientResponseException
- {{< relref "resttemplate-timeout" >}} — ResourceAccessException timeout
- {{< relref "webclient-timeout" >}} — WebClientRequestException timeout
