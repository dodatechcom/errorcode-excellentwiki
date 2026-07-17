---
title: "NullReferenceException"
description: "A NullReferenceException occurs when attempting to access a member or method on an object that is null."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `NullReferenceException` is thrown when you try to access a property, method, or field on an object reference that is null. While F# discourages null values, they can still occur when interoperating with .NET libraries or using `Unchecked.defaultof`.

## Common Causes

- Interacting with .NET libraries that return null
- Using `Option.defaultValue` incorrectly
- Forgetting to handle None cases
- Calling methods on uninitialized references

## How to Fix

```fsharp
// WRONG: Not handling null from .NET library
let name = getUserName null
printfn "%s" (name.ToUpper())  // NullReferenceException

// CORRECT: Check for null
let name = getUserName null
if obj.ReferenceEquals(name, null) then
    printfn "Name is null"
else
    printfn "%s" (name.ToUpper())
```

```fsharp
// WRONG: Using Value without checking
let opt = None
let value = opt.Value  // NullReferenceException

// CORRECT: Pattern match on Option
let opt = None
match opt with
| Some value -> printfn "%A" value
| None -> printfn "No value"
```

## Examples

```fsharp
// Example 1: Null from .NET
let list = System.Collections.Generic.List<string>()
let first = list.[0]  // NullReferenceException or IndexOutOfRangeException

// Example 2: Option.Value on None
let x : int option = None
let y = x.Value       // NullReferenceException

// Example 3: Unchecked null
let s : string = Unchecked.defaultof<_>
let len = s.Length     // NullReferenceException
```

## Related Errors

- [IndexOutOfRangeException](/languages/fsharp/index-out-of-range)
- [InvalidOperationException](/languages/fsharp/invalid-operation5)
