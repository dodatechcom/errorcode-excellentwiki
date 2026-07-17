---
title: "WebExchangeBindException - WebFlux binding error"
description: "Spring WebFlux throws WebExchangeBindException when request body validation fails in reactive endpoints"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["webflux", "reactive", "validation", "request-body", "netty"]
weight: 5
---

This error occurs when a reactive controller parameter annotated with `@Valid` or `@Validated` fails Bean Validation in a WebFlux application. It throws `WebExchangeBindException`.

## Common Causes

- Request body violates validation constraints
- Missing or incorrect `Content-Type` header
- Malformed JSON in request body
- Nested validation failure on `@Valid` fields
- Custom validator throws an exception

## How to Fix

1. Add validation annotations to the DTO:

```java
public record CreateOrderRequest(
    @NotBlank String productId,
    @Positive int quantity,
    @Valid Address shippingAddress
) {}
```

2. Use `@Valid` on the reactive parameter:

```java
@PostMapping
public Mono<ResponseEntity<Order>> createOrder(
        @Valid @RequestBody Mono<CreateOrderRequest> request) {
    return request.flatMap(req -> orderService.create(req)
        .map(order -> ResponseEntity.status(201).body(order)));
}
```

3. Handle validation errors in a global exception handler:

```java
@RestControllerAdvice
public class ReactiveExceptionHandler {

    @ExceptionHandler(WebExchangeBindException.class)
    public Mono<ResponseEntity<Map<String, String>>> handleValidation(
            WebExchangeBindException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getFieldErrors().forEach(error ->
            errors.put(error.getField(), error.getDefaultMessage())
        );
        return Mono.just(ResponseEntity.badRequest().body(errors));
    }
}
```

## Examples

```java
// Missing required field triggers WebExchangeBindException
record LoginRequest(@NotBlank String email, @NotBlank String password) {}
// WebExchangeBindException: Field 'email' must not be blank
```

## Related Errors

- [Bean not found]({{< relref "/frameworks/spring/spring-bean-not-found" >}})
- [REST client error]({{< relref "/frameworks/spring/rest-client-error" >}})
