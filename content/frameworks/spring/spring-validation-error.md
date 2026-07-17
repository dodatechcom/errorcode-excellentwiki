---
title: "MethodArgumentNotValidException - validation failed"
description: "Spring throws MethodArgumentNotValidException when request body validation fails on @Valid parameters"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["validation", "request-body", "bean-validation", "hibernate-validator"]
weight: 5
---

This error occurs when a `@Valid` or `@Validated` request body fails Bean Validation constraints. Spring throws `MethodArgumentNotValidException` and returns a 400 Bad Request response.

## Common Causes

- Required fields are missing or null
- Field values violate `@Size`, `@Min`, `@Max`, `@Email` constraints
- Custom `@Valid` annotation rejects the input
- Nested object validation fails on `@Valid` field
- Request Content-Type header is incorrect

## How to Fix

1. Add validation annotations to DTOs:

```java
public record CreateUserRequest(
    @NotBlank @Size(max = 255) String name,
    @NotBlank @Email String email,
    @Min(18) @Max(120) int age
) {}
```

2. Use `@Valid` on controller parameters:

```PostMapping
public ResponseEntity<User> createUser(@Valid @RequestBody CreateUserRequest request) {
    return ResponseEntity.ok(userService.create(request));
}
```

3. Handle validation exceptions globally:

```java
@RestControllerAdvice
public class ValidationExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(
            MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error ->
            errors.put(error.getField(), error.getDefaultMessage())
        );
        return ResponseEntity.badRequest().body(errors);
    }
}
```

## Examples

```java
// Missing @Email causes validation failure
record LoginRequest(@NotBlank String email, @NotBlank String password) {}
// MethodArgumentNotValidException: must not be blank
```

## Related Errors

- [Access denied]({{< relref "/frameworks/spring/spring-security-error" >}})
- [WebFlux validation error]({{< relref "/frameworks/spring/webflux-error" >}})
