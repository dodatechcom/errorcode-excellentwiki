---
title: "FSharp NamespaceError"
description: "Fix namespace errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1099
---

A namespace error occurs when F# namespaces are used incorrectly.

## Common Causes

- Duplicate namespace declarations
- Missing namespace qualification
- Circular namespace references

## How to Fix

Declare namespaces correctly:

```fsharp
namespace MyApp.Models

type Person = { Name: string; Age: int }
```

Use module within namespace:

```fsharp
namespace MyApp.Utils

module StringHelper =
    let capitalize (s: string) =
        s.[0].ToString().ToUpper() + s.[1..]
```

## Examples

```fsharp
namespace MyApp.Services

open MyApp.Models

type UserService() =
    member _.GetUser id = { Name = "Alice"; Age = 30 }
```

## Related Errors

- [F# Open](/languages/fsharp/fsharp-open-error)
- [F# AccessControl](/languages/fsharp/fsharp-access-control-error)
