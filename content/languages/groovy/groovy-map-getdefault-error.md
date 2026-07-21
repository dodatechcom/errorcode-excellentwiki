---
title: "Groovy Map GetOrDefault Key Missing Error"
description: "Fix Groovy map key missing errors when accessing map entries that do not exist without providing default values."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Accessing a non-existent key in a Groovy map with bracket notation returns null, which can cause NullPointerException downstream. The `getOrDefault` or safe navigation operator prevents this.

## Common Causes

- Map key name has typo (case-sensitive)
- Key was never added to the map
- Using `.` property access on a map returned from a method that may return null
- Nested map access without null checking intermediate maps
- Key exists but with different type (String vs Integer)

## How to Fix

```groovy
// WRONG: Direct access without default
def config = [host: "localhost", port: 8080]
def timeout = config.timeout  // null, not a Number

// CORRECT: Use getOrDefault or Elvis
def timeout = config.timeout ?: 30
// or
def timeout = config.getOrDefault("timeout", 30)
```

```groovy
// WRONG: Nested map access
def data = [user: [name: "Alice"]]
def city = data.user.address.city  // NullPointerException

// CORRECT: Safe navigation
def city = data.user?.address?.city ?: "Unknown"
```

## Examples

```groovy
// Example 1: Safe map access
def map = [a: 1, b: 2, c: 3]
println map.a          // 1
println map.d          // null
println map.d ?: 0     // 0

// Example 2: getOrDefault
def props = new Properties()
props.load(new File("config.properties").newReader())
def timeout = props.getProperty("timeout", "30")

// Example 3: withDefault for auto-vivification
def cache = [:].withDefault { key -> [] }
cache.names << "Alice"
cache.scores << 95
println cache  // {names: ["Alice"], scores: [95]}
```

## Related Errors

- [Missing property error](groovy-missingproperty) -- property not found
- [Null pointer error](groovy-null-pointer) -- null reference crashes
