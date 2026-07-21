---
title: "Groovy MOP Metaclass Method Resolution Error"
description: "Fix Groovy MOP metaclass errors when method resolution fails due to ambiguous or incorrect metaclass modifications."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The Groovy Meta-Object Protocol (MOP) allows runtime modification of method resolution. Metaclass errors occur when method lookup fails due to conflicting registrations, invalid method closures, or circular method delegation.

## Common Causes

- Metaclass method override creates infinite recursion
- Multiple metaclass registrations conflict on the same method name
- Invalid closure registered as a metaclass method
- Metaclass changes on a class affecting all instances unexpectedly
- Attempting to override final methods through metaclass

## How to Fix

```groovy
// WRONG: Infinite recursion in metaclass override
String.metaClass.toString = {
    delegate.toString()  // calls itself infinitely
}
println "hello"

// CORRECT: Call original method via代言
String.metaClass.toString = ->
    delegate.toUpperCase()
```

```groovy
// WRONG: Metaclass override breaks all String instances
String.metaClass.length = { 0 }
"hello".length()  // returns 0 for all strings!

// CORRECT: Use per-instance metaClass
def s = "hello"
s.metaClass.length = { 0 }
s.length()  // 0
"world".length()  // 5 (unchanged)
```

## Examples

```groovy
// Example 1: Add method via metaclass
Integer.metaClass.isPrime = { ->
    if (delegate < 2) return false
    for (i in 2..Math.sqrt(delegate)) {
        if (delegate % i == 0) return false
    }
    true
}
println 17.isPrime()  // true

// Example 2: Method delegation pattern
class Animal { String sound = "..." }
Animal.metaClass.makeSound = {
    "${delegate.class.simpleName} says ${delegate.sound}"
}
def cat = new Animal(sound: "Meow")
println cat.makeSound()  // "Animal says Meow"

// Example 3: Reset metaclass
String.metaClass = null  // reset to default
```

## Related Errors

- [Metaclass error](metaclass-error) -- metaclass-related issues
- [Missing method error](groovy-missing-method) -- method not found
