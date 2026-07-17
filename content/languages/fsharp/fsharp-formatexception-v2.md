---
title: "[Solution] F# FormatException String Not in Correct Format"
description: "Fix F# FormatException when parsing strings to numbers, dates, or other types. Validate and sanitize input before parsing."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["format", "exception", "parsing", "string", "conversion", "fsharp"]
weight: 5
---

## What This Error Means

A `FormatException` occurs when a string cannot be parsed into the expected type, such as parsing a non-numeric string to an integer or an incorrect date format.

## Common Causes

- Parsing non-numeric string to int/double
- Incorrect date format
- Malformed input from user or external source
- Wrong culture or locale settings
- Extra whitespace in input

## How to Fix

```fsharp
// WRONG: Parsing without validation
let number = int "abc"  // FormatException

// CORRECT: Use tryParse for safe parsing
let number = 
    match System.Int32.TryParse("abc") with
    | true, n -> Some n
    | false, _ -> None
// None
```

```fsharp
// WRONG: Direct parsing of user input
let input = System.Console.ReadLine()
let age = int input  // May fail

// CORRECT: Validate first
let input = System.Console.ReadLine()
match System.Int32.TryParse(input) with
| true, age when age >= 0 && age <= 150 ->
    printfn "Age: %d" age
| _ ->
    printfn "Invalid age"
```

```fsharp
// WRONG: Date parsing without format
let date = System.DateTime.Parse("not-a-date")  // FormatException

// CORRECT: Use TryParse with culture
let mutable date = System.DateTime.MinValue
let success = System.DateTime.TryParse("2024-01-15", &date)
if success then
    printfn "%A" date
```

## Examples

```fsharp
// Example 1: Safe parsing helpers
let tryParseInt s = 
    match System.Int32.TryParse(s) with
    | true, n -> Some n
    | false, _ -> None

let tryParseFloat s =
    match System.Double.TryParse(s) with
    | true, n -> Some n
    | false, _ -> None

// Example 2: Parse with default
let parseIntDefault defaultValue s =
    match System.Int32.TryParse(s) with
    | true, n -> n
    | false, _ -> defaultValue

let value = parseIntDefault 0 "abc"  // 0

// Example 3: DateTime parsing
let parseDate s =
    match System.DateTime.TryParse(s) with
    | true, d -> Some d
    | false, _ -> None
```

## Related Errors

- [fsharp-argumentexception]({{< relref "/languages/fsharp/fsharp-argumentexception" >}}) — argument error
- [fsharp-indexoutofrange]({{< relref "/languages/fsharp/fsharp-indexoutofrange" >}}) — index out of range
- [fsharp-matcherror]({{< relref "/languages/fsharp/fsharp-matcherror" >}}) — match failure
