---
title: "FSharp TupleDeconstructionError"
description: "Fix tuple deconstruction errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1083
---

A tuple deconstruction error occurs when pattern matching on tuples incorrectly.

## Common Causes

- Wrong number of elements in pattern
- Using wrong syntax for tuple destructuring
- Mismatched types in pattern match arms

## How to Fix

Use correct tuple patterns:

```fsharp
let (x, y) = (1, 2)  // correct deconstruction
let ((a, b), c) = ((1, 2), 3)  // nested tuples
```

Match tuples in function parameters:

```fsharp
let addPair (x, y) = x + y
let result = addPair (3, 4)
```

## Examples

```fsharp
let swap (x, y) = (y, x)
let (a, b) = swap (1, 2)  // a=2, b=1

let printPair (name, age) =
    printfn "%s is %d" name age
```

## Related Errors

- [F# PatternWildcard](/languages/fsharp/fsharp-pattern-wildcard-error)
- [F# MatchFailure](/languages/fsharp/fsharp-match-failure-error)
