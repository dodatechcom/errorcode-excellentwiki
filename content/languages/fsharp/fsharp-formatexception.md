---
title: "FormatException in F#"
description: "F# raises FormatException when parsing a string into a specific type fails"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `FormatException` occurs when attempting to parse a string into a specific type (int, float, DateTime, etc.) and the string does not match the expected format.

## Common Causes

- Parsing non-numeric string as number
- Invalid date format
- Malformed input string
- Missing type conversion

## How to Fix

Use `TryParse` instead of `Parse`:

```fsharp
let tryParseInt (s: string) =
    match System.Int32.TryParse(s) with
    | true, value -> Some value
    | false, _ -> None

let result = tryParseInt "42"  // Some 42
let result = tryParseInt "abc" // None
```

Use `Option.ofTry`:

```fsharp
let parseFloat s =
    match System.Double.TryParse(s) with
    | true, v -> Some v
    | false, _ -> None
```

Validate before parsing:

```fsharp
let safeParseInt s =
    if System.Text.RegularExpressions.Regex.IsMatch(s, @"^\d+$") then
        Some (int s)
    else
        None
```

Handle date parsing:

```fsharp
let parseDate (s: string) =
    match System.DateTime.TryParse(s) with
    | true, dt -> Some dt
    | false, _ -> None
```

## Examples

```fsharp
let number = int "42"     // 42
let number = int "abc"    // FormatException
```

## Related Errors

- [ArgumentException]({{< relref "/languages/fsharp/argument-exception" >}})
- [IndexOutOfRangeException]({{< relref "/languages/fsharp/index-out-of-range" >}})
