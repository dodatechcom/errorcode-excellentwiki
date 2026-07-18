---
title: "[Solution] F# FormatException — Input String Not in Correct Format"
description: "Fix F# FormatException when parsing strings to numbers or dates. Learn safe parsing with TryParse, Option types, and validation."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `FormatException` is thrown when a string is not in the format expected by a parsing method. The error message typically says "Input string was not in a correct format". This occurs with methods like `int`, `float`, `System.Int32.Parse`, and `System.DateTime.Parse` when the input string does not match the expected format.

## Why It Happens

The most common cause is calling `int "abc"` or `float "not-a-number"` without validating the input first. The `int` function in F# calls `System.Int32.Parse` under the hood, which throws `FormatException` for non-numeric strings.

Another frequent cause is parsing dates and times with locale-dependent formats. `DateTime.Parse` uses the current culture's format, which may differ from the input string's format. For example, "01/02/2024" could be January 2nd or February 1st depending on the culture.

Currency and percentage strings also cause this issue. Parsing "$100.50" with `float` fails because of the dollar sign and comma characters.

Leading or trailing whitespace in numeric strings can cause parse failures depending on the parsing method used. `int` and `float` in F# do not tolerate whitespace.

Finally, using `System.Convert.ToInt32` or similar methods with strings that contain special characters or formatting (like "1,000" with a comma) throws this exception.

## How to Fix It

### Use TryParse for safe parsing

```fsharp
let parseAge (input: string) =
    match System.Int32.TryParse(input) with
    | true, age -> Some age
    | false, _  -> None

match parseAge "25" with
| Some age -> printfn "Age: %d" age
| None     -> printfn "Invalid age"
```

### Use Option.ofTry with F# style

```fsharp
let tryParseInt (s: string) =
    let mutable result = 0
    if System.Int32.TryParse(s, &result) then Some result
    else None

let age = tryParseInt "abc" // Returns None
```

### Use invariant culture for locale-independent parsing

```fsharp
open System.Globalization

let parseDecimal (input: string) =
    let mutable result = 0.0m
    if Decimal.TryParse(input, NumberStyles.Any, CultureInfo.InvariantCulture, &result) then
        Some result
    else
        None
```

### Clean input before parsing

```fsharp
let cleanAndParse (input: string) =
    input.Trim().Replace(",", "")
    |> tryParseInt

let value = cleanAndParse " 1,000 " // Returns Some 1000
```

### Use custom format strings for dates

```fsharp
open System.Globalization

let parseDate (input: string) =
    let mutable result = DateTime.MinValue
    if DateTime.TryParseExact(input, "yyyy-MM-dd", CultureInfo.InvariantCulture, DateTimeStyles.None, &result) then
        Some result
    else
        None
```

## Common Mistakes

- Using `int` instead of `int.TryParse` for user input
- Not specifying `CultureInfo.InvariantCulture` for machine-readable data
- Forgetting that `float "1,000"` fails because of the comma
- Trimming input before parsing with methods that handle whitespace internally
- Assuming `System.Int64.Parse` handles the same formats as `System.Int32.Parse`

## Related Pages

- [F# ArgumentException](/languages/fsharp/fsharp-argument-exception/)
- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# InvalidOperation](/languages/fsharp/fsharp-invalidoperation/)
