---
title: "[Solution] Java IllegalArgumentException — Validate Method Parameters"
description: "Fix Java IllegalArgumentException by validating parameters at method entry, using @NonNull annotations, and checking preconditions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
date: 2026-07-15
---

# Java IllegalArgumentException

An `IllegalArgumentException` signals that a method has been passed an argument that is inappropriate or outside the expected range. It is an unchecked exception commonly thrown by library methods to enforce contracts, and it almost always indicates a bug in the calling code.

## Common Causes

```java
// Cause 1: Negative value where positive is expected
setAge(-5);  // throws IllegalArgumentException

// Cause 2: Null where non-null is required
processItem(null);  // throws IllegalArgumentException

// Cause 3: Value outside valid range
setPageNumber(-1);  // throws IllegalArgumentException

// Cause 4: Invalid enum or format
Color.valueOf("notacolor");  // throws IllegalArgumentException
```

## Solutions

### Fix 1: Validate parameters at the start of the method

```java
// Wrong — no validation, bad values propagate silently
public void setAge(int age) {
    this.age = age;
}

// Correct — fail fast with a descriptive message
public void setAge(int age) {
    if (age < 0 || age > 150) {
        throw new IllegalArgumentException(
            "Age must be between 0 and 150, got: " + age
        );
    }
    this.age = age;
}
```

### Fix 2: Use `Objects.requireNonNull()` for null checks

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

### Fix 3: Use `@NonNull` annotations with static analysis

```java
import org.jetbrains.annotations.NotNull;

public void sendEmail(@NotNull String recipient, @NotNull String subject) {
    // Static analysis tools (IntelliJ, SpotBugs) will flag
    // callers who pass null without runtime cost
    Objects.requireNonNull(recipient, "recipient must not be null");
    // ...
}
```

### Fix 4: Use Preconditions from Guava

```java
import com.google.common.base.Preconditions;

public void setPageSize(int size) {
    Preconditions.checkArgument(
        size > 0 && size <= 100,
        "Page size must be between 1 and 100, got: %s",
        size
    );
    this.pageSize = size;
}

// Usage
setPageSize(0);  // IllegalArgumentException: Page size must be between 1 and 100, got: 0
```

### Fix 5: Use custom exceptions for domain-specific validation

```java
public class InvalidOrderException extends IllegalArgumentException {
    public InvalidOrderException(String message) {
        super(message);
    }
}

public void placeOrder(Order order) {
    if (order.getItems().isEmpty()) {
        throw new InvalidOrderException("Order must contain at least one item");
    }
    if (order.getTotal() <= 0) {
        throw new InvalidOrderException("Order total must be positive");
    }
}
```

## Prevention Tips

- Adopt a "validate early, fail fast" pattern at every public method boundary
- Write unit tests that verify your validation logic rejects invalid inputs
- Use `Objects.requireNonNull()` consistently instead of letting nulls propagate
- Enable IDE inspections and SpotBugs to catch missing null checks

## Related Errors

- [NullPointerException](../nullpointerexception) — null reference access
- [UnsupportedOperationException](../unsupportedoperationexception) — operation not supported
- [NumberFormatException](../numberformatexception) — invalid string-to-number conversion
