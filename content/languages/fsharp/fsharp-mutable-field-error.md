---
title: "[Solution] F# Mutable Field Error -- Fixing Immutability Violations"
description: "Fix F# mutable field errors when trying to mutate immutable values or use mutable in incorrect contexts."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Mutable Field Error

This error occurs when you attempt to assign a new value to an immutable binding or record field.

## Common Causes

- Attempting to reassign a let binding without mutable keyword
- Modifying a record field that was not declared mutable
- Using mutable in pattern matching contexts
- Trying to mutate a function parameter

## How to Fix

### Declare bindings as mutable

```fsharp
// WRONG: immutable binding
let count = 0
count <- 1  // error

// CORRECT: mutable binding
let mutable count = 0
count <- 1
```

### Mark record fields as mutable

```fsharp
// WRONG: record fields are immutable by default
type Counter = { Count: int }
let c = { Count = 0 }
c.Count <- 1  // error

// CORRECT: mutable record field
type Counter = { mutable Count: int }
let c = { Count = 0 }
c.Count <- 1
```

## Examples

```fsharp
type Agent = {
    mutable Name: string
    mutable Active: bool
}

let agent = { Name = "worker"; Active = true }
agent.Active <- false
printfn "%s is now %b" agent.Name agent.Active
```
