---
title: "[Solution] F# Type Abbreviation Error -- Generic Alias Mismatch"
description: "Fix F# type abbreviation errors when generic type aliases have incorrect parameter counts."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Type Abbreviation Error

This error occurs when a type abbreviation uses the wrong number of type parameters compared to its definition.

## Common Causes

- Declaring a type alias with 2 parameters but using it with 1
- Forgetting type parameters entirely on generic aliases
- Using abbreviated type with wrong generic arity
- Mixing up covariant and contravariant type parameters

## How to Fix

### Match parameter counts

```fsharp
// WRONG: type alias has 2 params, used with 1
type Result<'T, 'E> = Ok of 'T | Error of 'E
type IntResult = Result<int>  // error: needs 2 params

// CORRECT: fix the alias
type IntResult = Result<int, string>
```

### Use correct generic syntax

```fsharp
type Handler<'Input, 'Output> = 'Input -> Async<'Output>
type HttpHandler = Handler<string, string>  // correct usage
```

## Examples

```fsharp
type KeyValue<'K, 'V> = { Key: 'K; Value: 'V }
type IntEntry = KeyValue<int, string>

let entry = { Key = 1; Value = "first" }
```
