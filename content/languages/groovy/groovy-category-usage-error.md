---
title: "Groovy Category Usage Error Fix"
description: "Fix Groovy Category usage errors when categories are not properly registered or used outside the use block."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Groovy Categories add methods to existing classes within a `use` block. Outside this block, the added methods are not available, causing `MissingMethodException`.

## Common Causes

- Calling category method outside the `use` block
- Category class does not follow the static method convention
- Category method signature does not match expected parameters
- Category was defined in a different module not imported
- Multiple categories with conflicting method names

## How to Fix

```groovy
// WRONG: Category method called outside use block
class StringUtils {
    static String shout(String self) { self.toUpperCase() + "!" }
}
def s = "hello"
s.shout()  // MissingMethodException

// CORRECT: Wrap in use block
use(StringUtils) {
    def s = "hello"
    println s.shout()  // "HELLO!"
}
```

```groovy
// WRONG: Category method is not static
class StringUtils {
    String shout() { this.toUpperCase() + "!" }  // not static
}

// CORRECT: Category methods must be static
class StringUtils {
    static String shout(String self) { self.toUpperCase() + "!" }
}
```

## Examples

```groovy
// Example 1: Custom Integer category
class IntegerCategory {
    static Boolean isEven(Integer self) { self % 2 == 0 }
    static Boolean isOdd(Integer self) { self % 2 != 0 }
}

use(IntegerCategory) {
    println 4.isEven()   // true
    println 7.isOdd()    // true
}

// Example 2: Category with multiple methods
class FileCategory {
    static String readText(File self) { self.text }
    static List<String> readLines(File self) { self.readLines() }
}

use(FileCategory) {
    def f = new File("data.txt")
    println f.readText()
}

// Example 3: Nested use blocks
use(StringUtils, IntegerCategory) {
    println "hello".shout()
    println 42.isEven()
}
```

## Related Errors

- [Missing method error](groovy-missing-method) -- method not found
- [Runtime error](groovy-runtime-error) -- general runtime issues
