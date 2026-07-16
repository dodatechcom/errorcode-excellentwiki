---
title: "[Solution] Java AssertionError — Assertion Failure Fix"
description: "Fix Java AssertionError by enabling assertions, handling assertion flags properly, and using validation instead of assert for production code."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["assertionerror", "assert", "debugging", "precondition"]
weight: 5
---

# AssertionError — Assertion Failure Fix

An `AssertionError` is thrown when an `assert` statement evaluates to `false` at runtime. This is a subclass of `Error` and indicates that an internal invariant of the program has been violated. Assertions are disabled by default and must be explicitly enabled with the `-ea` JVM flag.

## Description

Assertions are used for debugging and development-time checks. They should never be used for argument validation in public APIs since they can be disabled at runtime. The error includes an optional detail message describing what went wrong.

## Common Causes

```java
// Cause 1: Assertion disabled in production but relied upon
assert list != null;  // throws AssertionError only if -ea is set
list.size();  // NullPointerException if assertions disabled

// Cause 2: Logic error in assertion condition
int value = computeValue();
assert value > 0 : "Value must be positive: " + value;

// Cause 3: Assertion in method that processes untrusted input
String input = getUserInput();
assert input.matches("\\d+") : "Expected numeric input";

// Cause 4: Assertion with side effects that affect program behavior
assert removeFromCache(key) != null : "Key not in cache";
```

## Solutions

```java
// Fix 1: Enable assertions when running the application
// java -ea -jar myapp.jar

// Fix 2: Use proper validation instead of assertions for public APIs
public void processInput(String input) {
    if (input == null) {
        throw new IllegalArgumentException("Input cannot be null");
    }
    if (!input.matches("\\d+")) {
        throw new IllegalArgumentException("Input must be numeric");
    }
}

// Fix 3: Use assertions for internal invariants only
public int divide(int a, int b) {
    assert b != 0 : "Division by zero";
    return a / b;
}

// Fix 4: Replace assertions with explicit checks
public void setAge(int age) {
    assert age >= 0 && age <= 150 : "Invalid age: " + age;
    // Better: use if-check for production
    if (age < 0 || age > 150) {
        throw new IllegalArgumentException("Invalid age: " + age);
    }
    this.age = age;
}
```

## Examples

```java
// This triggers AssertionError when assertions are enabled
public static void process(int[] data) {
    assert data != null : "Data array cannot be null";
    assert data.length > 0 : "Data array cannot be empty";
    // Processing logic
}

// Run with: java -ea MyApp
// AssertionError: Data array cannot be null
process(null);
```

## Related Exceptions

- [IllegalStateException]({{< relref "/languages/java/illegalstateexception" >}}) — object in wrong state for operation
- [IllegalArgumentException](../illegalargumentexception) — invalid method argument
- [NullPointerException](../nullpointerexception) — null reference access
