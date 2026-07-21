---
title: "[Solution] F# Foreach Loop Error -- Invalid Iteration Patterns"
description: "Fix F# foreach loop errors when iterating over collections with incorrect syntax or patterns."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Foreach Loop Error

This error occurs when for-in loops are used with incorrect syntax or on non-iterable types.

## Common Causes

- Using `for x in 1..10` where `1..10` is not a valid range expression
- Iterating over types that do not implement IEnumerable
- Incorrect range syntax with step values
- Missing `do` keyword in for loop body

## How to Fix

### Use correct range syntax

```fsharp
// WRONG: incorrect step syntax
for i in 1 to 10 step 2 do  // 'step' not valid syntax

// CORRECT: use seq with yield
for i in {1..2..10} do
    printfn "%d" i

// ALTERNATIVE: use seq
for i in Seq.initInfinite (fun i -> i * 2) |> Seq.take 5 do
    printfn "%d" i
```

### Iterate over sequences

```fsharp
let items = [1; 2; 3; 4; 5]
for item in items do
    printfn "%d" item

let numbers = seq { 0 .. 2 .. 20 }
for n in numbers do
    printfn "%d" n
```

## Examples

```fsharp
let processFiles paths =
    for path in paths do
        if File.Exists path then
            let content = File.ReadAllText path
            printfn "%s: %d chars" path content.Length
```
