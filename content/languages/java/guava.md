---
title: "[Solution] Preconditions Failed — Google Guava Validation Fix"
description: "Fix Guava Preconditions check failures. Handle IllegalArgumentException, IllegalStateException, and NullPointerException."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Preconditions Failed — Google Guava Validation Fix

Guava `Preconditions` methods throw exceptions when preconditions fail. These are similar to assertions but are always active in production code.

## What This Error Means

Common exceptions:

- `checkArgument()` → `IllegalArgumentException`
- `checkState()` → `IllegalStateException`
- `checkNotNull()` → `NullPointerException`

## Common Causes

```java
import com.google.common.base.Preconditions;

// Cause 1: checkArgument failure
public void setAge(int age) {
    Preconditions.checkArgument(age > 0 && age < 150,
        "Age must be between 0 and 150, got: %s", age);
}

// Cause 2: checkState failure
public class Connection {
    private boolean connected = false;
    public void send(String data) {
        Preconditions.checkState(connected, "Connection must be established first");
    }
}

// Cause 3: checkNotNull failure
public void process(User user) {
    Preconditions.checkNotNull(user, "User must not be null");
}
```

## How to Fix

### Fix 1: Provide valid input

```java
service.setAge(25);  // Valid, not -1
```

### Fix 2: Initialize state before use

```java
Connection conn = new Connection();
conn.connect();  // Set state to true
conn.send("data");  // Works
```

### Fix 3: Handle precondition exceptions

```java
try {
    Preconditions.checkArgument(age > 0);
} catch (IllegalArgumentException e) {
    log.warn("Invalid age: {}", e.getMessage());
}
```

## Related Errors

- {{< relref "illegalargumentexception" >}} — General IllegalArgumentException
- {{< relref "illegalstateexception" >}} — General IllegalStateException
- {{< relref "nullpointerexception" >}} — General NullPointerException
