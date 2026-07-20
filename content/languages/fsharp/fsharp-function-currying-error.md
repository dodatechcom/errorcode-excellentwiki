---
title: "FSharp FunctionCurryingError"
description: "Fix function currying errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1097
---

A function currying error occurs when multi-parameter functions are not curried correctly.

## Common Causes

- Parentheses grouping parameters incorrectly
- Missing curry/uncurry conversions
- Treated tuples as curried parameters

## How to Fix

Use multi-parameter functions:

```fsharp
let add x y = x + y  // curried by default
let addPair (x, y) = x + y  // tuple style
```

Convert between styles:

```fsharp
let curry f (a, b) = f a b
let uncurry f a b = f (a, b)
```

## Examples

```fsharp
let add x y = x + y
let add5 = add 5  // partially applied
let result = add5 3  // 8

let multiply x y = x * y
let double = multiply 2
```

## Related Errors

- [F# PartialApplication](/languages/fsharp/fsharp-partial-application-error)
- [F# FunctionComposition](/languages/fsharp/fsharp-function-composition-error)
