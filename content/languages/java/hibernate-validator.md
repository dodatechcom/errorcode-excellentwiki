---
title: "[Solution] ConstraintViolationException — Hibernate Validator Fix"
description: "Fix ConstraintViolationException from Hibernate Validator. Handle method-level and bean validation constraints."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ConstraintViolationException — Hibernate Validator Fix

A `ConstraintViolationException` from Hibernate Validator is thrown when a method or bean validation constraint is violated. This differs from JPA constraint violations as it occurs at the validation layer, not the database.

## What This Error Means

Common message:

- `Validation failed for method: ... constraint violations: ...`

## Common Causes

```java
// Cause 1: Method validation failure
@Service
public class UserService {
    @Validated
    public User createUser(@NotBlank String name, @Email String email) {
        // Throws ConstraintViolationException if name is blank
    }
}

// Cause 2: Bean validation failure
public class User {
    @Size(min = 2, max = 50)
    private String name;
}
```

## How to Fix

### Fix 1: Handle ConstraintViolationException

```java
@ExceptionHandler(ConstraintViolationException.class)
public ResponseEntity<Map<String, String>> handleConstraintViolation(
        ConstraintViolationException ex) {
    Map<String, String> errors = new HashMap<>();
    ex.getConstraintViolations().forEach(violation ->
        errors.put(
            violation.getPropertyPath().toString(),
            violation.getMessage()));
    return ResponseEntity.badRequest().body(errors);
}
```

### Fix 2: Use custom constraint validators

```java
@Constraint(validatedBy = ValidEmailValidator.class)
@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
public @interface ValidEmail {
    String message() default "Invalid email";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

public class ValidEmailValidator implements ConstraintValidator<ValidEmail, String> {
    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
        return value != null && value.matches("^[A-Za-z0-9+_.-]+@(.+)$");
    }
}
```

### Fix 3: Enable method validation

```java
@Configuration
@EnableMethodValidation
public class ValidatorConfig { }
```

## Related Errors

- {{< relref "spring-validation" >}} — MethodArgumentNotValidException
- {{< relref "spring-webflux" >}} — WebExchangeBindException
- {{< relref "hibernate-mapping" >}} — MappingException
