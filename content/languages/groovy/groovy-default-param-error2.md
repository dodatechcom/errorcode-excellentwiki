---
title: "Groovy Default Parameter Value Error"
description: "Fix Groovy default parameter errors when optional parameters are not at the end of the parameter list."
languages: ["groovy"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Groovy allows default parameter values, but compilation errors occur when default parameters are followed by required parameters, or when the default value expression has side effects or type conflicts.

## Common Causes

- Default parameter not at the end of the parameter list
- Default value expression has runtime dependencies that are not available at declaration
- Type of default value does not match the parameter type
- Method overloading conflicts with default parameter variants
- Using default parameters in abstract methods

## How to Fix

```groovy
// WRONG: Default parameter before required parameter
def greet(name = "World", greeting) {  // compile error
    "$greeting, $name!"
}

// CORRECT: Default parameters at the end
def greet(greeting, name = "World") {
    "$greeting, $name!"
}
greet("Hello")          // "Hello, World!"
greet("Hi", "Alice")    // "Hi, Alice!"
```

```groovy
// WRONG: Default value with side effect at declaration time
def process(data, count = items.size()) {  // items not defined yet
    data.take(count)
}

// CORRECT: Use null check instead
def process(data, count = null) {
    def actualCount = count ?: data.size()
    data.take(actualCount)
}
```

## Examples

```groovy
// Example 1: Multiple defaults
def createUser(name, role = "user", active = true) {
    [name: name, role: role, active: active]
}
createUser("Alice")                    // [name:"Alice", role:"user", active:true]
createUser("Bob", "admin")             // [name:"Bob", role:"admin", active:true]
createUser("Eve", "viewer", false)     // [name:"Eve", role:"viewer", active:false]

// Example 2: Default with complex expression
def fetchData(url, timeout = 30_000, retries = 3) {
    for (i in 1..retries) {
        try { return url.toURL().text } catch (e) { }
    }
    null
}

// Example 3: Named parameters with defaults
def config(host = "localhost", port = 8080, secure = false) {
    [host: host, port: port, secure: secure]
}
config(port: 443, secure: true)
```

## Related Errors

- [Compile error argument](groovy-default-param) -- parameter declaration issues
- [Compile error](groovy-compile-error) -- compilation failures
