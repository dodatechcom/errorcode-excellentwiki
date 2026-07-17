---
title: "NullPointerException"
description: "A NullPointerException occurs when attempting to access a method or property on a null reference."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `NullPointerException` (NPE) is thrown when you try to call a method or access a property on a null object reference. This is one of the most common runtime errors in Groovy.

## Common Causes

- Forgetting to initialize a variable
- Method returning null unexpectedly
- Not checking for null before accessing properties
- Collection operations returning null

## How to Fix

```groovy
// WRONG: Not checking for null
def name = getUserName()
println name.toUpperCase()  // NullPointerException if null

// CORRECT: Use null-safe operator
def name = getUserName()
println name?.toUpperCase()
```

```groovy
// WRONG: Direct access on nullable
def list = getItems()
def first = list[0]  // NullPointerException if list is null

// CORRECT: Check before accessing
def list = getItems()
if (list) {
    def first = list[0]
}
```

## Examples

```groovy
// Example 1: Null variable
def x = null
println x.toString()  // NullPointerException

// Example 2: Null from method
def findUser(id) {
    // might return null
}
def user = findUser(999)
println user.name  // NullPointerException

// Example 3: Null in collection
def items = [1, null, 3]
items.each { it.length() }  // NullPointerException on null element
```

## Related Errors

- [MissingMethodException: No signature of method](/languages/groovy/missing-method)
- [MissingPropertyException: No such property](/languages/groovy/missing-property)
