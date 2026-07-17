---
title: "[Solution] Groovy MissingMethodException"
description: "Fix Groovy MissingMethodException when calling methods that don't exist. Check method names, arguments, and metaclass."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MissingMethodException` occurs when Groovy cannot find a method with the given name and argument types on an object. This is a runtime error in Groovy's dynamic dispatch system.

## Common Causes

- Typo in method name
- Wrong number of arguments
- Wrong argument types
- Method not defined on the class
- Missing method in metaclass

## How to Fix

```groovy
// WRONG: Typo in method name
def person = new Person(name: "Alice")
person.nme  // MissingMethodException

// CORRECT: Use correct method name
person.name
```

```groovy
// WRONG: Wrong argument count
def add(int a, int b) { a + b }
add(1)  // MissingMethodException

// CORRECT: Provide correct arguments
add(1, 2)
```

```groovy
// WRONG: Wrong argument type
def greet(String name) { "Hello, $name" }
greet(42)  // MissingMethodException

// CORRECT: Pass correct type
greet("Alice")
```

```groovy
// WRONG: Calling method on null
def obj = null
obj.method()  // NullPointerException, not MissingMethod

// CORRECT: Null check
obj?.method()
```

## Examples

```groovy
// Example 1: Check available methods
def methods = String.class.methods.collect { it.name }
println methods

// Example 2: Use methodMissing for dynamic dispatch
class DynamicClass {
    def methodMissing(String name, args) {
        println "Called missing method: $name with args: $args"
    }
}

// Example 3: MetaClass method
String.metaClass.shout = { -> delegate.toUpperCase() + "!" }
println "hello".shout()  // HELLO!
```

## Related Errors

- [groovy-missingproperty]({{< relref "/languages/groovy/groovy-missingproperty" >}}) — missing property
- [groovy-nullpointererror]({{< relref "/languages/groovy/groovy-nullpointererror" >}}) — null pointer
- [groovy-casterror]({{< relref "/languages/groovy/groovy-casterror" >}}) — class cast error
