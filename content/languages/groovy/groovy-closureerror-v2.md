---
title: "[Solution] Groovy Closure Wrong Number of Arguments"
description: "Fix Groovy closure errors when calling closures with wrong argument count. Match closure signatures to call sites."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A closure error occurs when a Groovy closure is called with a different number of arguments than it expects. Groovy closures can accept variable arguments but must be defined appropriately.

## Common Causes

- Closure expects 1 argument but called with 0
- Closure expects 0 arguments but called with 1
- Method closure signature mismatch
- Using wrong closure call syntax

## How to Fix

```groovy
// WRONG: Closure expects 1 arg, called with 0
def greet = { name -> "Hello, $name" }
greet()  // Error: Expected 1 arg, got 0

// CORRECT: Use default or zero-arg closure
def greet = { name = "World" -> "Hello, $name" }
greet()  // "Hello, World"
```

```groovy
// WRONG: Closure expects 0 args, called with 1
def sayHello = { "Hello!" }
sayHello("Alice")  // Error: Expected 0 args, got 1

// CORRECT: Accept variable args
def sayHello = { name -> "Hello, ${name ?: 'World'}!" }
sayHello("Alice")  // "Hello, Alice!"
```

```groovy
// WRONG: forEach closure signature
[1, 2, 3].each { it, index ->  // Wrong signature for each
    println "$it at $index"
}

// CORRECT: each() only provides value, use eachWithIndex
[1, 2, 3].eachWithIndex { val, index ->
    println "$val at $index"
}
```

## Examples

```groovy
// Example 1: Variable argument closure
def process = { Object[] args ->
    args.each { println it }
}
process("hello", 42, [1,2,3])

// Example 2: Closure with optional param
def greet = { String name = "World" ->
    "Hello, $name!"
}
greet()         // "Hello, World!"
greet("Alice")  // "Hello, Alice!"

// Example 3: Method closure with correct arity
class Calculator {
    def add = { a, b -> a + b }
    def negate = { -it }
}

def calc = new Calculator()
println calc.add(2, 3)  // 5
println calc.negate(5)   // -5
```

## Related Errors

- [groovy-missingmethod]({{< relref "/languages/groovy/groovy-missingmethod" >}}) — missing method
- [groovy-missingproperty]({{< relref "/languages/groovy/groovy-missingproperty" >}}) — missing property
- [groovy-nullpointererror]({{< relref "/languages/groovy/groovy-nullpointererror" >}}) — null pointer
