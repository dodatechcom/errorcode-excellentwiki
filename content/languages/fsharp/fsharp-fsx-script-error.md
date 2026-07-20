---
title: "FSharp FsxScriptError"
description: "Fix F# script file (.fsx) errors."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1116
---

An F# script error occurs when running .fsx script files with incorrect syntax or references.

## Common Causes

- Missing #r references to assemblies
- Incorrect #load directives
- Script-specific syntax not valid in compiled code

## How to Fix

Add correct references:

```fsharp
#r "nuget: Newtonsoft.Json, 13.0.3"
#r "system.net.http"

open Newtonsoft.Json

let data = {| Name = "Alice"; Age = 30 |}
let json = JsonConvert.SerializeObject(data)
```

Use #load for local files:

```fsharp
#load "helpers.fs"
open Helpers
```

## Examples

```fsharp
#r "nuget: FSharp.Data"

open FSharp.Data

type Csv = CsvProvider<"data.csv">
let data = Csv.Load("data.csv")
```

## Related Errors

- [F# FakeBuild](/languages/fsharp/fsharp-fake-build-error)
- [F# Namespace](/languages/fsharp/fsharp-namespace-error)
