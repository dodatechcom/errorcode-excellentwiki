---
title: "FSharp OpenError"
description: "Fix open statement errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1100
---

An open error occurs when opening namespaces or modules incorrectly.

## Common Causes

- Opening non-existent namespace
- Circular dependencies from open statements
- Ambiguous names after opening multiple modules

## How to Fix

Open namespaces at the top:

```fsharp
open System
open System.Collections.Generic

let dict = Dictionary<string, int>()
```

Use qualified names when ambiguous:

```fsharp
open ModuleA
open ModuleB

// If both have 'process', use full path:
ModuleA.process "data"
```

## Examples

```fsharp
open System.IO
open System.Text

let readAll path =
    File.ReadAllText(path, Encoding.UTF8)
```

## Related Errors

- [F# Namespace](/languages/fsharp/fsharp-namespace-error)
- [F# AccessControl](/languages/fsharp/fsharp-access-control-error)
