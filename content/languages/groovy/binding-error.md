---
title: "Binding error"
description: "A Binding error occurs when accessing a variable that hasn't been defined in the current binding or scope."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Binding error occurs when you try to access a variable that hasn't been bound in the current scope. In Groovy scripts, binding manages variable resolution, and accessing undefined variables through binding causes this error.

## Common Causes

- Typo in variable name
- Variable not defined in script binding
- Accessing variable from wrong scope
- Script compilation issue

## How to Fix

```groovy
// WRONG: Accessing undefined binding variable
println myVar  // MissingPropertyException (binding error)

// CORRECT: Define variable first
def myVar = "hello"
println myVar
```

```groovy
// WRONG: Variable in different binding
def binding1 = new Binding()
binding1.setVariable("x", 10)

def shell = new GroovyShell(binding1)
def script = shell.parse("println y")  // y not in binding1
script.run()  // MissingPropertyException

// CORRECT: Set all required variables
binding1.setVariable("x", 10)
binding1.setVariable("y", 20)  // now available in script
```

## Examples

```groovy
// Example 1: Undefined variable in script
def script = new GroovyShell().parse("println undefinedVar")
script.run()  // MissingPropertyException

// Example 2: Wrong binding variable name
def b = new Binding()
b.setVariable("name", "Alice")
def s = new GroovyShell(b)
s.parse("println nme")  // typo in variable name

// Example 3: Scope issue
def x = 10
def closure = { println y }  // y not in closure scope
closure()  // MissingPropertyException
```

## Related Errors

- [MissingPropertyException: No such property](/languages/groovy/missing-property)
- [MissingMethodException: No signature of method](/languages/groovy/missing-method)
