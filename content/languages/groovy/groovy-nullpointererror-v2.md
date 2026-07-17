---
title: "[Solution] Groovy NullPointerException"
description: "Fix Groovy NullPointerException when accessing members on null references. Use safe navigation and null checks."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["null", "pointer", "null-safe", "navigation", "groovy"]
weight: 5
---

## What This Error Means

A `NullPointerException` occurs when Groovy tries to access a method or property on a `null` reference. Groovy provides the safe navigation operator `?.` to handle this.

## Common Causes

- Accessing method on null object
- Dereferencing null variable
- Collection returning null elements
- Method returning null unexpectedly
- Missing initialization

## How to Fix

```groovy
// WRONG: Direct access on potentially null
def name = getNullableName()
println name.length()  // NullPointerException if null

// CORRECT: Use safe navigation
def name = getNullableName()
println name?.length()
```

```groovy
// WRONG: Chain of calls without null check
def city = person?.address?.city?.name  // May NPE at any point

// CORRECT: Safe navigation with defaults
def city = person?.address?.city?.name ?: "Unknown"
```

```groovy
// WRONG: Not handling null return
def result = service.getData()
println result.size()  // NPE if getData returns null

// CORRECT: Null check or Elvis operator
def result = service.getData() ?: []
println result.size()
```

## Examples

```groovy
// Example 1: Safe navigation operator
def person = null
println person?.name  // null, no exception

// Example 2: Elvis operator for defaults
def value = null
def result = value ?: "default"
println result  // "default"

// Example 3: Collect with null safety
def items = [1, null, 3, null, 5]
def cleaned = items.findAll { it != null }
println cleaned  // [1, 3, 5]

// Example 4: Null-safe collection operations
def list = null
def size = list?.size() ?: 0
```

## Related Errors

- [groovy-missingproperty]({{< relref "/languages/groovy/groovy-missingproperty" >}}) — missing property
- [groovy-missingmethod]({{< relref "/languages/groovy/groovy-missingmethod" >}}) — missing method
- [groovy-stringindex]({{< relref "/languages/groovy/groovy-stringindex" >}}) — string index
