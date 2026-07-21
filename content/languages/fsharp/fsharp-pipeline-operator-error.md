---
title: "[Solution] F# Pipeline Operator Error -- Incorrect Composition"
description: "Fix F# pipeline operator errors when the |> operator is misused or arguments do not align."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Pipeline Operator Error

This error occurs when the pipe operator `|>` is used incorrectly, such as piping a value into a function that expects different arguments.

## Common Causes

- Piping into a function expecting multiple curried arguments incorrectly
- Forgetting that pipe inserts as the last argument
- Using pipe with functions that return partial applications
- Mixing up `<|` and `|>`

## How to Fix

### Understand pipe argument position

```fsharp
// WRONG: pipe puts list as second argument to Map
let result = [1;2;3] |> Map.add "key"

// CORRECT: pipe puts value as LAST argument
let result = [1;2;3] |> Map.ofList
```

### Use parentheses for clarity

```fsharp
// WRONG: ambiguous composition
let result = [1;2;3] |> List.map (fun x -> x * 2) |> List.filter (fun x -> x > 2)

// CORRECT: chain cleanly with clear steps
let result =
    [1; 2; 3]
    |> List.map (fun x -> x * 2)
    |> List.filter (fun x -> x > 2)
```

## Examples

```fsharp
let processWords (text: string) =
    text
    |> fun s -> s.Split(' ')
    |> Array.map (fun w -> w.ToLower())
    |> Array.filter (fun w -> w.Length > 3)
    |> Array.sort
```
