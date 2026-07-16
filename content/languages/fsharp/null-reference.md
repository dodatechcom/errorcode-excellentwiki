---
title: "NullReferenceException"
description: "A NullReferenceException occurs when attempting to access a member or method on an object reference that is null."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["null", "reference", "nulloreferenceexception"]
weight: 5
---

## What This Error Means

A `NullReferenceException` is thrown when code tries to dereference a null object reference. In F#, this typically happens when working with .NET interop code or when using option types incorrectly. F#'s type system helps prevent nulls, but they can still occur through interop or `Unchecked.defaultof`.

## Common Causes

- Forgetting to handle `None` from an option type
- Interacting with .NET libraries that return null
- Using `Option.get` on a `None` value
- Dereferencing an uninitialized mutable reference

## How to Fix

```fsharp
// WRONG: Using Option.get on None
let name: string option = None
let length = name.Value.Length    // NullReferenceException

// CORRECT: Pattern match or use default
let name: string option = None
let length =
    match name with
    | Some n -> n.Length
    | None -> 0
```

```fsharp
// WRONG: Interop with .NET returning null
open System.IO
let path: string = null
let file = File.ReadAllText(path)  // NullReferenceException

// CORRECT: Check for null before use
open System.IO
let path: string = null
if not (isNull path) then
    File.ReadAllText(path) |> ignore
else
    printfn "Path is null"
```

## Examples

```fsharp
// Example 1: Option.get failure
let x = int option None
printfn "%d" (x.Value)          // NullReferenceException

// Example 2: Null from .NET
open System
let regex = System.Text.RegularExpressions.Regex("pattern")
let input: string = null
let matches = regex.Matches(input)  // may produce null reference issues

// Example 3: Unchecked default
let arr: int array = Unchecked.defaultof<int array>
arr.Length                        // NullReferenceException
```

## How to Debug

- Use `Option.defaultValue` or pattern matching instead of `.Value`
- Add null checks when working with .NET APIs
- Enable nullable reference types in project settings
- Use `isNull` function for null checks

## Related Errors

- [KeyNotFoundException](/languages/fsharp/match-failed)
