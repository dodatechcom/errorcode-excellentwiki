---
title: "[Solution] Go Assignment to Entry in Nil Map — Runtime Error Fix"
description: "Fix Go panic: assignment to entry in nil map. Initialize maps with make() before writing to them."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["map", "nil", "init", "make", "panic"]
weight: 5
---

# Assignment to Entry in Nil Map — Runtime Error Fix

An assignment to entry in nil map panic occurs when you try to write a key-value pair to a map that has not been initialized.

## Description

In Go, maps must be initialized with `make()` or a map literal before writing to them. Reading from a nil map returns the zero value without panicking, but writing to one causes a runtime panic.

Common scenarios:

- **Declaring map without initializing** — `var m map[string]int` leaves `m` as nil.
- **Forgetting to initialize in a function** — passing a nil map to a function that writes to it.
- **Unmarshaling into a nil map** — JSON unmarshaling into a struct field that is a nil map.

## Common Causes

```go
// Cause 1: Declared but not initialized
var m map[string]int
m["key"] = 42 // panic: assignment to entry in nil map

// Cause 2: Nil map from function return
func getMap() map[string]int {
    return nil
}

func main() {
    m := getMap()
    m["key"] = 42 // panic
}

// Cause 3: Struct with map field not initialized
type Config struct {
    Headers map[string]string
}

func main() {
    cfg := Config{}
    cfg.Headers["Content-Type"] = "application/json" // panic
}

// Cause 4: Reading is fine, writing panics
var m map[string]int
v := m["key"] // Returns 0, no panic
m["key"] = 1  // panic
```

## How to Fix

### Fix 1: Initialize maps with make()

```go
// Wrong
var m map[string]int
m["key"] = 42

// Correct
m := make(map[string]int)
m["key"] = 42
```

### Fix 2: Use map literal syntax

```go
// Wrong
var m map[string]int

// Correct
m := map[string]int{
    "key": 42,
}
```

### Fix 3: Initialize map fields in struct constructors

```go
// Wrong
type Config struct {
    Headers map[string]string
}

cfg := Config{}
cfg.Headers["key"] = "value" // panic

// Correct
type Config struct {
    Headers map[string]string
}

func NewConfig() *Config {
    return &Config{
        Headers: make(map[string]string),
    }
}

cfg := NewConfig()
cfg.Headers["key"] = "value"
```

### Fix 4: Check if map is nil before writing

```go
// Wrong
func setConfig(cfg map[string]string, key, value string) {
    cfg[key] = value // panic if cfg is nil
}

// Correct
func setConfig(cfg map[string]string, key, value string) {
    if cfg == nil {
        cfg = make(map[string]string)
    }
    cfg[key] = value
}
```

### Fix 5: Use a pointer to a map for optional maps

```go
// Wrong — struct with nil map field
type Response struct {
    Headers map[string]string
}

// Correct — use pointer so nil means "no headers"
type Response struct {
    Headers *map[string]string
}

func (r *Response) SetHeader(key, value string) {
    if r.Headers == nil {
        m := make(map[string]string)
        r.Headers = &m
    }
    (*r.Headers)[key] = value
}
```

## Examples

```go
// This triggers: panic: assignment to entry in nil map
package main

func main() {
    var m map[string]int
    m["answer"] = 42
}
```

## Related Errors

- [concurrent-map-write]({{< relref "/languages/go/concurrent-map-write" >}}) — writing to a map from multiple goroutines.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil pointer.
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — JSON decoding into a nil map can cause issues.
