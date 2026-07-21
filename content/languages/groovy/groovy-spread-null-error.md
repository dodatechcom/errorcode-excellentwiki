---
title: "Groovy Spread Operator Method Error"
description: "Fix Groovy spread operator (.*.) errors when calling methods on collection elements that may be null."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The spread operator `*.` calls a method on each element of a collection. If any element is null, the call throws a NullPointerException because `null.method()` fails.

## Common Causes

- Collection contains null elements
- Method does not exist on some elements (mixed-type collection)
- Spread on a non-collection type
- Using spread where collect with null check is needed
- Nested spread operators on deeply nested null values

## How to Fix

```groovy
// WRONG: Collection contains nulls
def items = ["hello", null, "world"]
def lengths = items*.length()  // NullPointerException on null

// CORRECT: Filter nulls first
def items = ["hello", null, "world"]
def lengths = items.findAll { it != null }*.length()
// [5, 5]
```

```groovy
// WRONG: Spread on non-collection
def name = "hello"
def upper = name*.toUpperCase()  // error: not a collection

// CORRECT: Use regular method call
def upper = name.toUpperCase()
```

## Examples

```groovy
// Example 1: Basic spread
def people = [
    [name: "Alice", age: 30],
    [name: "Bob", age: 25]
]
def names = people*.name  // ["Alice", "Bob"]

// Example 2: Nested spread
def companies = [
    [name: "Acme", employees: [[name: "X"], [name: "Y"]]],
    [name: "Globex", employees: [[name: "Z"]]]
]
def empNames = companies*.employees*.name  // [["X","Y"], ["Z"]]

// Example 3: Safe spread with null filtering
def data = [null, [val: 1], [val: null], [val: 3]]
def vals = data.findAll { it?.val != null }*.val  // [1, 3]
```

## Related Errors

- [Null pointer error](groovy-null-pointer) -- null reference issues
- [Spread operator error](groovy-spread-operator) -- spread syntax problems
