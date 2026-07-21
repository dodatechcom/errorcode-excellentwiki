---
title: "[Solution] F# Object Expression Error -- Incorrect Interface Implementation"
description: "Fix F# object expression errors when creating anonymous class instances that implement interfaces."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Object Expression Error

This error occurs when object expressions (anonymous class implementations) are written incorrectly.

## Common Causes

- Missing interface name after `interface` keyword
- Not providing body for implemented members
- Using object expressions where a concrete class is needed
- Incorrectly nesting object expressions

## How to Fix

### Provide complete interface implementation

```fsharp
type ICounter =
    abstract Increment: unit -> unit
    abstract Value: int

// WRONG: missing Value member
let counter =
    { new ICounter with
        member _.Increment() = () }

// CORRECT: implement all members
let counter =
    { new ICounter with
        member _.Increment() = ()
        member _.Value = 0 }
```

### Use object expressions for callbacks

```fsharp
let comparer =
    { new System.Collections.Generic.IComparer<int> with
        member _.Compare(x, y) = y.CompareTo(x) }
```

## Examples

```fsharp
type ILogger =
    abstract Log: string -> unit

let createLogger prefix =
    { new ILogger with
        member _.Log msg = printfn "[%s] %s" prefix msg }
```
