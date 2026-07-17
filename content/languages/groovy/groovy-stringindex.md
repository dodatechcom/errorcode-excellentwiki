---
title: "[Solution] Groovy StringIndexOutOfBoundsException"
description: "Fix Groovy StringIndexOutOfBoundsException when accessing characters beyond string length. Validate string indices."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `StringIndexOutOfBoundsException` occurs when you access a character or substring at an index that is beyond the string's length.

## Common Causes

- Index exceeds string length
- Off-by-one error in substring
- Empty string access
- Incorrect offset in substring operations
- User input without length validation

## How to Fix

```groovy
// WRONG: Index exceeds length
def str = "hello"
def ch = str.charAt(10)  // StringIndexOutOfBoundsException

// CORRECT: Check length first
def str = "hello"
if (str.length() > 10) {
    def ch = str.charAt(10)
}
```

```groovy
// WRONG: Substring beyond bounds
def str = "hello"
def sub = str.substring(3, 10)  // Error

// CORRECT: Clamp or check bounds
def str = "hello"
def end = Math.min(10, str.length())
def sub = str.substring(3, end)
```

```groovy
// WRONG: Accessing empty string
def str = ""
def ch = str.charAt(0)  // Error

// CORRECT: Check if empty
def str = ""
if (str.length() > 0) {
    def ch = str.charAt(0)
}
```

## Examples

```groovy
// Example 1: Safe char access
def safeChar(str, index) {
    if (str && index >= 0 && index < str.length()) {
        return str.charAt(index)
    }
    return null
}

// Example 2: Safe substring
def safeSubstring(str, start, end) {
    start = Math.max(0, start)
    end = Math.min(str?.length() ?: 0, end)
    if (start < end) {
        return str.substring(start, end)
    }
    return ""
}

// Example 3: Groovy GDK safe methods
def str = "hello"
def ch = str.getAt(2)  // 'l'
def sub = str[1..3]     // "ell"
```

## Related Errors

- [groovy-missingmethod]({{< relref "/languages/groovy/groovy-missingmethod" >}}) — missing method
- [groovy-nullpointererror]({{< relref "/languages/groovy/groovy-nullpointererror" >}}) — null pointer
- [groovy-casterror]({{< relref "/languages/groovy/groovy-casterror" >}}) — cast error
