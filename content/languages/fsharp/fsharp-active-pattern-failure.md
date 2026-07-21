---
title: "[Solution] F# Active Pattern Failure -- Partial Pattern Matching Issues"
description: "Fix F# active pattern failures when partial patterns do not cover all cases or return incorrect results."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Active Pattern Failure

This error occurs when an active pattern function does not handle all inputs or returns incomplete results for partial patterns.

## Common Causes

- Partial active pattern missing the failure case
- Incomplete match on the results of an active pattern
- Active pattern returning wrong union case
- Nesting active patterns without handling None

## How to Fix

### Handle all cases in partial patterns

```fsharp
// WRONG: no failure case for partial active pattern
let (|Even|Odd|) n =
    if n % 2 = 0 then Even

// CORRECT: always provide failure case
let (|Even|Odd|) n =
    if n % 2 = 0 then Even
    else Odd
```

### Use tryParse-style patterns

```fsharp
let (|Integer|_|) str =
    match System.Int32.TryParse(str) with
    | true, n -> Some n
    | false, _ -> None

match "42" with
| Integer n -> printfn "Parsed: %d" n
| _ -> printfn "Not an integer"
```

## Examples

```fsharp
let (|Lower|Upper|Mixed|) (s: string) =
    if s = s.ToLower() then Lower
    elif s = s.ToUpper() then Upper
    else Mixed

let classify word =
    match word with
    | Lower -> "lowercase"
    | Upper -> "UPPERCASE"
    | Mixed -> "MiXeD"
```
