---
title: "[Solution] F# Discriminated Union Equality Error -- Comparing Union Values"
description: "Fix F# discriminated union equality errors when comparing or hashing union values incorrectly."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Discriminated Union Equality Error

This error occurs when discriminated union values are compared or used in collections that require equality or hashing.

## Common Causes

- DU types containing non-comparable fields used with Set or Map
- Missing [<CustomEquality>] when default structural equality is insufficient
- Using reference equality instead of structural equality
- Putting mutable fields in DU cases used with hash-based collections

## How to Fix

### Ensure comparable fields

```fsharp
// WRONG: float fields cause comparison issues with NaN
type Point = { X: float; Y: float }
let set = Set.ofList [{ X = 1.0; Y = 2.0 }]  // NaN issues

// CORRECT: use int or avoid NaN
type Point = { X: int; Y: int }
let set = Set.ofList [{ X = 1; Y = 2 }]
```

### Implement custom equality when needed

```fsharp
[<CustomEquality; CustomComparison>]
type CaseInsensitive =
    | CaseInsensitive of string
    override this.Equals(other) =
        match other with
        | :? CaseInsensitive as other ->
            String.equalsCaseInsensitive this.Value other.Value
        | _ -> false
    override this.GetHashCode() = this.Value.ToLower().GetHashCode()
```

## Examples

```fsharp
type Color = Red | Green | Blue

let colors = Set.ofList [Red; Green; Blue; Red]
printfn "%A" colors  // set contains Red, Green, Blue
```
