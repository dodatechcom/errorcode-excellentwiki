---
title: "[Solution] Java StackOverflowError — method calls itself without terminating base case"
description: "Fix Java StackOverflowError when method calls itself without terminating base case with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StackOverflowError — method calls itself without terminating base case

A `StackOverflowError` occurs when public int factorial(int n) {
    return n * factorial(n-1);  // no base case
}.

## Common Causes

```java
public int factorial(int n) {
    return n * factorial(n-1);  // no base case
}
```

## Solutions

```java
// Fix: add base case
public int factorial(int n) {
    if (n<=1) return 1;
    return n * factorial(n-1);
}

// Fix: iterate
public int factorial(int n) {
    int r = 1;
    for (int i=2; i<=n; i++) r *= i;
    return r;
}

// Fix: fix equals()
@Override
public boolean equals(Object obj) {
    if (this==obj) return true;
    if (!(obj instanceof Person o)) return false;
    return Objects.equals(this.name, o.name);
}
```

## Prevention Checklist

- Always define clear base case.
- Use iteration for simple loops.
- Test with large inputs.
- Use @Override correctly.

## Related Errors

OutOfMemoryError, StackOverflowError
