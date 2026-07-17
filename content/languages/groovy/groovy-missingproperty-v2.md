---
title: "[Solution] Groovy MissingPropertyException"
description: "Fix Groovy MissingPropertyException when accessing non-existent properties. Check property names, scope, and object types."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["missing-property", "property", "scope", "dynamic", "groovy"]
weight: 5
---

## What This Error Means

A `MissingPropertyException` is thrown when Groovy tries to access a property that doesn't exist on an object or in the current binding/scope.

## Common Causes

- Typo in property name
- Property not defined in the current scope
- Accessing a property on a wrong object type
- Closures not having access to outer scope variables
- Script binding issues

## How to Fix

```groovy
// WRONG: Typo in property name
def person = [name: "Alice", age: 30]
println person.nme  // MissingPropertyException

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

```groovy
// WRONG: Closure missing outer variable
def localVar = 10
def cl = { println localVar }
localVar = null  // Now closure fails
cl()  // May fail

// CORRECT: Capture value
def localVar = 10
def captured = localVar
def cl = { println captured }
cl()  // Works
```

## Examples

```groovy
// Example 1: Check property existence
def person = [name: "Alice", age: 30]
println person.containsKey("name")  // true
println person.containsKey("email")  // false

// Example 2: Use propertyMissing for dynamic properties
class DynamicProps {
    def props = [:]
    def propertyMissing(String name) {
        props[name]
    }
    def propertyMissing(String name, value) {
        props[name] = value
    }
}

// Example 3: Safe navigation
def obj = null
println obj?.someProperty  // null, no exception
```

## Related Errors

- [groovy-missingmethod]({{< relref "/languages/groovy/groovy-missingmethod" >}}) — missing method
- [groovy-nullpointererror]({{< relref "/languages/groovy/groovy-nullpointererror" >}}) — null pointer
- [groovy-metaclasserror]({{< relref "/languages/groovy/groovy-metaclasserror" >}}) — metaclass error
