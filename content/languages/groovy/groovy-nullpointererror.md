---
title: "NullPointerException in Groovy"
description: "A NullPointerException occurs when attempting to use a reference that points to no object (null)."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `NullPointerException` (NPE) is thrown when code tries to access a method or property on a null reference. Groovy's safe navigation operator `?.` can help prevent NPEs.

## Common Causes

- Method returning null when caller expects non-null
- Uninitialized variable passed to a method
- Collection element is null
- Method chaining without null checks

## How to Fix

```groovy
// WRONG: No null check
println name.toUpperCase()       // NPE if name is null

// CORRECT: Use safe navigation
println name?.toUpperCase()      // returns null instead of NPE
```

```groovy
// WRONG: Method chain without null checks
def city = getPerson().getAddress().getCity()

// CORRECT: Use safe navigation
def city = getPerson()?.getAddress()?.getCity()
```

## Examples

```groovy
def map = [a: 1, b: null]
println map.b + 1           // NPE

// CORRECT
println (map.b ?: 0) + 1    // 1

def items = ["a", null, "c"]
items.each { println it?.toUpperCase() }
```

## Related Errors

- [MissingPropertyException](/languages/groovy/missing-property) - property access issues
