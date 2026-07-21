---
title: "Groovy GDK Method Not Found Error"
description: "Fix Groovy GDK method errors when enhanced collection methods fail due to missing imports or wrong method signatures."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Groovy Development Kit (GDK) adds convenience methods to Java classes like String, File, and collections. These methods may not be found if the Groovy version differs or if the code is called from plain Java context.

## Common Causes

- GDK method is version-specific and not available in current Groovy
- Calling GDK methods from Java code compiled against JDK only
- Method name conflicts with Java standard library methods
- GDK method requires specific Groovy imports not present
- Using GDK on a subclass that overrides the enhanced method

## How to Fix

```groovy
// WRONG: GDK method not available in Java context
// This works in Groovy but not when called from Java
String s = "hello world"
s.tokenize(" ")  // GDK method, may fail in Java

// CORRECT: Use standard Java methods or explicit Groovy API
String s = "hello world"
s.split(" ")  // standard Java
// or in Groovy context:
s.tokenize(" ")  // works
```

```groovy
// WRONG: Assuming GDK collect on non-iterable
int x = 42
x.collect { it * 2 }  // MissingMethodException

// CORRECT: Use GDK on appropriate types
def list = [1, 2, 3]
list.collect { it * 2 }  // [2, 4, 6]
```

## Examples

```groovy
// Example 1: String GDK methods
def s = "  Hello World  "
println s.trim()           // Java method
println s.capitalize()     // GDK method
println s.center(20)       // GDK method

// Example 2: File GDK methods
def f = new File("test.txt")
println f.text             // GDK: reads entire file
f.eachLine { println it }  // GDK: iterates lines

// Example 3: List GDK methods
def nums = [3, 1, 4, 1, 5]
println nums.toSet()       // [3, 1, 4, 5]
println nums.groupBy { it % 2 }  // {[1]:[1,1,5], [0]:[3,4]}
```

## Related Errors

- [Missing method error](groovy-missing-method) -- GDK method not available
- [Missing property error](groovy-missingproperty) -- GDK property access
