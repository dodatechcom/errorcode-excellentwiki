---
title: "[Solution] Groovy ClassCastException"
description: "Fix Groovy ClassCastException when runtime type casts fail. Use safe casting, instanceof checks, and type coercion."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `ClassCastException` occurs when Groovy tries to cast an object to a type it is not. This happens with explicit casts and when Groovy's dynamic typing resolves to wrong types.

## Common Causes

- Explicit cast with `as` to wrong type
- Returning wrong type from method
- Collection type mismatches
- Groovy auto-boxing issues
- Java interop type mismatches

## How to Fix

```groovy
// WRONG: Unsafe cast
def value = "hello"
def num = value as int  // ClassCastException or NumberFormatException

// CORRECT: Check type before casting
def value = "hello"
if (value instanceof Number) {
    def num = value as int
}
```

```groovy
// WRONG: Casting list element
def list = [1, 2, "three"]
def nums = list as List<Integer>  // ClassCastException on "three"

// CORRECT: Filter before casting
def list = [1, 2, "three"]
def nums = list.findAll { it instanceof Integer } as List<Integer>
```

```groovy
// WRONG: Wrong return type
def getData() {
    return "hello"  // Returns String
}
def num = getData() as int  // ClassCastException

// CORRECT: Use safe conversion
def num = getData()?.isNumber() ? getData() as int : 0
```

## Examples

```groovy
// Example 1: Safe casting with null check
def safeAsType(value, type) {
    try {
        return value?.asType(type)
    } catch (Exception e) {
        return null
    }
}

// Example 2: instanceof check
def process(value) {
    if (value instanceof String) {
        println "String: ${value}"
    } else if (value instanceof Number) {
        println "Number: ${value}"
    } else {
        println "Unknown type: ${value.class}"
    }
}

// Example 3: Groovy type coercion
def safeInt(value) {
    try {
        return value as Integer
    } catch (Exception e) {
        return 0
    }
}
```

## Related Errors

- [groovy-missingmethod]({{< relref "/languages/groovy/groovy-missingmethod" >}}) — missing method
- [groovy-nullpointererror]({{< relref "/languages/groovy/groovy-nullpointererror" >}}) — null pointer
- [groovy-stringindex]({{< relref "/languages/groovy/groovy-stringindex" >}}) — string index
