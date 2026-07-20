---
title: "FSharp ResolveTypeError"
description: "Fix type resolution errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1119
---

A type resolution error occurs when the compiler cannot resolve ambiguous types.

## Common Causes

- Ambiguous type from multiple open statements
- Generic type with conflicting constraints
- Missing type annotation causing ambiguity

## How to Fix

Add explicit type annotations:

```fsharp
let processItem (item: string) : int = item.Length
```

Use qualified type names:

```fsharp
let result : System.Collections.Generic.List<int> =
    System.Collections.Generic.List<int>()
```

## Examples

```fsharp
let parseNumber (input: string) : int =
    match System.Int32.TryParse(input) with
    | true, n -> n
    | _ -> 0
```

## Related Errors

- [F# OverloadResolution](/languages/fsharp/fsharp-overload-resolution-error)
- [F# LetBinding](/languages/fsharp/fsharp-let-binding-type-inference)
