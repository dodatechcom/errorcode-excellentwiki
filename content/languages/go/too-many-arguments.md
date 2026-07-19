---
title: "[Solution] Go too many arguments / not enough arguments — Compile Error Fix"
description: "Fix Go too many arguments or not enough arguments error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# too many arguments / not enough arguments

The error `not enough arguments in call to X` or `too many arguments in call to X` occurs when argument count doesn't match.

## How to Fix

### Fix 1: Match argument count

```go
func add(a, b int) int { return a + b }

add(1)       // error: not enough arguments
add(1, 2)    // correct
add(1, 2, 3) // error: too many arguments
```

### Fix 2: Pass slice to variadic with ...

```go
s := []int{1, 2, 3}
sum(s...)
```

## Examples

```go
package main

func greet(name string, age int) {}

func main() {
    greet("Alice")
}
```

Output:
```
not enough arguments in call to greet
```

## Related Errors

- [undefined-name]({{< relref "/languages/go/undefined-name" >}}) — undefined name.
- [cannot-use-type]({{< relref "/languages/go/cannot-use-type" >}}) — type mismatch.
