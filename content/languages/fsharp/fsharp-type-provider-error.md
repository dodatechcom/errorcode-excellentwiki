---
title: "[Solution] F# Type Provider Error -- Missing Generated Members"
description: "Fix F# type provider errors when generated types are not found or have incompatible signatures."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Type Provider Error

This error occurs when a type provider generates types or members that the compiler cannot find or that have incompatible signatures.

## Common Causes

- Type provider assembly not loaded or version mismatch
- Incorrect type provider configuration in the project
- Static parameter values causing code generation failures
- Network-dependent type providers failing without connectivity

## How to Fix

### Verify assembly references

```xml
<!-- WRONG: missing reference to provider assembly -->
<!-- CORRECT: include the provider package -->
<PackageReference Include="FSharp.Data" Version="*" />
```

### Check static parameters

```fsharp
// WRONG: invalid static parameter
type Csv = CsvProvider<"nonexistent.csv">

// CORRECT: use a valid resource
type Csv = CsvProvider<Sample="Name,Value\nAlice,1">
```

## Examples

```fsharp
open FSharp.Data

type CsvData = CsvProvider<Sample="Name,Age,Balance\nAlice,30,1000.50">

let processFile path =
    let data = CsvData.Load(path)
    for row in data.Rows do
        printfn "%s is %d with $%.2f" row.Name row.Age row.Balance
```
