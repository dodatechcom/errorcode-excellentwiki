---
title: "Groovy Pipeline Operator Error Fix"
description: "Fix Groovy pipeline operator errors when chaining method calls with incorrect operator usage or type mismatches."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The pipeline operator `|>` passes the result of one expression as the first argument to the next function. Errors occur when function signatures don't match the piped value, or when pipeline chains have null intermediate results.

## Common Causes

- Pipeline function expects different argument type than provided
- Intermediate function returns null, breaking the chain
- Pipeline function has multiple required parameters
- Trying to pipeline with a method that needs `this` context
- Pipeline operator not supported in CompileStatic mode

## How to Fix

```groovy
// WRONG: Function expects different type
def toUpper = { String s -> s.toUpperCase() }
def result = 42 |> toUpper  // ClassCastException

// CORRECT: Ensure type compatibility
def toUpper = { String s -> s.toUpperCase() }
def result = "hello" |> toUpper  // "HELLO"
```

```groovy
// WRONG: Null breaks pipeline
def parse = { String s -> s?.toInteger() }
def result = null |> parse |> { it * 2 }  // NullPointerException

// CORRECT: Handle null in pipeline
def parse = { String s -> s?.toInteger() ?: 0 }
def result = null |> parse |> { it * 2 }  // 0
```

## Examples

```groovy
// Example 1: Basic pipeline
def add = { int a, int b -> a + b }
def result = 5 |> { add(it, 3) }  // 8

// Example 2: String processing pipeline
def result = "hello world"
    |> { it.capitalize() }
    |> { it.replace(" ", "_") }
    |> { it + "!" }
println result  // "Hello_World!"

// Example 3: Data processing pipeline
def process = { List nums ->
    nums.findAll { it > 0 }
        .collect { it * 2 }
        .sum()
}
def result = [-1, 2, -3, 4] |> process
println result  // 12
```

## Related Errors

- [Method not found error](groovy-missing-method) -- function signature mismatch
- [Null pointer error](groovy-null-pointer) -- null in pipeline chain
