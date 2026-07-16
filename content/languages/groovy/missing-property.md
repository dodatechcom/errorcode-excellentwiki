---
title: "MissingPropertyException: No such property"
description: "A MissingPropertyException occurs when accessing a property that doesn't exist on an object."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["property", "missing", "attribute", "groovy"]
weight: 5
---

## What This Error Means

A `MissingPropertyException` is thrown when you try to access a property or field on an object that doesn't exist. Groovy resolves properties at runtime, so typos or missing fields result in this error.

## Common Causes

- Typo in property name
- Property not defined in class
- Accessing private property without getter
- Missing import or initialization

## How to Fix

```groovy
// WRONG: Typo in property name
class Person {
    String name
}
def p = new Person(name: "Alice")
println p.nme  // MissingPropertyException: No such property: nme

// CORRECT: Use correct property name
println p.name  // "Alice"
```

```groovy
// WRONG: Accessing non-existent property
def map = [a: 1, b: 2]
println map.c  // MissingPropertyException (if not using @CompileStatic)

// CORRECT: Use get or containsKey
println map.get("c", "default")
```

## Examples

```groovy
// Example 1: Missing field
class Config {
    String host = "localhost"
}
def c = new Config()
println c.port  // MissingPropertyException

// Example 2: Typo in map access
def settings = [debug: true, verbose: false]
println settigns.debug  // MissingPropertyException

// Example 3: Dynamic property
class Dynamic {
    def methodMissing(String name, args) {
        "handled"
    }
}
def d = new Dynamic()
println d.dynamicProp  // MissingPropertyException
```

## Related Errors

- [MissingMethodException: No signature of method](/languages/groovy/missing-method)
