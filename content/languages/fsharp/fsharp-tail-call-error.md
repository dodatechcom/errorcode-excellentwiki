---
title: "FSharp TailCallError"
description: "Fix tail call optimization errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1103
---

A tail call error occurs when recursive functions are not properly optimized for tail calls.

## Common Causes

- Performing operations after the recursive call
- Not using tail recursive pattern with accumulator
- Stack overflow from deep recursion

## How to Fix

Use tail recursive pattern:

```fsharp
let factorial n =
    let rec loop acc n =
        if n <= 1 then acc
        else loop (acc * n) (n - 1)
    loop 1 n
```

Use continuation passing style:

```fsharp
let rec process items cont =
    match items with
    | [] -> cont []
    | x :: xs ->
        process xs (fun result ->
            cont (transform x :: result))
```

## Examples

```fsharp
let sumList lst =
    let rec loop acc = function
        | [] -> acc
        | x :: xs -> loop (acc + x) xs
    loop 0 lst
```

## Related Errors

- [F# InlineFunction](/languages/fsharp/fsharp-inline-function-error)
- [F# AsyncTimeout](/languages/fsharp/fsharp-async-timeout-error)
