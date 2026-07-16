---
title: "Validation error"
description: "Spring throws ConstraintViolationException or MethodArgumentNotValidException when request validation fails"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["validation", "constraint", "bean-validation", "request"]
weight: 5
---

This error occurs when Spring's validation mechanism rejects a request because a bean, method parameter, or request body violates the defined constraints (e.g. `@NotNull`, `@Size`, `@Valid`).

## Common Causes

- Missing `@Valid` annotation on controller method parameter
- Request body fields do not meet `@NotNull`, `@Min`, `@Size` constraints
- Custom `ConstraintValidator` throws an exception
- Missing Hibernate Validator dependency

## How to Fix

1. Add `@Valid` annotation to request body parameters:

```java
@RestController
public class UserController {

    @PostMapping("/users")
    public ResponseEntity<User> createUser(@Valid @RequestBody UserDto userDto) {
        return ResponseEntity.ok(userService.create(userDto));
    }
}
```

2. Define validation constraints on DTOs:

```java
public class UserDto {
    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100)
    private String name;

    @Email(message = "Invalid email format")
    @NotBlank
    private String email;

    @Min(value = 18, message = "Age must be at least 18")
    private int age;
}
```

3. Handle validation errors with a global exception handler:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(err ->
            errors.put(err.getField(), err.getDefaultMessage())
        );
        return ResponseEntity.badRequest().body(errors);
    }
}
```

## Examples

```java
POST /users
Content-Type: application/json

{"name": "", "email": "invalid"}
```

```text
MethodArgumentNotValidException: Validation failed for argument [0] UserDto:
Name is required, Invalid email format
```

## Related Errors

- [DataSource connection error]({{< relref "/frameworks/spring/connection-refused5" >}})
