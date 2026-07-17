---
title: "[Solution] MethodArgumentNotValidException — Spring Validation Fix"
description: "Fix MethodArgumentNotValidException when @Valid request body fails Bean Validation. Handle @RequestBody validation errors properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# MethodArgumentNotValidException — Spring Validation Fix

A `MethodArgumentNotValidException` is thrown when a `@Valid` or `@Validated` `@RequestBody` fails Bean Validation constraints. Spring wraps all validation errors into this exception.

## What This Error Means

The exception occurs at the controller layer when request body validation fails. Common message:

- `Validation failed for argument [0]: ... 3 errors: ...`

## Common Causes

```java
// Cause 1: Missing validation annotations
public class CreateUserRequest {
    private String name;  // No @NotBlank — always passes validation
    private String email; // No @Email — always passes validation
}

// Cause 2: Missing @Valid on @RequestBody
@PostMapping("/users")
public User create(@RequestBody CreateUserRequest request) { ... }
// Missing @Valid

// Cause 3: Group validation mismatch
public class CreateUserRequest {
    @NotBlank(groups = CreateGroup.class)
    private String name;
}
// Using default group but expecting CreateGroup
```

## How to Fix

### Fix 1: Add validation annotations to DTO

```java
public class CreateUserRequest {
    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100, message = "Name must be 2-100 characters")
    private String name;

    @NotBlank(message = "Email is required")
    @Email(message = "Email must be valid")
    private String email;
}
```

### Fix 2: Add @Valid to controller parameter

```java
@PostMapping("/users")
public User create(@Valid @RequestBody CreateUserRequest request) {
    return userService.create(request);
}
```

### Fix 3: Handle validation errors globally

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidationErrors(
            MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error ->
            errors.put(error.getField(), error.getDefaultMessage()));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

## Related Errors

- {{< relref "spring-bean" >}} — NoSuchBeanDefinitionException
- {{< relref "hibernate-validator" >}} — ConstraintViolationException
- {{< relref "jpa-constraint" >}} — ConstraintViolationException: Duplicate entry
