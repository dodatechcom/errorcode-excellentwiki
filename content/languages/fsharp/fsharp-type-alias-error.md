---
title: "[Solution] F# Type Alias Error -- Invalid Type Abbreviations"
description: "Fix F# type alias errors when creating invalid or circular type abbreviations."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Type Alias Error

This error occurs when type aliases are defined incorrectly or create circular references.

## Common Causes

- Circular type aliases where A = B and B = A
- Aliasing generic types without proper parameter lists
- Using type aliases with incompatible generic arities
- Attempting to alias erased types from type providers

## How to Fix

### Avoid circular references

```fsharp
// WRONG: circular alias
type A = B
type B = A  // error: circular reference

// CORRECT: use a record or class instead
type A = { Value: B option }
and B = { Name: string; Ref: A option }
```

### Use correct generic syntax

```fsharp
// WRONG: missing type parameter
type IntList = list  // error: needs <int>

// CORRECT: specify parameters
type IntList = list<int>
type StringMap = Map<string, int>
```

## Examples

```fsharp
type Handler = string -> Async<unit>
type Middleware = Handler -> Handler
type Pipeline = Middleware list

let run (pipeline: Pipeline) (handler: Handler) =
    List.foldBack (fun m h -> m h) pipeline handler
```
