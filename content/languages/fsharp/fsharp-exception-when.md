---
title: "[Solution] F# Exception in When Guard — Guard Clause Failure"
description: "Fix F# exceptions thrown in match guard clauses. Learn safe guard expressions, exception handling in patterns, and guard best practices."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An exception in a `when` guard clause occurs when the boolean expression in a pattern match guard throws an exception. The guard expression is evaluated at runtime when the pattern structurally matches, and if the expression fails, the exception propagates rather than trying the next case.

## Why It Happens

The most common cause is calling a function in a guard that can throw. For example, `when List.length list > 0` is safe, but `when list |> List.head > 5` will throw if the list is empty because `List.head` is called before the comparison.

Another frequent cause is accessing properties or methods that may be null or throw. If a guard expression calls `someObject.Value` where `someObject` is `None`, the `.Value` call throws `ArgumentException`.

Database queries or network calls in guard expressions are dangerous because they can fail for many reasons (timeout, connection lost, data corruption).

Side effects in guards are particularly problematic because the guard may be evaluated multiple times if multiple patterns are tried, causing unexpected repeated execution.

Finally, division or modulo operations in guards can throw `DivideByZeroException` if the divisor is zero.

## How to Fix It

### Keep guard expressions simple and side-effect free

```fsharp
// Wrong — may throw if list is empty
match myList with
| head :: _ when myList |> List.head > 5 -> "large"

// Correct — use pattern matching to bind first
match myList with
| head :: _ when head > 5 -> "large"
| _                       -> "other"
```

### Use try-with inside guards when needed

```fsharp
match value with
| x when (try riskyCheck x with _ -> false) -> "passed"
| _                                          -> "failed"
```

### Move complex logic outside the match

```fsharp
let isValid = try checkValue value with _ -> false

match value with
| x when isValid -> process x
| _               -> defaultResult
```

### Use Option-based checks in guards

```fsharp
match item with
| Some x when x |> Option.isSome -> "has value"
| _                               -> "no value"
```

### Validate before the match expression

```fsharp
let validatedItems =
    items
    |> List.filter (fun item ->
        try validate item
        with _ -> false)

match validatedItems with
| valid :: _ -> process valid
| []         -> handleInvalid ()
```

## Common Mistakes

- Putting expensive or failing operations inside guard expressions
- Using `.Value` on Option types in guards without null checking
- Performing I/O operations in guard clauses
- Not accounting for side effects being evaluated multiple times
- Assuming guards are only evaluated once per match expression

## Related Pages

- [F# MatchFailureException](/languages/fsharp/fsharp-match-failure/)
- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# ArgumentException](/languages/fsharp/fsharp-argument-exception/)
