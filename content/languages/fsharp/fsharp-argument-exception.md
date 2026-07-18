---
title: "[Solution] F# ArgumentException — Invalid Argument Passed to Function"
description: "Fix F# ArgumentException for invalid or null arguments. Learn argument validation with nullArg, raise, and precondition checks."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `ArgumentException` is thrown when a function receives an argument that does not meet its requirements. The base `ArgumentException` indicates the argument is invalid, while derived types like `ArgumentNullException` and `ArgumentOutOfRangeException` provide more specific information.

## Why It Happens

The most common cause is passing a null value to a function that does not accept null. In F#, many functions use `nullArg` to explicitly check for null and throw `ArgumentNullException` with a descriptive message.

Another frequent cause is passing a value outside the allowed range. For example, passing a negative number to an array index or a percentage value greater than 100.

Wrong argument types are another source. If a function expects a specific type and receives a different type, the CLR throws `ArgumentException`. This is common with .NET library interop where type safety is enforced at runtime.

Missing required arguments in F# are handled differently from C#. F# functions use currying rather than optional parameters, so a missing argument is typically a type error at compile time. However, calling .NET methods with missing required parameters can throw this exception.

Finally, invariant violations in constructors (like passing an empty string for a required name) are often validated with `ArgumentException`.

## How to Fix It

### Validate arguments with nullArg

```fsharp
let processName (name: string) =
    nullArg (nameof name) if isNull name
    name.ToUpper()
```

### Check argument ranges explicitly

```fsharp
let getElement index (arr: 'a array) =
    if index < 0 || index >= arr.Length then
        invalidArg (nameof index) (sprintf "Index %d out of range [0, %d)" index arr.Length)
    arr.[index]
```

### Use when guards for argument validation

```fsharp
let setPercentage (value: float) =
    if value < 0.0 || value > 100.0 then
        invalidArg (nameof value) (sprintf "Percentage must be between 0 and 100, got %f" value)
    value / 100.0
```

### Validate custom types in constructors

```fsharp
type PositiveInteger private (value: int) =
    do
        if value <= 0 then
            invalidArg (nameof value) "Value must be positive"
    static member Create(value: int) = PositiveInteger(value)
    member _.Value = value
```

### Use Result type for validation instead of exceptions

```fsharp
let validateAge age =
    if age < 0 || age > 150 then
        Error "Age must be between 0 and 150"
    else
        Ok age

match validateAge -5 with
| Ok validAge    -> printfn "Valid age: %d" validAge
| Error msg      -> printfn "Invalid: %s" msg
```

## Common Mistakes

- Not validating arguments at public API boundaries
- Using generic `ArgumentException` instead of `ArgumentNullException` for null values
- Throwing exceptions for validation that could use the `Result` type
- Forgetting that F# functions are curried, so partial application can leave arguments unchecked
- Not providing descriptive error messages when validating arguments

## Related Pages

- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# IndexOutOfRangeException](/languages/fsharp/fsharp-indexoutofrange/)
- [F# FormatException](/languages/fsharp/fsharp-formatexception/)
