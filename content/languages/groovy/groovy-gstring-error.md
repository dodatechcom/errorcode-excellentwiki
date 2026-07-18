---
title: "[Solution] Groovy GString Interpolation Error"
description: "Fix Groovy GString interpolation errors. Handle variable resolution, escaping, and toString conversions."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

GString interpolation errors occur when Groovy cannot resolve a variable or expression inside a GString template. This includes missing properties, failed toString calls, and syntax errors in expressions.

## Why It Happens

- Variable name does not exist in current scope: The variable referenced in `${}` is not defined.
- Property access on null object within interpolation: The object is null when property is accessed.
- Complex expression has syntax errors: The expression inside `${}` contains invalid syntax.
- Escaped dollar sign still interpolated: The escaping mechanism was not applied correctly.
- Object has no meaningful toString implementation: The default toString is not informative.

## How to Fix It

Verify variable exists before interpolation:

```groovy
def name = "Alice"
println "Hello, ${name}!"  // Works

// WRONG: Variable does not exist
// println "Value: ${undefinedVar}"

// CORRECT: Check existence first
if (this.hasProperty('undefinedVar')) {
    println "Value: ${this.undefinedVar}"
} else {
    println "Variable not defined"
}
```

Use safe navigation in interpolation:

```groovy
def user = null
// WRONG: NullPointerException
// println "Name: ${user.name}"

// CORRECT: Safe navigation
println "Name: ${user?.name ?: 'Unknown'}"
```

Escape dollar signs properly:

```groovy
// WRONG: Interpolates $variable
def price = "Cost: $100"

// CORRECT: Escape dollar sign
def price = 'Cost: $100'
def price2 = "Cost: \$100"

// Triple-quoted strings do not interpolate
def raw = '''No interpolation: ${var}'''
```

Use expressions in interpolation:

```groovy
def items = [1, 2, 3]
println "Count: ${items.size()}"
println "Sum: ${items.sum()}"
println "First: ${items?.first() ?: 'empty'}"
```

Use string concatenation for simple cases:

```groovy
// For simple cases, concatenation may be clearer
def greeting = "Hello, " + name + "!"
```

Use string manipulation methods:

```groovy
def name = "Alice"
def greeting = "Hello, ${name.toUpperCase()}!"
println greeting
```

Handle multi-line GStrings:

```groovy
def user = [name: "Alice", age: 30]
def json = """{
    "name": "${user.name}",
    "age": ${user.age}
}"""
println json
```

Use format specifiers for precision:

```groovy
def value = 3.14159
println "Pi is ${String.format('%.2f', value)}"
```

## Common Mistakes

- Using double quotes when single quotes are needed for literal dollar signs.
- Forgetting that GString calls toString() automatically on objects.
- Not handling null values in complex expressions within interpolation.
- Mixing GString and String concatenation unnecessarily.
- Not understanding that triple-quoted strings do not support interpolation.
- Using GStrings for simple string constants. Single quotes are more efficient.
- Forgetting that GString equality is different from String equality.

## Related Pages

- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer
- [groovy-missing-property-v2]({{< relref "/languages/groovy/groovy-missingproperty-v2" >}}) - missing property
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
- [groovy-io-error]({{< relref "/languages/groovy/groovy-io-error" >}}) - I/O exception
