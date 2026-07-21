---
title: "Groovy Named Parameter Constructor Error"
description: "Fix Groovy named parameter constructor errors when passing named arguments to classes without matching properties."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Named parameter constructors in Groovy map argument names to property setters. Errors occur when a named parameter does not match any property, when the property is private without a setter, or when the value type is incompatible.

## Common Causes

- Named parameter does not match any property name
- Property exists but has no setter (private, final without setter)
- Value type incompatible with property type
- Typo in parameter name (Groovy is case-sensitive)
- Using named parameters with a Java class without @NamedArg support

## How to Fix

```groovy
// WRONG: Property does not exist
class Person {
    String name
    int age
}
def p = new Person(name: "Alice", gender: "F")
// MissingPropertyException: gender

// CORRECT: Only use existing properties
def p = new Person(name: "Alice", age: 30)
```

```groovy
// WRONG: Final property without constructor support
class Config {
    final String host  // no setter
}
def c = new Config(host: "localhost")  // error

// CORRECT: Add constructor or make non-final
class Config {
    String host
    Config(String host) { this.host = host }
}
def c = new Config("localhost")
```

## Examples

```groovy
// Example 1: Basic named parameters
class User {
    String name
    int age
    boolean active = true
}
def user = new User(name: "Alice", age: 30)
println "${user.name}, ${user.age}, active: ${user.active}"

// Example 2: With inheritance
class Animal {
    String name
}
class Dog extends Animal {
    String breed
}
def dog = new Dog(name: "Rex", breed: "Labrador")

// Example 3: Map constructor pattern
class Point {
    double x, y
    static Point of(Map params) {
        new Point(x: params.x, y: params.y)
    }
}
```

## Related Errors

- [Missing property error](groovy-missingproperty) -- property not found
- [Property access error](groovy-property-access-error) -- property access issues
