---
title: "[Solution] F# Recursive Type Error -- Cyclical Reference Issues"
description: "Fix F# recursive type errors when types reference each other without the rec keyword."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Recursive Type Error

This error occurs when mutually referencing types that do not use the `and` or `rec` keyword for mutual recursion.

## Common Causes

- Types referencing each other without `and` keyword
- Missing `rec` on recursive type definitions
- Creating infinite types without base cases
- Using type abbreviations instead of full type definitions for recursive structures

## How to Fix

### Use and for mutual recursion

```fsharp
// WRONG: separate definitions cannot reference each other
type Tree = { Value: int; Children: NodeList }
type NodeList = { Items: Tree list }

// CORRECT: use rec and and
type Tree = { Value: int; Children: NodeList }
and NodeList = { Items: Tree list }
```

### Ensure base cases exist

```fsharp
// WRONG: infinite type with no base
type Infinite = { Inner: Infinite }

// CORRECT: add a base case
type Tree =
    | Leaf
    | Node of Tree * Tree
```

## Examples

```fsharp
type Expression =
    | Number of float
    | Add of Expression * Expression
    | Multiply of Expression * Expression

let rec evaluate expr =
    match expr with
    | Number n -> n
    | Add (a, b) -> evaluate a + evaluate b
    | Multiply (a, b) -> evaluate a * evaluate b
```
