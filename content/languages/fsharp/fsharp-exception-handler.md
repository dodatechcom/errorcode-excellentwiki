---
title: "[Solution] F# Exception Handler Error -- Fixing Try-With Patterns"
description: "Fix F# exception handler errors when try-with blocks are malformed or catch the wrong exception types."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Exception Handler Error

This error arises when try-with or try-finally blocks are incorrectly structured or reference exception types that do not exist.

## Common Causes

- Missing exception handler after try keyword
- Catching non-existent exception types
- Using multiple when guards without proper binding
- Neglecting to re-raise caught exceptions when needed

## How to Fix

### Catch specific exceptions

```fsharp
// WRONG: catching string instead of exception type
try
    File.ReadAllText("missing.txt")
with
| Failure msg -> printfn "Failed: %s" msg

// CORRECT: use System.IO.FileNotFoundException
try
    File.ReadAllText("missing.txt")
with
| :? System.IO.FileNotFoundException as ex ->
    printfn "File not found: %s" ex.Message
```

### Always provide handler or use finally

```fsharp
// WRONG: empty try block
try
    riskyOperation ()

// CORRECT: provide handler or finally
try
    riskyOperation ()
with
| ex -> printfn "Error: %s" ex.Message
```

## Examples

```fsharp
open System.IO

let safeRead path =
    try
        File.ReadAllText(path) |> Ok
    with
    | :? FileNotFoundException -> Error "File not found"
    | :? UnauthorizedAccessException -> Error "Access denied"
    | ex -> Error (sprintf "Unexpected: %s" ex.Message)
```
