---
title: "Serialization error"
description: "Spring fails to serialize or deserialize JSON during HTTP communication or caching"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring (via Jackson) cannot serialize a Java object to JSON or deserialize JSON into a Java object. This commonly affects REST API responses and request body parsing.

## Common Causes

- Circular references between objects (e.g. bidirectional JPA relationships)
- Missing default constructor on a DTO class
- Jackson cannot serialize a field (e.g. `InputStream`, `Proxy`)
- JSON does not match the target class structure

## How to Fix

1. Break circular references with `@JsonIgnore` or `@JsonManagedReference`/`@JsonBackReference`:

```java
@Entity
public class User {
    @OneToMany(mappedBy = "user")
    @JsonManagedReference
    private List<Post> posts;
}

@Entity
public class Post {
    @ManyToOne
    @JsonBackReference
    private User user;
}
```

2. Ensure DTOs have a no-arg constructor:

```java
public class UserDto {
    private String name;
    private String email;

    // Required for Jackson deserialization
    public UserDto() {}

    public UserDto(String name, String email) {
        this.name = name;
        this.email = email;
    }
}
```

3. Handle `InvalidDefinitionException` globally:

```java
@RestControllerAdvice
public class JsonExceptionHandler {
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Map<String, String>> handleJsonError(HttpMessageNotReadableException ex) {
        return ResponseEntity.badRequest().body(Map.of("error", "Invalid JSON: " + ex.getMessage()));
    }
}
```

## Examples

```java
// Bidirectional JPA relationship causes infinite recursion
@Entity
public class Department {
    @OneToMany(mappedBy = "department")
    private List<Employee> employees; // Employee has Department reference
}

// Response: {"employees":[{"department":{"employees":[...
// Error: Infinite recursion (StackOverflow)
```

```text
com.fasterxml.jackson.databind.exc.InvalidDefinitionException:
No serializer found for class org.hibernate.proxy... and no properties discovered
```

## Related Errors

- [Profile not found]({{< relref "/frameworks/spring/profile-error" >}})
