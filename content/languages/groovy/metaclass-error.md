---
title: "Metaclass error"
description: "A Metaclass error occurs when accessing or modifying metaclass behavior that doesn't exist or is invalid."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["metaclass", "meta", "class", "groovy"]
weight: 5
---

## What This Error Means

A Metaclass error occurs when Groovy cannot find a method or property through the metaclass system, or when there's an issue with dynamic method resolution. This is related to Groovy's dynamic nature and metaclass programming.

## Common Causes

- Missing method on metaclass
- Invalid metaclass modification
- Category not properly registered
- Method not found in category or metaclass

## How to Fix

```groovy
// WRONG: Using non-existent metaclass method
String.metaClass.nonExistentMethod = { -> "hello" }
"hello".nonExistentMethod()  // works, but:
def s = "hello"
s.someOtherMethod()  // MissingMethodException

// CORRECT: Define and use consistently
String.metaClass.greet = { -> "Hello from metaclass" }
"hello".greet()  // "Hello from metaclass"
```

```groovy
// WRONG: Category not properly used
class StringUtils {
    static String shout(String self) { self.toUpperCase() + "!" }
}
// String.shout()  // doesn't work without use(StringUtils)

// CORRECT: Use category in scope
use(StringUtils) {
    println "hello".shout()  // HELLO!
}
```

## Examples

```groovy
// Example 1: Method not in metaclass
class MyClass {}
MyClass.metaClass.newMethod = { -> "new" }
def obj = new MyClass()
obj.oldMethod()  // MissingMethodException

// Example 2: Category scope issue
class Helper {
    static String help(String s) { "helped: $s" }
}
// Outside use(Helper), help() not available

// Example 3: Metaclass conflict
String.metaClass.toString = { -> "custom" }  // overrides toString
def s = "hello"
println s  // "custom" - may cause unexpected behavior
```

## Related Errors

- [MissingMethodException: No signature of method](/languages/groovy/missing-method)
- [MissingPropertyException: No such property](/languages/groovy/missing-property)
