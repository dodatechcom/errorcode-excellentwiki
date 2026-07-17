---
title: "AST transformation error in Groovy"
description: "Fix AST transformation errors when compile-time code generation fails or produces incorrect code."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Groovy AST transformations modify the Abstract Syntax Tree at compile time to generate or modify code. Errors occur when the transformation produces invalid code or conflicts with existing code.

## Common Causes

- Built-in AST annotation used incorrectly
- Custom AST transformation has compile errors
- Conflicting AST transformations on same element
- Missing required annotation parameters

## How to Fix

```groovy
// WRONG: @Canonical on interface
@Canonical
interface MyInterface { }   // cannot be applied to interfaces

// CORRECT: Apply to class
@Canonical
class MyClass { String name; int age }
```

```groovy
// WRONG: Missing @Immutable fields
@Immutable
class Config { String name }

// CORRECT: Use @Immutable correctly
@Immutable
class Config { final String name; final int count }
```

## Examples

```groovy
@groovy.transform.ToString
class Person { String name; int age }
def p = new Person(name: "Alice")
println p   // Person(Alice, 0)
```

## Related Errors

- [MissingMethodException](/languages/groovy/missing-method) - compilation errors
- [Cast Error](/languages/groovy/cast-error) - type casting issues
