---
title: "Closure error in Groovy"
description: "Fix Groovy closure errors when closures fail to execute, have scoping issues, or throw exceptions."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["closure", "delegate", "scope", "groovy"]
weight: 5
---

## What This Error Means

Closures in Groovy are blocks of code that can be passed around and executed later. Errors occur due to scoping issues, delegate resolution, or incorrect parameter binding.

## Common Causes

- Variable not in closure's lexical scope
- Delegate method not found
- Closure called with wrong number of arguments
- `it` keyword ambiguity with multiple parameters

## How to Fix

```groovy
// WRONG: Variable not in scope
def closure = { println x }
closure()   // x not defined

// CORRECT: Define x before the closure
def x = 10
closure()
```

```groovy
// WRONG: Closure called with wrong args
def greet = { name -> println "Hello, ${name}" }
greet()   // wrong number of args

// CORRECT: Provide the argument
greet("Alice")
```

## Examples

```groovy
def items = [1, 2, 3]
def sum = 0
items.each { sum += it }
println sum   // 6

def fn = { a, b -> a + b }
fn(1)   // wrong number of arguments error
```

## Related Errors

- [MissingMethodException](/languages/groovy/missing-method) - method not found
- [MissingPropertyException](/languages/groovy/missing-property) - property not found
