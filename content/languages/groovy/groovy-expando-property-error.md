---
title: "Groovy Expando MetaClass Dynamic Property Error"
description: "Fix Groovy Expando and MetaClass dynamic property errors when adding properties at runtime that conflict with existing ones."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Expando objects allow adding properties dynamically, but errors occur when property names conflict with Groovy reserved words, when Expando is used with CompileStatic, or when dynamic properties shadow existing methods.

## Common Causes

- Property name matches a Groovy built-in method (e.g., `class`, `metaClass`)
- Using CompileStatic with Expando (dynamic properties not visible)
- Setting Expando properties in wrong order
- Expando property name contains special characters
- Thread-safety issues with shared Expando instances

## How to Fix

```groovy
// WRONG: Property name shadows built-in
def exp = new Expando()
exp.class = "test"  // shadows Object.getClass()
println exp.class   // returns the Class, not "test"

// CORRECT: Use unique property names
def exp = new Expando()
exp.className = "test"
println exp.className  // "test"
```

```groovy
// WRONG: Expando with @CompileStatic
@CompileStatic
class Foo {
    void test() {
        def exp = new Expando()
        exp.name = "Alice"
        println exp.name  // compile error
    }
}

// CORRECT: Use Map or remove CompileStatic
def map = [name: "Alice"]
println map.name
```

## Examples

```groovy
// Example 1: Basic Expando
def exp = new Expando()
exp.firstName = "Alice"
exp.lastName = "Smith"
exp.fullName = { -> "${firstName} ${lastName}" }
println exp.fullName()  // "Alice Smith"

// Example 2: Dynamic class creation
def DynClass = new Expando()
DynClass.someMethod = { println "Hello!" }
def obj = DynClass.create()
obj.someMethod()  // "Hello!"

// Example 3: Expando as configuration
def config = new Expando()
config.host = "localhost"
config.port = 8080
config.timeout = 30
println "${config.host}:${config.port}"
```

## Related Errors

- [Metaclass error](metaclass-error) -- metaclass modification issues
- [Expando error](groovy-expando-error) -- Expando-related problems
