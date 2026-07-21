---
title: "[Solution] F# Exception Reraise Error -- Losing Stack Trace"
description: "Fix F# exception re-raise errors when catching and rethrowing exceptions loses the original stack trace."
languages: ["fsharp"]
error-types: ["runtime"]
severities: ["warning"]
---

# F# Exception Re-raise Error

This error occurs when exceptions are caught and re-thrown incorrectly, losing the original stack trace information.

## Common Causes

- Using `raise ex` instead of `reraise()` which resets the stack trace
- Catching and creating a new exception from the caught one
- Logging and rethrowing with a wrapper that obscures the original type
- Using `raise (exn(...))` instead of preserving the original

## How to Fix

### Use reraise() in catch blocks

```fsharp
// WRONG: loses stack trace
try
    riskyOperation ()
with
| ex ->
    logError ex.Message
    raise ex  // stack trace starts here

// CORRECT: use reraise()
try
    riskyOperation ()
with
| ex ->
    logError ex.Message
    reraise()  // preserves original stack trace
```

### Wrap with ExceptionDispatchInfo

```fsharp
open System.Runtime.ExceptionServices

try
    riskyOperation ()
with
| ex ->
    logError ex.Message
    ExceptionDispatchInfo.Capture(ex).Throw()
```

## Examples

```fsharp
let safeOperation path =
    try
        File.ReadAllText(path) |> Ok
    with
    | :? FileNotFoundException as ex ->
        logWarning "File missing: %s" path
        reraise()
    | ex ->
        logError "Unexpected error: %s" ex.Message
        Error ex.Message
```
