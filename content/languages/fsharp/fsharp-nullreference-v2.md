---
title: "[Solution] F# NullReferenceException"
description: "Fix F# NullReferenceException when accessing null references. Use Option types and avoid null in F# code."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `NullReferenceException` occurs when you access a member on a null reference. Although F# discourages null, interop with C# and .NET libraries can produce null values.

## Common Causes

- Interacting with C# code that returns null
- Uninitialized mutable references
- Using `Unchecked.defaultof` 
- Not handling null from .NET library calls
- Database returning null

## How to Fix

```fsharp
// WRONG: Accessing potentially null value
let name: string = getFromCSharp()
printfn "%d" name.Length  // NullReferenceException if null

// CORRECT: Check for null using Option
let name: string = getFromCSharp()
if System.Object.ReferenceEquals(name, null) then
    printfn "Name is null"
else
    printfn "%d" name.Length
```

```fsharp
// WRONG: Using mutable without init
let mutable myValue: string = Unchecked.defaultof<_>
printfn "%s" myValue  // NullReferenceException

// CORRECT: Use Option type
let myValue: string option = None
match myValue with
| Some v -> printfn "%s" v
| None -> printfn "No value"
```

```fsharp
// WRONG: C# interop returning null
let list = new System.Collections.Generic.List<string>()
let item = list.[0]  // May be null if list uses nullable

// CORRECT: Use Option.ofObj
let itemOpt = list.[0] |> Option.ofObj
match itemOpt with
| Some item -> printfn "%s" item
| None -> printfn "Item is null"
```

## Examples

```fsharp
// Example 1: Option.ofObj for null-safe conversion
let safeName = Option.ofObj (getFromCSharp())
printfn "%A" safeName  // Some "Alice" or None

// Example 2: Null attribute for C# interop
[<AllowNullLiteral>]
type MyClass() =
    member val Name = "" with get, set

// Example 3: DefaultArg for null handling
let name = DefaultArg (Option.ofObj nameFromCSharp) "Anonymous"
printfn "%s" name
```

## Related Errors

- [fsharp-matcherror]({{< relref "/languages/fsharp/fsharp-matcherror" >}}) — match failure
- [fsharp-notfoundexception]({{< relref "/languages/fsharp/fsharp-notfoundexception" >}}) — key not found
- [fsharp-argumentexception]({{< relref "/languages/fsharp/fsharp-argumentexception" >}}) — argument error
