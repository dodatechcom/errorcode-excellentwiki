---
title: "MissingPropertyException: No such property"
description: "A MissingPropertyException occurs when Groovy cannot find a property on an object or in the current scope."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["property", "missing", "groovy", "scope"]
weight: 5
---

## What This Error Means

A `MissingPropertyException` is thrown when Groovy tries to access a property that doesn't exist on an object or in the current binding/scope.

## Common Causes

- Typo in property name
- Property not defined in the current scope
- Accessing a property on a wrong object type
- Closures not having access to outer scope variables

## How to Fix

```groovy
// WRONG: Typo in property name
def person = [name: "Alice", age: 30]
println person.nme   // MissingPropertyException

// CORRECT: Use correct property name
println person.name
```

```groovy
// WRONG: Property not defined
class Foo {
    void bar() { println x }  // x not defined
}

// CORRECT: Define the property
class Foo {
    def x = 42
    void bar() { println x }
}
```

## Examples

```groovy
println unknownVar         // MissingPropertyException
def s = "hello"
println s.nonExist         // MissingPropertyException
```

## Related Errors

- [MissingMethodException](/languages/groovy/missing-method) - method not found
