---
title: "Groovy GString Equality Comparison Error"
description: "Fix Groovy GString and String equality comparison errors when comparing interpolated strings with plain strings."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## This Error Means

GString objects and String objects are different types in Groovy. While `==` performs `.equals()` on the value, Map keys and Set membership can behave unexpectedly when mixing GString and String.

## Common Causes

- Using GString as Map key where String was expected
- Comparing GString with `is()` instead of `==`
- Set containing both GString and String duplicates
- Interpolation in switch/case with String comparison
- Deserialized data is String but code compares with GString

## How to Fix

```groovy
// WRONG: GString and String as different Map keys
def map = [:]
map["key"] = "value"           // String key
map["${'key'}"] = "other"     // GString key -- TWO entries!
println map.size()             // 2, not 1

// CORRECT: Convert to String
def map = [:]
map["key"] = "value"
map["${'key'}".toString()] = "other"
println map.size()             // 1 -- same key
```

```groovy
// WRONG: Using is() for comparison
def s1 = "hello"
def s2 = "${'hel'}lo"
println s1.is(s2)     // false -- different objects

// CORRECT: Use == for value equality
println s1 == s2       // true
```

## Examples

```groovy
// Example 1: Set deduplication
Set set = ["hello", "${'hello'}" as String, "${'hello'}"]
println set.size()  // 2 (GString and String are different)

// Example 2: Enum comparison
enum Color { RED, BLUE }
def c = Color.RED
def name = "${'RED'}"
println c.name() == name        // true (String comparison)
println c.name().is(name)       // false

// Example 3: Safe comparison method
def safeEquals(a, b) {
    a?.toString() == b?.toString()
}
```

## Related Errors

- [GString error](groovy-gstring-error) -- GString formatting issues
- [String equality error](groovy-string-gstring-equality) -- equality edge cases
