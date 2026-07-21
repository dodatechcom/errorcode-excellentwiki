---
title: "Groovy Tuple Type Mismatch Error"
description: "Fix Groovy Tuple type mismatch errors when creating tuples with incompatible element types or destructuring incorrectly."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Groovy Tuples are typed by their size and element types. Type mismatch errors occur when assigning to typed tuples with wrong element types, or when using Tuple constructors with incompatible values.

## Common Causes

- Assigning wrong type to typed Tuple element
- Using Tuple constructor with too many or too few arguments
- Mixing typed and untyped Tuple usage
- Destructuring Tuple with wrong variable count
- Casting Tuple to incompatible Tuple type

## How to Fix

```groovy
// WRONG: Type mismatch in typed Tuple
def tuple = new Tuple3<String, Integer, Boolean>("Alice", "30", true)
// error: String cannot be assigned to Integer

// CORRECT: Match types exactly
def tuple = new Tuple3<String, Integer, Boolean>("Alice", 30, true)
```

```groovy
// WRONG: Destructuring Tuple with wrong count
def tuple = new Tuple3(1, 2, 3)
def (a, b) = tuple  // extra element ignored silently

// CORRECT: Match destructuring count
def tuple = new Tuple3(1, 2, 3)
def (a, b, c) = tuple
```

## Examples

```groovy
// Example 1: Create typed Tuple
def point = new Tuple2<Double, Double>(3.14, 2.71)
println "x=${point.first}, y=${point.second}"

// Example 2: Untyped Tuple
def data = new Tuple("hello", 42, true)
println data[0]  // "hello"
println data[1]  // 42

// Example 3: Tuple as Map value
def records = [
    new Tuple("Alice", 30),
    new Tuple("Bob", 25)
]
records.each { name, age ->
    println "$name is $age"
}
```

## Related Errors

- [Type mismatch error](groovy-type-mismatch) -- general type incompatibility
- [Cast error](groovy-casterror) -- explicit casting problems
