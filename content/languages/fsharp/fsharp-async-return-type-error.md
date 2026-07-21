---
title: "[Solution] F# Async Return Type Error -- Mismatched Async Signatures"
description: "Fix F# async return type errors when async computation expressions return incorrect types."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Async Return Type Error

This error occurs when async computation expressions return a type that does not match the declared return type.

## Common Causes

- Forgetting that async { } returns Async<'T>, not 'T
- Returning `unit` when a value is expected in async block
- Mixing synchronous return values with async bindings
- Incorrect type annotation on async-returning functions

## How to Fix

### Match async return types

```fsharp
// WRONG: returning string when Async<int> expected
let fetchData: Async<int> =
    async {
        return "hello"  // type mismatch
    }

// CORRECT: return matching type
let fetchData: Async<int> =
    async {
        let! data = getDataFromDb ()
        return data.Length
    }
```

### Use Async.AwaitTask for .NET interop

```fsharp
let fetchAsync url =
    async {
        use client = new HttpClient()
        let! response = client.GetStringAsync(url) |> Async.AwaitTask
        return response
    }
```

## Examples

```fsharp
let processUsers () =
    async {
        let! users = fetchAllUsers ()
        let count = List.length users
        return count
    }
```
