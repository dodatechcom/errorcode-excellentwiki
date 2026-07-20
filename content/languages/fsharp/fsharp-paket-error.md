---
title: "FSharp PaketError"
description: "Fix Paket dependency manager errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1115
---

A Paket error occurs when dependency resolution fails or paket.dependencies is misconfigured.

## Common Causes

- Version conflicts between packages
- Missing paket.dependencies file
- Network issues during restore

## How to Fix

Configure dependencies correctly:

```
// paket.dependencies
source https://nuget.org/api/v2

framework: net6.0

nuget FSharp.Core ~> 7.0
nuget Paket
```

Run paket commands:

```bash
paket install
paket update
paket restore
```

## Examples

```
// paket.references
FSharp.Core
Paket
```

## Related Errors

- [F# FakeBuild](/languages/fsharp/fsharp-fake-build-error)
- [F# FsxScript](/languages/fsharp/fsharp-fsx-script-error)
