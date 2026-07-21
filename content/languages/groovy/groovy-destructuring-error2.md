---
title: "Groovy Destructuring Declaration Error"
description: "Fix Groovy destructuring errors when unpacking lists or maps with incorrect variable count or type mismatches."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Destructuring errors occur when Groovy tries to unpack a collection into variables but the number of variables does not match the collection size, or the types are incompatible with the target variables.

## Common Causes

- More variables declared than elements in the collection
- Fewer variables than elements (extra elements ignored silently)
- Destructuring a map where key names do not match variable names
- Attempting to destructure a non-iterable type
- Using destructuring in for-loop with wrong collection structure

## How to Fix

```groovy
// WRONG: Variable count mismatch
def (a, b, c) = [1, 2]
// c is null, no error but may cause issues later

// CORRECT: Match variable count or use rest parameter
def (a, b) = [1, 2]
// or
def (a, b, *rest) = [1, 2, 3, 4]
// a=1, b=2, rest=[3,4]
```

```groovy
// WRONG: Destructuring map with wrong key names
def (name, age) = [name: "Alice", age: 30]
// name and age are both null because map destructuring uses index, not keys

// CORRECT: Use .keySet() or iterate differently
def map = [name: "Alice", age: 30]
def name = map.name
def age = map.age
```

## Examples

```groovy
// Example 1: List destructuring
def (first, second, third) = ["a", "b", "c"]
println "$first, $second, $third"  // a, b, c

// Example 2: Map entry iteration
def map = [x: 1, y: 2, z: 3]
map.each { key, value ->
    println "$key -> $value"
}

// Example 3: Destructuring in closures
def process = { String name, int age ->
    println "$name is $age years old"
}
def data = ["Alice", 30]
process(*data)
```

## Related Errors

- [Index out of bounds error](groovy-index-out-of-bounds) -- collection access issues
- [Cast error](groovy-casterror) -- type conversion problems
