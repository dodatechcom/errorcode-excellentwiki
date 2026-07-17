---
title: "[Solution] Go Nil Map Assignment — Runtime Error Fix"
description: "Fix Go nil map panic when assigning to an uninitialized map. Always use make() to initialize maps before writing entries."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Nil Map Assignment — Runtime Error Fix

Assigning to an entry in a nil map causes a runtime panic. Maps in Go must be initialized before writing to them.

## Description

In Go, a declared but uninitialized map is `nil`. While reading from a nil map returns the zero value (no panic), writing to one panics with `assignment to entry in nil map`. This often happens when a map is returned from a function or stored in a struct without being properly initialized.

Common scenarios:

- **Uninitialized struct field map** — a map field in a struct left as its zero value.
- **Returned map from failed init** — a function returns nil instead of an initialized map.
- **Map parameter not checked** — passing a nil map to a function that writes to it.
- **Conditional initialization skipped** — the `make()` call is in a branch that doesn't execute.

## Common Causes

```go
// Cause 1: Struct field map not initialized
type Cache struct {
    items map[string]string
}

func main() {
    c := Cache{}
    c.items["key"] = "value" // panic: assignment to entry in nil map
}

// Cause 2: Function returns nil map
func buildMap() map[string]int {
    var m map[string]int
    return m
}

func main() {
    m := buildMap()
    m["x"] = 1 // panic
}

// Cause 3: Map parameter used without init
func populate(m map[string]int) {
    m["count"] = 100 // panics if m is nil
}

func main() {
    var m map[string]int
    populate(m) // panic
}

// Cause 4: Conditional make skipped
func main() {
    var m map[string]int
    if false {
        m = make(map[string]int)
    }
    m["a"] = 1 // panic
}
```

## How to Fix

### Fix 1: Always use make() to initialize maps

```go
// Wrong
var m map[string]int
m["key"] = 1

// Correct
m := make(map[string]int)
m["key"] = 1
```

### Fix 2: Initialize maps in struct constructors

```go
// Wrong
type Cache struct {
    items map[string]string
}

func newCache() *Cache {
    return &Cache{} // items is nil
}

// Correct
func newCache() *Cache {
    return &Cache{items: make(map[string]string)}
}
```

### Fix 3: Initialize maps before passing to functions

```go
// Wrong
var m map[string]int
populate(m)

// Correct
m := make(map[string]int)
populate(m)
```

### Fix 4: Use map literal syntax

```go
// Wrong
var m map[string]int

// Correct — map literal is already initialized
m := map[string]int{"a": 1}
```

## Examples

```go
// This triggers: panic: assignment to entry in nil map
package main

func main() {
    var scores map[string]int
    scores["alice"] = 100
}
```

## Related Errors

- [concurrent-map-write]({{< relref "/languages/go/concurrent-map-write" >}}) — writing to a map from multiple goroutines without synchronization.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil pointer (related nil-value panic).
- [index-out-of-range]({{< relref "/languages/go/index-out-of-range" >}}) — accessing a slice index beyond its bounds.
