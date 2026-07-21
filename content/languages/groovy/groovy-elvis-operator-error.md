---
title: "Groovy Elvis Operator Null Pointer Error"
description: "Fix Groovy Elvis operator issues when the left operand returns null instead of a useful fallback value."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The Elvis operator `?:` returns the left operand if it is truthy (non-null, non-false), otherwise the right operand. Errors occur when both operands can be null or when the operator is used on a property that throws an exception.

## Common Causes

- Right operand of Elvis is also null, propagating null downstream
- Left operand evaluates to false or empty string (which Elvis treats as falsy)
- Elvis on a property access that throws MissingPropertyException
- Chained Elvis operators where null propagates through the chain
- Misunderstanding that Elvis treats empty string as falsy

## How to Fix

```groovy
// WRONG: Right operand is also null
def name = user?.profile?.name ?: null
// name is still null, downstream code may fail

// CORRECT: Provide meaningful default
def name = user?.profile?.name ?: "Unknown User"
```

```groovy
// WRONG: Empty string is falsy with Elvis
def input = ""
def result = input ?: "default"
// result is "default" even though input was set

// CORRECT: Use explicit null check if empty string is valid
def result = (input != null && input != "") ? input : "default"
```

## Examples

```groovy
// Example 1: Basic Elvis usage
def x = null
def y = x ?: 42  // y = 42

// Example 2: With method call
def config = getConfig()
def timeout = config?.timeout ?: 30

// Example 3: Chained Elvis
def host = config?.server?.host ?: config?.defaultHost ?: "localhost"
def port = config?.server?.port ?: 8080
```

## Related Errors

- [Null pointer error](groovy-null-pointer) -- null reference crashes
- [Safe navigation error](groovy-safe-navigation) -- null-safe operator issues
