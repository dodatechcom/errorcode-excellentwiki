---
title: "ClassCastException in Groovy"
description: "A ClassCastException occurs when an object is cast to a type it is not compatible with."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cast", "ClassCastException", "type", "groovy"]
weight: 5
---

## What This Error Means

A `ClassCastException` is thrown when Groovy attempts to cast an object to a class that it is not an instance of.

## Common Causes

- Casting an object to an incompatible type
- Returning wrong type from a method
- Type coercion failure between incompatible types

## How to Fix

```groovy
// WRONG: Invalid cast
def list = [1, 2, 3]
def str = list as String   // ClassCastException

// CORRECT: Use appropriate conversion
def str = list.join(", ")   // "1, 2, 3"
```

```groovy
// WRONG: Casting non-numeric string
Integer x = "hello" as Integer   // ClassCastException

// CORRECT: Validate before casting
def s = "42"
if (s.isNumber()) {
    Integer x = s as Integer
}
```

## Examples

```groovy
Integer x = "hello" as Integer   // ClassCastException
def map = [a: 1, b: 2]
def list = map as List            // ClassCastException
```

## Related Errors

- [MissingMethodException](/languages/groovy/missing-method) - type mismatch
- [Type Mismatch in VBA](/languages/vba/type-mismatch) - similar type errors
