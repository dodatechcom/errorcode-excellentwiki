---
title: "[Solution] F# Module Access Error -- Fixing Scope and Visibility"
description: "Fix F# module access errors when identifiers are not visible due to private scope or missing open statements."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Module Access Error

This error occurs when you try to access a value, function, or type that is not visible in the current scope.

## Common Causes

- Missing `open` statement for a required module
- Accessing private members from outside their module
- Incorrect fully qualified path to a type
- Using auto-open modules before they are available

## How to Fix

### Open required modules

```fsharp
// WRONG: List module not in scope
let result = map (fun x -> x * 2) [1; 2; 3]

// CORRECT: open or use qualified name
let result = List.map (fun x -> x * 2) [1; 2; 3]
// or
open FSharp.Collections
let result = map (fun x -> x * 2) [1; 2; 3]
```

### Check access modifiers

```fsharp
// WRONG: accessing private function
module Internal =
    let private helper x = x + 1
    let publicResult = helper 42

// Outside Internal module
let result = Internal.helper 42  // error: not visible
```

## Examples

```fsharp
open System
open System.IO

let readConfig path =
    File.ReadAllText(path)
    |> fun content -> content.Trim()
```
