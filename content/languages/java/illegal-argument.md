---
title: "[Solution] Java IllegalArgumentException — Null / Empty Argument Fix"
description: "Fix Java IllegalArgumentException for null and empty arguments. Validate parameters at method entry using Objects.requireNonNull, Preconditions, and @NonNull annotations."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalArgumentException — Null / Empty Argument

An `IllegalArgumentException` is thrown when a method receives an argument that is inappropriate for the method's contract — such as `null` when non-null is required, empty strings where content is expected, or values outside a valid range. It signals a bug in the calling code.

## Description

`IllegalArgumentException` is an unchecked exception that library and application methods use to enforce their contracts. The exception message should describe exactly what was wrong with the argument. Unlike `NullPointerException`, which signals a missing reference, `IllegalArgumentException` signals a present but invalid value.

Common variants:

- `IllegalArgumentException: argument must not be null`
- `IllegalArgumentException: Empty string is not allowed`
- `IllegalArgumentException: Page size must be between 1 and 100`

## Common Causes

```java
// Cause 1: Null where non-null is required
processItem(null);  // throws IllegalArgumentException

// Cause 2: Empty string where content is expected
validateEmail("");  // throws IllegalArgumentException

// Cause 3: Value outside valid range
setPageSize(-1);  // throws IllegalArgumentException

// Cause 4: Invalid enum value
Color.valueOf("notacolor");  // throws IllegalArgumentException

// Cause 5: Invalid regex pattern
String.matches("[invalid");  // throws IllegalArgumentException
```

## How to Fix

### Fix 1: Validate parameters at method entry

```java
// Wrong — no validation
public void setAge(int age) {
    this.age = age;
}

// Correct — fail fast with descriptive message
public void setAge(int age) {
    if (age < 0 || age > 150) {
        throw new IllegalArgumentException(
            "Age must be between 0 and 150, got: " + age
        );
    }
    this.age = age;
}
```

### Fix 2: Use Objects.requireNonNull for null checks

```java
import java.util.Objects;

// Wrong — NPE happens later, hard to trace
public void processItem(Item item) {
    item.validate();
}

// Correct — clear message at the point of entry
public void processItem(Item item) {
    Objects.requireNonNull(item, "item must not be null");
    item.validate();
}
```

### Fix 3: Use Guava Preconditions for concise validation

```java
import com.google.common.base.Preconditions;

public void setPageSize(int size) {
    Preconditions.checkArgument(
        size > 0 && size <= 100,
        "Page size must be between 1 and 100, got: %s", size
    );
    this.pageSize = size;
}
```

### Fix 4: Validate strings for empty/blank

```java
// Wrong — allows empty and blank strings
public void setEmail(String email) {
    this.email = email;
}

// Correct — validate content
public void setEmail(String email) {
    if (email == null || email.isBlank()) {
        throw new IllegalArgumentException("Email must not be null or empty");
    }
    if (!email.contains("@")) {
        throw new IllegalArgumentException("Invalid email format: " + email);
    }
    this.email = email;
}
```

### Fix 5: Use @NonNull annotations with static analysis

```java
import org.jetbrains.annotations.NotNull;

public void sendEmail(@NotNull String recipient, @NotNull String subject) {
    Objects.requireNonNull(recipient, "recipient must not be null");
    Objects.requireNonNull(subject, "subject must not be null");
    // Static analysis flags callers who pass null
}
```

## Examples

This error commonly occurs when:

- A public API method is called with null by external code
- Configuration values are missing from a properties file
- User input is passed directly to a method without validation
- A builder or factory method receives invalid parameters

## Related Errors

- [NullPointerException](nullpointerexception) — null reference access when validation is missing
- [UnsupportedOperationException](#) — operation not supported for the given argument
- [NumberFormatException](numberformat-error) — invalid string-to-number conversion
