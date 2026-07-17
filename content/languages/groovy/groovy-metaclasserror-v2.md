---
title: "[Solution] Groovy MissingMethodException on MetaClass"
description: "Fix Groovy metaclass errors when dynamic method dispatch fails on metaclass. Handle runtime method addition and interception."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A metaclass error occurs when Groovy's dynamic method dispatch fails on a metaclass. This happens when trying to call methods that haven't been added to the metaclass or when metaclass manipulation is incorrect.

## Common Causes

- Calling method added to wrong metaclass
- Metaclass method override causing recursion
- Instance metaclass vs class metaclass conflicts
- Method not properly added to metaclass

## How to Fix

```groovy
// WRONG: Method not on metaclass
String.metaClass.myMethod = { -> "hello" }
def s = "test"
s.myMethod()  // May fail depending on Groovy version

// CORRECT: Use proper metaclass definition
String.metaClass.myMethod = { -> "hello" }
def s = "test"
s.myMethod()  // "hello"
```

```groovy
// WRONG: Infinite recursion in metaclass
String.metaClass.toString = { delegate.toUpperCase() }  // Calls itself

// CORRECT: Call original method
String.metaClass.toString = { ->
    delegate.toUpperCase()
}
// Better: use a named method instead
String.metaClass.myToString = { -> delegate.toUpperCase() }
```

```groovy
// WRONG: Instance metaclass conflict
def obj = "hello"
obj.metaClass.newMethod = { -> "instance method" }
obj.metaClass.newMethod()  // May work differently than expected

// CORRECT: Verify method availability
if (obj.metaClass.respondsTo(obj, 'newMethod')) {
    obj.metaClass.newMethod()
}
```

## Examples

```groovy
// Example 1: Add method to class metaclass
Integer.metaClass.isEven = { -> delegate % 2 == 0 }
println 4.isEven()  // true

// Example 2: Intercept all method calls
String.metaClass.methodMissing = { String name, args ->
    println "Called: $name(${args.join(', ')})"
    "intercepted"
}
println "hello".nonExistentMethod("arg")  // "intercepted"

// Example 3: Per-instance metaclass
def obj = "hello"
obj.metaClass.toUpperCase2 = { -> delegate.toUpperCase() + "!" }
println obj.toUpperCase2()  // HELLO!
```

## Related Errors

- [groovy-missingmethod]({{< relref "/languages/groovy/groovy-missingmethod" >}}) — missing method
- [groovy-missingproperty]({{< relref "/languages/groovy/groovy-missingproperty" >}}) — missing property
- [groovy-asterror]({{< relref "/languages/groovy/groovy-asterror" >}}) — AST error
