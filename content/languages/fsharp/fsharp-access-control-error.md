---
title: "FSharp AccessControlError"
description: "Fix access control errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1101
---

An access control error occurs when accessing private or internal members incorrectly.

## Common Causes

- Trying to access private members from outside module
- Missing internal keyword for assembly-level access
- Incorrect use of private in discriminated unions

## How to Fix

Use correct access modifiers:

```fsharp
module private InternalModule =
    let helper x = x + 1

module PublicModule =
    let process x = InternalModule.helper x
```

Make types internal:

```fsharp
[<AutoOpen>]
internal module Helpers =
    let formatError msg = $"Error: {msg}"
```

## Examples

```fsharp
type Person =
    { Name: string
      mutable Age: int }
    member private this.InternalId = this.Name.GetHashCode()
    member this.DisplayName = $"{this.Name} ({this.InternalId})"
```

## Related Errors

- [F# Namespace](/languages/fsharp/fsharp-namespace-error)
- [F# Open](/languages/fsharp/fsharp-open-error)
