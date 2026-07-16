---
title: "ClassCastException"
description: "A ClassCastException occurs when attempting to cast an object to a class it is not an instance of."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cast", "class", "type", "classcastexception"]
weight: 5
---

## What This Error Means

A `ClassCastException` is thrown when you try to cast an object to a type that it isn't compatible with. Groovy performs runtime type checking for explicit casts using the `as` keyword.

## Common Causes

- Casting incompatible types
- Assumptions about return types from methods
- Generic type erasure causing wrong assumptions
- Interoperating with Java collections

## How to Fix

```groovy
// WRONG: Invalid cast
def x = "hello"
def n = x as int  // ClassCastException

// CORRECT: Check type before casting
def x = "hello"
if (x instanceof Integer) {
    def n = x as int
}
```

```groovy
// WRONG: Wrong generic type assumption
List<Integer> numbers = [1, 2, 3]
numbers.add("four")  // may fail at runtime with ClassCastException

// CORRECT: Use proper typing
List<Integer> numbers = [1, 2, 3]
numbers.add(4)  // correct
```

## Examples

```groovy
// Example 1: String to Integer
def s = "hello"
int n = s as int  // ClassCastException

// Example 2: Wrong collection type
def list = [1, 2, 3] as ArrayList
list.add("four")  // ClassCastException when iterating

// Example 3: Interface cast
class Dog { void bark() {} }
def animal = new Dog()
def runnable = animal as Runnable  // ClassCastException
```

## Related Errors

- [NullPointerException](/languages/groovy/null-pointer5)
- [MissingMethodException: No signature of method](/languages/groovy/missing-method)
