---
title: "Groovy Swapping Operator Error Fix"
description: "Fix Groovy swapping operator (=..=) errors when exchanging variable values between incompatible types or non-assignable targets."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The Groovy swapping operator `=..=` exchanges the values of two variables. Errors occur when the variables have incompatible types, are final, or when one side is a method return value that cannot be assigned.

## Common Causes

- Swapping with final variables or constants
- One side is a method return value (not an l-value)
- Type incompatibility prevents assignment
- Swapping with null when the other side has strict typing
- Attempting to swap with a property that has a setter constraint

## How to Fix

```groovy
// WRONG: Cannot swap with non-assignable
def (a, b) = [1, 2]
(1 + 2) =..= a  // error: cannot assign to expression

// CORRECT: Use assignable variables
def (a, b) = [1, 2]
a =..= b
println "a=$a, b=$b"  // a=2, b=1
```

```groovy
// WRONG: Swapping incompatible final types
final int x = 5
final String y = "hello"
x =..= y  // type mismatch

// CORRECT: Use non-final variables
def x = 5
def y = "hello"
x =..= y
println "x=$x, y=$y"  // x=hello, y=5 (Groovy is dynamic)
```

## Examples

```groovy
// Example 1: Basic swap
def a = 10
def b = 20
a =..= b
println "a=$a, b=$b"  // a=20, b=10

// Example 2: Swap in list
def list = [3, 1, 4, 1, 5]
list[0] =..= list[4]
println list  // [5, 1, 4, 1, 3]

// Example 3: Swap with different types
def x = "hello"
def y = 42
x =..= y
println "x=${x.class}: $x"  // x=class java.lang.Integer: 42
println "y=${y.class}: $y"  // y=class java.lang.String: hello
```

## Related Errors

- [Type mismatch error](groovy-type-mismatch) -- type conversion problems
- [Cast error](groovy-casterror) -- explicit type casting issues
