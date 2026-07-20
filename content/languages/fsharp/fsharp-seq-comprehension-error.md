---
title: "FSharp SeqComprehensionError"
description: "Fix seq comprehension errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1091
---

A seq comprehension error occurs when generating sequences incorrectly.

## Common Causes

- Infinite sequences without take
- Yield vs yield! confusion
- Lazy evaluation issues

## How to Fix

Use correct seq expressions:

```fsharp
let numbers = seq {
    for i in 1..10 do
        yield i * 2
}
```

Use yield! for flattening:

```fsharp
let nested = seq {
    for i in 1..3 do
        yield! [i; i * 10]
}
```

## Examples

```fsharp
let fibonacci = seq {
    let mutable a, b = 0, 1
    while true do
        yield a
        let temp = a + b
        a <- b
        b <- temp
} |> Seq.take 10
```

## Related Errors

- [F# ListComprehension](/languages/fsharp/fsharp-list-comprehension-error)
- [F# QueryExpression](/languages/fsharp/fsharp-query-expression-error)
