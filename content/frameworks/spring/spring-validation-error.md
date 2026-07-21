---
title: "[Solution] Spring Bean Validation Error -- How to Fix"
description: "Fix Spring bean validation errors. Resolve @Valid, constraint violations, and custom validator issues."
frameworks: ["spring"]
error-types: ["validation-error"]
severities: ["warning"]
weight: 5
comments: true
---

A Spring bean validation error occurs when request data fails validation constraints defined with annotations like `@NotNull`, `@Size`, or `@Email`. Proper validation prevents invalid data from entering the system.

## Why It Happens

Spring uses Bean Validation (JSR 380) to validate request data. Errors occur when the `@Valid` annotation is missing on method parameters, when validation constraints are not properly defined, when custom validators have implementation errors, when the validation group is incorrect, or when `MethodArgumentNotValidException` is not handled.

## Common Error Messages

```
MethodArgumentNotValidException: Validation failed for argument: 0
```

```
ConstraintViolationException: Validation failed for method parameter
```

```
javax.validation.ConstraintViolationException: must not be blank
```

```
BindException: Failed to populate List<MyDto>: Argument '0' is null
```

## How to Fix It

### 1. Add Validation Annotations to DTOs

Define constraints on request objects:

```java
public class CreateUserRequest {

    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100, message = "Name must be 2-100 characters")
    private String name;

    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    private String email;

    @NotNull(message = "Age is required")
    @Min(value = 18, message = "Must be at least 18")
    @Max(value = 120, message = "Must be at most 120")
    private Integer age;

    @Size(min = 8, max = 128, message = "Password must be 8-128 characters")
    private String password;

    // Getters and setters
}
```

### 2. Use @Valid in Controllers

Trigger validation on request parameters:

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody CreateUserRequest request) {
        User user = userService.create(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }

    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(
            @PathVariable Long id,
            @Valid @RequestBody UpdateUserRequest request) {
        return ResponseEntity.ok(userService.update(id, request));
    }
}
```

### 3. Handle Validation Errors

Return meaningful error responses:

```java
@RestControllerAdvice
public class ValidationExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, Object>> handleValidationErrors(
            MethodArgumentNotValidException ex) {

        Map<String, String> fieldErrors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error ->
            fieldErrors.put(error.getField(), error.getDefaultMessage()));

        Map<String, Object> response = new HashMap<>();
        response.put("status", 400);
        response.put("error", "Validation Failed");
        response.put("fieldErrors", fieldErrors);

        return ResponseEntity.badRequest().body(response);
    }

    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<Map<String, Object>> handleConstraintViolations(
            ConstraintViolationException ex) {

        Map<String, String> errors = new HashMap<>();
        ex.getConstraintViolations().forEach(violation ->
            errors.put(
                violation.getPropertyPath().toString(),
                violation.getMessage()
            ));

        return ResponseEntity.badRequest().body(Map.of(
            "status", 400,
            "error", "Constraint Violation",
            "violations", errors
        ));
    }
}
```

### 4. Create Custom Validators

Implement custom validation logic:

```java
@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = UniqueEmailValidator.class)
public @interface UniqueEmail {
    String message() default "Email already exists";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

public class UniqueEmailValidator implements ConstraintValidator<UniqueEmail, String> {

    @Autowired
    private UserRepository userRepository;

    @Override
    public boolean isValid(String email, ConstraintValidatorContext context) {
        if (email == null) return true;
        return !userRepository.existsByEmail(email);
    }
}

// Usage
public class CreateUserRequest {
    @UniqueEmail
    private String email;
}
```

## Common Scenarios

**Scenario 1: Validation doesn't trigger.**
Check that `@Valid` is present on the `@RequestBody` parameter. Without it, Spring will not validate the request.

**Scenario 2: Validation error returns HTML instead of JSON.**
Add `@RestController` or `@ResponseBody` to the controller to ensure JSON responses.

**Scenario 3: Custom validation runs but result is ignored.**
Ensure the custom validator implements `ConstraintValidator` and the annotation is applied to the correct target (field, parameter, or type).

## Prevent It

1. **Always use `@Valid` with `@RequestBody`** to ensure validation runs before processing.

2. **Use validation groups** for different scenarios (create vs. update) where different constraints apply.

3. **Test validation in unit tests** with both valid and invalid data.
