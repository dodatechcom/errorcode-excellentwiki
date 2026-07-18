---
title: "[Solution] F# Discriminated Union — Incomplete Pattern Match Error"
description: "Fix F# incomplete pattern matching on discriminated unions. Learn exhaustive matching, wildcard cases, and compiler warning handling."
languages: ["fsharp"]
error-types: ["compile-error"]
severities: ["warning"]
weight: 10
---

## What This Error Means

An incomplete pattern match warning (or runtime `MatchFailureException`) occurs when a `match` expression does not cover all cases of a discriminated union. F# issues a compile-time warning for incomplete matches, but if warnings are treated as non-fatal, the incomplete match will throw at runtime when an uncovered case is encountered.

## Why It Happens

The most common cause is adding a new case to a discriminated union without updating all match expressions that use it. For example, adding a `Pending` case to a `Status` union without handling it in every match on `Status`.

Another frequent cause is using wildcard `_` too early in a match, which catches cases that should be handled specifically. This hides the fact that important cases are being ignored.

Nested discriminated unions require matching on both the outer and inner types. If the inner union has cases that are not covered, the match is incomplete.

Guard clauses (`when`) can also mask incomplete patterns. If a guard rejects a value, the runtime tries the next case, but if there is no next case, it throws.

Finally, using `function` syntax without covering all cases creates a partial function that fails at runtime.

## How to Fix It

### Cover all discriminated union cases explicitly

```fsharp
type Status =
    | Active
    | Inactive
    | Pending

let label status =
    match status with
    | Active   -> "Active"
    | Inactive -> "Inactive"
    | Pending  -> "Pending"
```

### Use a wildcard as the last case

```fsharp
let label status =
    match status with
    | Active   -> "Active"
    | Inactive -> "Inactive"
    | other    -> sprintf "Unknown: %A" other
```

### Use the compiler warning to find missing cases

```bash
# Treat warnings as errors to catch incomplete matches
dotnet build /warnaserror
```

### Handle nested unions completely

```fsharp
type Result<'a, 'b> =
    | Ok of 'a
    | Error of 'b

type Response =
    | Success of Result<string, exn>
    | Failure of string

let describe response =
    match response with
    | Success (Ok value)      -> sprintf "Success: %s" value
    | Success (Error ex)      -> sprintf "Error: %s" ex.Message
    | Failure reason          -> sprintf "Failure: %s" reason
```

### Use `with` for additional union matching

```fsharp
let handleResult result =
    match result with
    | Ok value                      -> printfn "Got: %A" value
    | Error (:? System.TimeoutException) -> printfn "Timed out"
    | Error ex                      -> printfn "Error: %s" ex.Message
```

## Common Mistakes

- Treating F# compiler warnings about incomplete patterns as non-fatal
- Adding new union cases without updating all match expressions
- Using `_` wildcard to catch cases that should be handled specifically
- Not matching on both outer and inner types of nested discriminated unions
- Assuming the compiler will always catch incomplete matches (it does not for all cases)

## Related Pages

- [F# MatchFailureException](/languages/fsharp/fsharp-match-failure/)
- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# InvalidOperation](/languages/fsharp/fsharp-invalidoperation/)
