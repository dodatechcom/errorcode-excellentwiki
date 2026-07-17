---
title: "ArgumentException in F#"
description: "F# raises ArgumentException when a function receives an invalid argument"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `ArgumentException` is thrown when a function receives an argument that is invalid in value but valid in type. This includes `ArgumentNullException` for null values.

## Common Causes

- Null passed to non-null parameter
- Invalid argument value
- Wrong argument combination
- Out of range values

## How to Fix

Validate arguments:

```fsharp
let setAge (age: int) =
    if age < 0 || age > 150 then
        invalidArg "age" (sprintf "Invalid age: %d" age)
    age
```

Use option types:

```fsharp
let connect (host: string option) (port: int option) =
    let h = host |> Option.defaultValue "localhost"
    let p = port |> Option.defaultValue 8080
    sprintf "%s:%d" h p
```

Check for null:

```fsharp
let processString (s: string) =
    if isNull s then
        raise (System.ArgumentNullException("s"))
    s.ToUpper()
```

Use pattern matching:

```fsharp
let validateColor = function
    | "red" | "blue" | "green" -> true
    | _ -> false
```

## Examples

```fsharp
let divide a b =
    if b = 0 then invalidArg "b" "Cannot divide by zero"
    a / b

divide 10 0  // ArgumentException
```

## Related Errors

- [IndexOutOfRangeException]({{< relref "/languages/fsharp/index-out-of-range" >}})
- [MatchFailureException]({{< relref "/languages/fsharp/match-failure" >}})
