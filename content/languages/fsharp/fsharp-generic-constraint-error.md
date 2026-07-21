---
title: "[Solution] F# Generic Constraint Error -- Fixing Type Parameter Constraints"
description: "Fix F# generic constraint errors when type parameters lack required constraints for member calls or operations."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Generic Constraint Error

This error occurs when a generic type parameter lacks the constraints needed to use specific operations or members.

## Common Causes

- Missing `equality` or `comparison` constraints on types used with = or <
- Using `.Length` or other members without structural constraint
- Not providing `defaultof<T>` support for nullable defaults
- Calling static members without `^T: (static member ...)`

## How to Fix

### Add where constraints

```fsharp
// WRONG: no constraint on T
let getCount (items: 'T list) =
    if items.Length > 0 then items.Length else 0

// CORRECT: explicitly constrain
let inline getCount (items: ^T list) =
    if (^T: (member Length: int) items) > 0 then
        (^T: (member Length: int) items)
    else
        0
```

### Use default constraint

```fsharp
let safeHead<'T when 'T: equality> (items: 'T list) =
    match items with
    | [] -> Unchecked.defaultof<'T>
    | x :: _ -> x
```

## Examples

```fsharp
let inline add (a: ^T) (b: ^T) : ^T =
    (^T: (static member (+): ^T * ^T -> ^T) (a, b))

let result1 = add 1 2
let result2 = add 1.5 2.5
let result3 = add "hello" " world"
```
