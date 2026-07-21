---
title: "[Solution] F# Unit Return Error -- Unintended Side Effects"
description: "Fix F# unit return errors when expressions return unit instead of the expected type."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Unit Return Error

This error occurs when an expression returns `unit` in a context where a different type is expected, often caused by semicolon misuse.

## Common Causes

- Using semicolons that chain expressions, causing only the last to matter
- Placing a printfn before a return expression that then returns unit
- Forgetting to return the actual result from a function
- Misusing `ignore` when the value is needed

## How to Fix

### Avoid unnecessary semicolons

```fsharp
// WRONG: semicolon causes unit return
let compute x =
    printfn "Computing %d" x;
    x * 2  // this is not the return value -- ignored

// CORRECT: remove semicolon to use implicit return
let compute x =
    printfn "Computing %d" x
    x * 2
```

### Use ignore for intentional side effects

```fsharp
let processItems items =
    items
    |> List.iter (fun item ->
        printfn "Processing %A" item
        item.DoWork() |> ignore)
```

## Examples

```fsharp
let calculateTax income rate =
    let tax = income * rate
    printfn "Tax on %.2f is %.2f" income tax
    tax  // this line is the return value
```
