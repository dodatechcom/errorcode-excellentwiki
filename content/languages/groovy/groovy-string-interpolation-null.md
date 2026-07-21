---
title: "Groovy String Interpolation Null Error"
description: "Fix Groovy string interpolation errors when interpolating null values into GString templates produces unexpected output."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

String interpolation in Groovy with `${variable}` or `${expr}` silently converts null to the string "null". This can cause confusing output or downstream parsing errors when "null" is not a valid value.

## Common Causes

- Object property returns null, interpolated as string "null"
- Map lookup returns null, producing "null" in output
- Method call in interpolation returns null
- Null in nested property chain produces "null" instead of error
- JSON/XML serialization containing literal "null" strings

## How to Fix

```groovy
// WRONG: Null becomes string "null"
def name = null
def msg = "Hello, ${name}!"  // "Hello, null!"

// CORRECT: Use Elvis for default
def msg = "Hello, ${name ?: 'stranger'}!"
```

```groovy
// WRONG: Nested null in string
def user = [name: "Alice", address: null]
def msg = "${user.name} lives at ${user.address.city}"
// NullPointerException at .city

// CORRECT: Safe navigation
def msg = "${user.name} lives at ${user.address?.city ?: 'unknown'}"
```

## Examples

```groovy
// Example 1: Null interpolation
def x = null
println "Value: ${x}"        // "Value: null"
println "Value: ${x ?: ''}"  // "Value: "

// Example 2: Safe string building
def person = [name: "Bob", phone: null]
def contact = "${person.name}${person.phone ? ', ' + person.phone : ''}"
println contact  // "Bob"

// Example 3: Triple-quoted GString
def config = [host: "localhost", port: null]
def url = """
    Host: ${config.host ?: 'default'}
    Port: ${config.port ?: 8080}
"""
println url
```

## Related Errors

- [Null pointer error](groovy-null-pointer) -- null reference issues
- [GString error](groovy-gstring-error) -- GString formatting problems
