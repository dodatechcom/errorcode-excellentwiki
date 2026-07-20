---
title: "FSharp PartialApplicationError"
description: "Fix partial application errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1098
---

A partial application error occurs when too few arguments are provided to a function.

## Common Causes

- Function returns another function instead of value
- Type inference issues with partial application
- Wrong argument order for partial application

## How to Fix

Provide correct number of arguments:

```fsharp
let add x y = x + y
let result = add 3 4  // 7, not a function
let add3 = add 3     // function, type: int -> int
```

Use underscore for placeholders:

```fsharp
let add = (+)
let add3 = add 3 _
```

## Examples

```fsharp
let log level msg = printfn "[%s] %s" level msg
let logError = log "ERROR"
logError "Something went wrong"

let filterBy = List.filter
let filterEvens = filterBy (fun x -> x % 2 = 0)
```

## Related Errors

- [F# FunctionCurrying](/languages/fsharp/fsharp-function-currying-error)
- [F# FunctionComposition](/languages/fsharp/fsharp-function-composition-error)
