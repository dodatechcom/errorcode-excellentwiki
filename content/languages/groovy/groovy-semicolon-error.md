---
title: "Groovy CompileError Missing Semicolon Error"
description: "Fix Groovy compile errors for missing semicolons and statement terminators when using Java-style syntax."
languages: ["groovy"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Groovy does not require semicolons at end of lines, but compile errors occur when two statements on the same line are ambiguous without a separator, or when returning expressions from closures are incorrectly terminated.

## Common Causes

- Two method calls on the same line without semicolon separator
- Variable declaration followed by another statement on same line
- Missing newline after return statement in certain contexts
- Method chain spanning lines without proper continuation
- Import statements missing semicolons when multiple on same line

## How to Fix

```groovy
// WRONG: Ambiguous two statements on one line
println("hello") println("world")  // compile error

// CORRECT: Add semicolon or newline
println("hello"); println("world")
// or
println("hello")
println("world")
```

```groovy
// WRONG: Return on same line as next statement
def x = 1 return x  // compile error

// CORRECT: Separate statements
def x = 1
return x
```

## Examples

```groovy
// Example 1: Multiple statements need semicolons
def a = 1; def b = 2; def c = a + b

// Example 2: Method chains without semicolons (works fine)
def result = [1, 2, 3]
    .collect { it * 2 }
    .findAll { it > 2 }

// Example 3: One-liner closures
def greet = { name -> "Hello, $name!" }
def result = greet("World")
```

## Related Errors

- [Syntax error](groovy-syntax-error) -- general syntax problems
- [Compile error](groovy-compile-error) -- compilation failures
