---
title: "Groovy parse error"
description: "A Groovy parse error occurs when the Groovy compiler encounters syntax that violates the language grammar."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Groovy parse error is raised when the Groovy parser encounters code that doesn't conform to the language's syntax rules. This is typically a compile-time error that prevents the script or class from being executed.

## Common Causes

- Missing or mismatched parentheses, brackets, or braces
- Invalid operator usage
- Missing semicolons (when not using newline inference)
- Invalid string interpolation syntax

## How to Fix

```groovy
// WRONG: Missing closing brace
class Greeter {
    void greet() {
        println "hello"
    // missing closing brace
// Groovy parse error

// CORRECT: Balance braces
class Greeter {
    void greet() {
        println "hello"
    }
}
```

```groovy
// WRONG: Invalid string interpolation
def name = "World"
def msg = "Hello, ${name"  // Groovy parse error

// CORRECT: Proper interpolation syntax
def msg = "Hello, ${name}"
def msg2 = "Hello, $name"
```

## Examples

```groovy
// Example 1: Mismatched parentheses
def x = (1 + 2  // parse error

// Example 2: Invalid GString
def s = "Hello ${name"  // parse error

// Example 3: Missing import statement context
import groovy.util.*  // works, but:
import groovy.util  // parse error
```

## Related Errors

- [MissingMethodException: No signature of method](/languages/groovy/missing-method)
- [MissingPropertyException: No such property](/languages/groovy/missing-property)
