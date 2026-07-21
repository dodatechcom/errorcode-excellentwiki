---
title: "[Solution] Spring Web Request Handling Error -- How to Fix"
description: "Fix Spring web request errors. Resolve request mapping, controller, and HTTP handling issues in Spring."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring web request handling error occurs when controllers cannot process HTTP requests due to mapping conflicts, missing annotations, incorrect parameter binding, or response handling issues. These errors prevent clients from accessing API endpoints.

## Why It Happens

Spring MVC uses `@RequestMapping` and its variants to map HTTP requests to handler methods. Errors occur when multiple methods map to the same path, when `@RequestBody` or `@PathVariable` annotations are missing, when content negotiation fails, or when the response type doesn't match the client's expectations.

## Common Error Messages

```
NoSuchRequestHandlingMethodException: No handler found for GET /api/users
```

```
IllegalStateException: Multiple SLF4J bindings
```

```
HttpMediaTypeNotSupportedException: Content type 'text/plain' not supported
```

```
TypeMismatchException: Failed to convert value of type 'java.lang.String' to required type 'java.lang.Long'
```

## How to Fix It

### 1. Use Correct Request Mapping Annotations

Map routes with proper annotations:

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        return ResponseEntity.ok(userService.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        return userService.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody CreateUserRequest request) {
        User user = userService.create(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }

    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(
            @PathVariable Long id,
            @Valid @RequestBody UpdateUserRequest request) {
        return userService.update(id, request)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
```

### 2. Handle Request Parameters Correctly

Use appropriate annotations for different parameter types:

```java
@RestController
@RequestMapping("/api/search")
public class SearchController {

    @GetMapping
    public ResponseEntity<Page<User>> searchUsers(
            @RequestParam String query,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size,
            @RequestParam(defaultValue = "name") String sortBy) {
        return ResponseEntity.ok(userService.search(query, page, size, sortBy));
    }

    @GetMapping("/by-email/{email}")
    public ResponseEntity<User> findByEmail(
            @PathVariable @Email String email) {
        return userService.findByEmail(email)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
}
```

### 3. Handle Exceptions with @ControllerAdvice

Create a global exception handler:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(new ErrorResponse("NOT_FOUND", ex.getMessage()));
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getAllErrors().forEach(error ->
            errors.put(error.getField(), error.getDefaultMessage()));
        return ResponseEntity.badRequest()
            .body(new ErrorResponse("VALIDATION_ERROR", "Validation failed", errors));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGeneral(Exception ex) {
        log.error("Unexpected error: ", ex);
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(new ErrorResponse("INTERNAL_ERROR", "An unexpected error occurred"));
    }
}
```

### 4. Return Proper Response Entities

Use ResponseEntity for full control over HTTP responses:

```java
@GetMapping("/report")
public ResponseEntity<byte[]> downloadReport() {
    byte[] report = reportService.generateReport();
    return ResponseEntity.ok()
        .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=report.pdf")
        .contentType(MediaType.APPLICATION_PDF)
        .contentLength(report.length)
        .body(report);
}
```

## Common Scenarios

**Scenario 1: 404 for a valid endpoint.**
Check that the `@RequestMapping` path matches the request URL exactly, including leading slashes. Verify the controller is in a package scanned by `@SpringBootApplication`.

**Scenario 2: Content type mismatch error.**
Ensure the `Content-Type` header in the request matches what the controller expects. Use `consumes` and `produces` attributes to specify supported types.

**Scenario 3: @RequestBody returns null.**
Check that the JSON payload is valid and the `Content-Type` is `application/json`. Verify the request class has a no-arg constructor and proper getters/setters.

## Prevent It

1. **Use `@RestController` instead of `@Controller`** to automatically add `@ResponseBody` to all methods.

2. **Always use `@Valid` with `@RequestBody`** to trigger validation before processing.

3. **Test controllers with `MockMvc`** for fast, isolated testing without starting the full server.
