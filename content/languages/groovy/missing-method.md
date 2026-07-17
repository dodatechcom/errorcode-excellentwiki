---
title: "MissingMethodException: No signature of method"
description: "A MissingMethodException occurs when calling a method that does not exist on an object or class."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MissingMethodException` is thrown when Groovy cannot find a method matching the given name and argument types on the target object. Groovy resolves methods at runtime, so this error typically indicates a typo, wrong argument types, or missing imports.

## Common Causes

- Typo in method name
- Wrong number or types of arguments
- Method defined in a different class or module not imported
- Calling an instance method on a static context or vice versa

## How to Fix

```groovy
// WRONG: Typo in method name
def list = [1, 2, 3]
list.ad(4)              // MissingMethodException: No signature of method: add()

// CORRECT: Use correct method name
def list = [1, 2, 3]
list.add(4)
```

```groovy
// WRONG: Wrong argument types
def sb = new StringBuilder()
sb.append(123)          // works, but:
sb.append(true, true)   // MissingMethodException: wrong number of args

// CORRECT: Check method signature
def sb = new StringBuilder()
sb.append("hello")
```

## Examples

```groovy
// Example 1: Method doesn't exist on String
def s = "hello"
println s.toInteger()   // works (Groovy extension)
println s.toBigDecimal() // works
println s.nonExistent()  // MissingMethodException

// Example 2: Wrong arguments
class Calculator {
    int add(int a, int b) { a + b }
}
def calc = new Calculator()
calc.add(1)              // MissingMethodException: wrong number of args
calc.add("a", "b")      // MissingMethodException: wrong types

// Example 3: Static vs instance
class Foo {
    static void bar() { println "static" }
}
def foo = new Foo()
foo.bar()               // MissingMethodException (bar is static)
Foo.bar()               // works
```

## Related Errors

- [MissingPropertyException: No such property: X](/languages/groovy/missing-property)
