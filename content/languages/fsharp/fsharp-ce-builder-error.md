---
title: "[Solution] F# Computation Expression Builder Error -- Missing Methods"
description: "Fix F# computation expression builder errors when the builder does not implement required methods."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Computation Expression Builder Error

This error occurs when a custom computation expression builder is missing methods required by the constructs used within it.

## Common Causes

- Using `yield` without a Yield method on the builder
- Using `for` without For or GetEnumerator support
- Missing Combine for multi-expression blocks
- Using `do!` without a Bind that handles Async

## How to Fix

### Implement required builder methods

```fsharp
// WRONG: using yield without Yield method
type ListBuilder() =
    member _.Bind(m, f) = List.collect f m

let x = listBuilder { yield 1 }  // error

// CORRECT: implement Yield
type ListBuilder() =
    member _.Bind(m, f) = List.collect f m
    member _.Yield(x) = [x]
    member _.Zero() = []
```

### Add For support

```fsharp
type SeqBuilder() =
    member _.Yield(x) = seq { yield x }
    member _.For(items, f) = Seq.collect f items
    member _.Zero() = seq { }
```

## Examples

```fsharp
type MaybeBuilder() =
    member _.Return(x) = Some x
    member _.Bind(x, f) = Option.bind f x
    member _.Zero() = None
    member _.Combine(a, b) = Option.orElse b (Some a)
    member _.Delay(f) = f

let maybe = MaybeBuilder()
```
