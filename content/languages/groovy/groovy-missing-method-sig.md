---
title: "Groovy MissingMethodException No Signature Error"
description: "Fix Groovy MissingMethodException when calling a method that does not exist on the target object or class."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MissingMethodException` is thrown when Groovy cannot find a method matching the name and argument types on the target object. This is common with dynamic method dispatch and GString interpolation.

## Common Causes

- Method name typo or case sensitivity mismatch
- Wrong number or types of arguments passed to the method
- Calling a method defined in a subclass from a parent reference
- GString used where a String is expected (GString is not String)
- Method defined in a trait but not mixed into the class

## How to Fix

```groovy
// WRONG: Method does not exist on String
def s = "hello"
s.nonExistentMethod()  // MissingMethodException

// CORRECT: Use existing String methods
def s = "hello"
s.toUpperCase()
s.capitalize()
s.reverse()
```

```groovy
// WRONG: GString where String expected
class Foo {
    void bar(String s) { println s }
}
def foo = new Foo()
foo.bar("hello")        // works
foo.bar("${'hello'}")  // MissingMethodException - GString != String

// CORRECT: Convert GString to String
foo.bar("${'hello'}".toString())
foo.bar("${'hello'}" as String)
```

## Examples

```groovy
// Example 1: Wrong argument types
class Calculator {
    int add(int a, int b) { a + b }
}
def calc = new Calculator()
calc.add(1, 2)      // works
calc.add("1", "2")  // MissingMethodException

// Example 2: Missing null check
def obj = null
obj.toString()  // NullPointerException not MissingMethod

// Example 3: Dynamic method call
def m = "hello"
m.invokeMethod("toUpperCase", [])  // works
m.invokeMethod("nonExistent", [])  // MissingMethodException
```

## Related Errors

- [Missing property error](groovy-missingproperty) -- property access failures
- [Class cast error](groovy-casterror) -- type conversion problems
