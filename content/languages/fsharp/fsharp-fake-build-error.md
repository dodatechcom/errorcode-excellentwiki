---
title: "FSharp FakeBuildError"
description: "Fix FAKE build script errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1114
---

A FAKE build error occurs when build scripts have incorrect syntax or missing dependencies.

## Common Causes

- Missing NuGet packages in build script
- Incorrect target dependencies
- Wrong FAKE version

## How to Fix

Reference packages correctly:

```fsharp
#r "paket: groupref build //"
#load ".fake/build.fsx/paket.load"

open Fake.Core
open Fake.DotNet
open Fake.IO

Target.create "Build" (fun _ ->
    DotNet.build id "src/MyApp"
)

Target.create "Test" (fun _ ->
    DotNet.test id "tests/MyApp.Tests"
)

open Fake.Core.TargetOperators
"Build" ==> "Test" ==> "Default"

Target.runOrDefault "Default"
```

## Examples

```fsharp
Target.create "Clean" (fun _ ->
    Shell.cleanDir "bin"
    Shell.cleanDir "obj"
)

Target.create "Build" (fun _ ->
    DotNet.build id "src/MyApp"
)
```

## Related Errors

- [F# Paket](/languages/fsharp/fsharp-paket-error)
- [F# FsxScript](/languages/fsharp/fsharp-fsx-script-error)
