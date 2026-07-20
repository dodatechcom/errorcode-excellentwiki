---
title: "FSharp ListComprehensionError"
description: "Fix list comprehension errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1092
---

A list comprehension error occurs when creating lists using computation expressions incorrectly.

## Common Causes

- Missing yield in list expressions
- Incorrect list syntax
- Type mismatches in list elements

## How to Fix

Use correct list expression syntax:

```fsharp
let squares = [ for i in 1..10 -> i * i ]
let evens = [ for i in 1..20 if i % 2 = 0 -> i ]
```

Combine lists:

```fsharp
let combined = [1; 2; 3] @ [4; 5; 6]
let nested = [ for x in 1..3 do yield! [x; x*2] ]
```

## Examples

```fsharp
let matrix = [
    for i in 1..3 do
        for j in 1..3 do
            yield (i, j, i * j)
]
```

## Related Errors

- [F# SeqComprehension](/languages/fsharp/fsharp-seq-comprehension-error)
- [F# TypeError](/languages/fsharp/fsharp-type-inference-error)
