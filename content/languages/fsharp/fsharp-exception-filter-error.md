---
title: "[Solution] F# Exception Filter Error -- When Guards on Exception Handlers"
description: "Fix F# exception filter errors when using when guards on exception matching expressions."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Exception Filter Error

This error occurs when `when` guards on exception handlers are syntactically incorrect or reference unavailable bindings.

## Common Causes

- Using when guard with exception matching that references mutable state
- Exception filter throwing its own exception
- Guard condition evaluating after the exception is caught
- Missing parentheses around complex guard expressions

## How to Fix

### Write correct exception filters

```fsharp
// WRONG: guard may throw additional exception
try
    riskyOperation ()
with
| :? IOException as ex when ex.HResult = -2146232800 ->  // HResult may not exist
    printfn "IO error"

// CORRECT: safe guard expression
try
    riskyOperation ()
with
| :? IOException as ex ->
    if ex.HResult = -2146232800 then
        printfn "File not found"
    else
        reraise()
```

### Use sequential matching

```fsharp
try
    processData ()
with
| ex when ex.Message.Contains("timeout") ->
    printfn "Timeout detected"
| :? System.TimeoutException ->
    printfn "Timeout exception"
```

## Examples

```fsharp
let safeParse (s: string) =
    try
        Some (int s)
    with
    | :? System.FormatException as ex ->
        printfn "Parse failed: %s" ex.Message
        None
    | :? System.OverflowException ->
        printfn "Number too large"
        None
```
