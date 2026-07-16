---
title: "Closure error"
description: "A Closure error occurs when calling a closure with wrong arguments or when the closure throws an exception."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["closure", "call", "arguments", "groovy"]
weight: 5
---

## What This Error Means

A Closure error occurs when a closure is called with incorrect arguments, when the closure itself throws an exception, or when there's a mismatch between the expected and actual closure signature.

## Common Causes

- Wrong number of arguments passed to closure
- Closure accessing undeclared variables
- Closure throwing an exception
- Missing return statement

## How to Fix

```groovy
// WRONG: Wrong number of arguments
def add = { a, b -> a + b }
add(1)  // closure expects 2 arguments

// CORRECT: Provide correct arguments
def add = { a, b -> a + b }
add(1, 2)  // 3
```

```groovy
// WRONG: Closure with undeclared variable
def process = { it.value }  // 'it' is implicit
process()  // no argument provided

// CORRECT: Define parameters explicitly
def process = { item -> item.value }
process([value: 42])
```

## Examples

```groovy
// Example 1: Wrong arity
def greet = { name -> println "Hello, $name" }
greet()  // MissingMethodException (wrong number of args)

// Example 2: Exception inside closure
def risky = { throw new RuntimeException("oops") }
risky()  // RuntimeException

// Example 3: Closure returning null
def find = { list -> list.find { it > 10 } }
def result = find([1, 2, 3])  // result is null, may cause NPE later
```

## Related Errors

- [NullPointerException](/languages/groovy/null-pointer5)
- [MissingMethodException: No signature of method](/languages/groovy/missing-method)
