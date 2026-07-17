---
title: "[Solution] WebExchangeBindException — WebFlux Validation Fix"
description: "Fix WebExchangeBindException when reactive request validation fails. Handle @Valid in WebFlux controllers properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# WebExchangeBindException — WebFlux Validation Fix

A `WebExchangeBindException` is thrown when `@Valid` or `@Validated` fails in a WebFlux controller. It is the reactive equivalent of `MethodArgumentNotValidException`.

## What This Error Means

Common message:

- `Validation failed for argument [0]: ... errors: ...`

## Common Causes

```java
// Cause 1: Missing validation annotations
public class CreateUserRequest {
    private String name;  // No @NotBlank
}

// Cause 2: @Valid missing on @RequestBody
@PostMapping("/users")
public Mono<User> create(@RequestBody CreateUserRequest request) {
    return userService.create(request);  // No @Valid
}
```

## How to Fix

### Fix 1: Add @Valid to WebFlux controller

```java
@PostMapping("/users")
public Mono<ResponseEntity<User>> create(
        @Valid @RequestBody Mono<CreateUserRequest> request) {
    return request.flatMap(req -> userService.create(req))
        .map(ResponseEntity::ok);
}
```

### Fix 2: Handle validation errors

```java
@ControllerAdvice
public class ValidationExceptionHandler {

    @ExceptionHandler(WebExchangeBindException.class)
    public Mono<ResponseEntity<Map<String, String>>> handleValidation(
            WebExchangeBindException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getFieldErrors().forEach(error ->
            errors.put(error.getField(), error.getDefaultMessage()));
        return Mono.just(ResponseEntity.badRequest().body(errors));
    }
}
```

### Fix 3: Add validation annotations to DTO

```java
public class CreateUserRequest {
    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100)
    private String name;

    @NotBlank(message = "Email is required")
    @Email(message = "Email must be valid")
    private String email;
}
```

## Related Errors

- {{< relref "spring-validation" >}} — MethodArgumentNotValidException
- {{< relref "webclient" >}} — WebClientResponseException
- {{< relref "webclient-timeout" >}} — WebClientRequestException timeout
