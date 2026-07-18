---
title: "[Solution] F# Active Pattern — Partial Function Error"
description: "Fix F# active pattern partial function errors. Learn partial active patterns, complete active patterns, and pattern matching best practices."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An active pattern error occurs when a partial active pattern returns `None` and there is no fallback case in the match expression. Partial active patterns are designed to classify some values but not others, and when no case matches, a `MatchFailureException` is thrown.

## Why It Happens

The most common cause is using a partial active pattern without a wildcard case. Partial active patterns (those returning `option` or using `| Pattern | _ ->`) only match values they recognize, and unmatched values must be handled by a default case.

Another frequent cause is an active pattern that throws an exception during classification. If the pattern's implementation calls a function that fails (like parsing or division), the exception propagates instead of returning `None`.

Parameterized active patterns with invalid parameters can cause unexpected behavior. If the parameter changes the classification logic, some values that were previously matched may no longer match.

Active patterns with overlapping cases can cause ambiguity. If two patterns match the same value, the first one wins, which may not be the intended behavior.

Finally, recursive active patterns that do not terminate cause stack overflow errors during pattern matching.

## How to Fix It

### Always include a wildcard case for partial patterns

```fsharp
let (|Even|Odd|) n =
    if n % 2 = 0 then Even else Odd

match number with
| Even -> "even"
| Odd  -> "odd"
// Always safe because the pattern is complete
```

### Handle None returns from partial patterns

```fsharp
let (|ParseInt|_|) (s: string) =
    match System.Int32.TryParse(s) with
    | true, v -> Some v
    | false, _ -> None

match input with
| ParseInt n -> printfn "Number: %d" n
| _          -> printfn "Not a number"
```

### Use try-with in active pattern implementations

```fsharp
let (|SafeDivide|_|) (a, b) =
    try
        Some (a / b)
    with
    | :? System.DivideByZeroException -> None

match (10, 0) with
| SafeDivide result -> printfn "Result: %d" result
| _                 -> printfn "Cannot divide"
```

### Make active patterns idempotent and side-effect free

```fsharp
// Wrong — side effects in active pattern
let mutable counter = 0
let (|Counted|_|) x =
    counter <- counter + 1
    Some x

// Correct — pure function
let (|Positive|_|) x =
    if x > 0 then Some x else None
```

### Use parameterized active patterns carefully

```fsharp
let (|Range|_|) (min, max) x =
    if x >= min && x <= max then Some x else None

match age with
| Range (0, 12) child   -> "Child"
| Range (13, 17) teen   -> "Teenager"
| Range (18, 65) adult  -> "Adult"
| _                      -> "Senior"
```

## Common Mistakes

- Using partial active patterns without a wildcard fallback case
- Putting side effects or I/O operations in active pattern implementations
- Creating overlapping patterns that cause ambiguous matches
- Not handling exceptions thrown inside active pattern logic
- Using active patterns where a simple function or guard would be clearer

## Related Pages

- [F# MatchFailureException](/languages/fsharp/fsharp-match-failure/)
- [F# Discriminated Union Error](/languages/fsharp/fsharp-discriminated-union/)
- [F# Exception in When Guard](/languages/fsharp/fsharp-exception-when/)
