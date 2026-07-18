---
title: "[Solution] F# NullReferenceException — Null Access in F# Code"
description: "Fix F# NullReferenceException when accessing null values. Learn Option types, null checking, and why null is dangerous in F#."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `NullReferenceException` is thrown when you try to access a member or method on a null reference. In F#, null is technically allowed for reference types (especially when interoping with .NET libraries), but it is not idiomatic and leads to this error.

## Why It Happens

The most common cause is receiving null from a .NET library or API that does not use F#'s `Option` type. For example, `Dictionary.TryGetValue` returns a tuple, but `Dictionary.[key]` throws `KeyNotFoundException` (not null), while `Dictionary.tryGetValue` returns an `Option`.

Another frequent cause is using `Unchecked.defaultof<'T>` which returns null for reference types. If this value is used without checking, accessing its members throws.

Record types and discriminated unions in F# can be null if they are declared with `[<AllowNullLiteral>]`. This attribute allows null values, which breaks the assumption that F# types are never null.

Database queries and HTTP responses that return null values from C# code are another common source. When these values are passed directly into F# functions without null checking, the null reference causes an error.

Finally, mutable fields that have not been initialized default to null for reference types. Accessing these fields before assignment throws this exception.

## How to Fix It

### Use Option for nullable values

```fsharp
let findUser id =
    match database.TryFindUser(id) with
    | null  -> None
    | user  -> Some user

// Use with pattern matching
match findUser 42 with
| Some user -> printfn "Found: %s" user.Name
| None      -> printfn "User not found"
```

### Check for null explicitly when needed

```fsharp
let processValue (value: obj) =
    if obj.ReferenceEquals(value, null) then
        printfn "Value is null"
    else
        printfn "Value: %A" value
```

### Use Option.ofObj for safe conversion

```fsharp
let maybeUser = Option.ofObj possiblyNullUser
match maybeUser with
| Some user -> user.Name
| None      -> "Unknown"
```

### Avoid AllowNullLiteral when possible

```fsharp
// Wrong — allows null values
[<AllowNullLiteral>]
type User() =
    member val Name = "" with get, set

// Correct — use Option instead
type User = {
    Name: string
    Email: string option
}
```

### Use nullArg for argument validation

```fsharp
let processName (name: string) =
    nullArg (nameof name) if name |> isNull
    name.ToUpper()
```

## Common Mistakes

- Using `[<AllowNullLiteral>]` on types that should never be null
- Not converting .NET null returns to F# Option types
- Using `defaultof<T>` without null checking
- Comparing with `= null` instead of `isNull` function
- Passing null values through F# pipelines without interception

## Related Pages

- [F# MatchFailureException](/languages/fsharp/fsharp-match-failure/)
- [F# InvalidOperation](/languages/fsharp/fsharp-invalidoperation/)
- [F# TypeInitializationException](/languages/fsharp/fsharp-type-init-error/)
