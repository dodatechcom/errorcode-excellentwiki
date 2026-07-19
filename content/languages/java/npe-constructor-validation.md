---
title: "[Solution] Java NullPointerException"
description: "Missing Constructor Parameter Validation"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# constructors accepting parameters without null validation

A `constructors` is thrown when public userservice(userrepository repo) {.

## Common Causes

```java
public UserService(UserRepository repo) {
    this.repo = repo;  // no null check
}
```

## Solutions

```java
// Fix: Objects.requireNonNull
public UserService(UserRepository repo) {
    this.repo = Objects.requireNonNull(repo, "repo must not be null");
}

// Fix: @NonNull
@NonNull public UserService(@NonNull UserRepository repo) { this.repo = repo; }

// Fix: builder validation
public User build() {
    if (name == null) throw new IllegalStateException("name required");
    return new User(name, email);
}
```

## Prevention Checklist

- Always validate required constructor parameters.
- Use @NonNull annotations.
- Add validation in builder build().

## Related Errors

[NullPointerException](nullpointerexception), [IllegalArgumentException](illegalargumentexception)
