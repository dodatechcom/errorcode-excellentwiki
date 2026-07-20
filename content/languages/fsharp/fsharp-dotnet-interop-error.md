---
title: "FSharp DotNetInteropError"
description: "Fix .NET interop errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1104
---

A .NET interop error occurs when calling .NET libraries from F# incorrectly.

## Common Causes

- Nullable reference type mismatches
- Incorrect attribute usage for .NET types
- Missing type conversions for interop

## How to Fix

Handle nullable values:

```fsharp
open System

let result =
    match box someValue with
    | null -> None
    | :? string as s -> Some s
    | _ -> None
```

Use correct attributes:

```fsharp
[<DllImport("user32.dll")>]
extern int MessageBox(IntPtr hWnd, string text, string caption, int type)
```

## Examples

```fsharp
open System.Runtime.InteropServices

[<StructLayout(LayoutKind.Sequential)>]
type Point =
    struct
        val X: float
        val Y: float
    end
```

## Related Errors

- [F# NullHandling](/languages/fsharp/fsharp-null-handling-error)
- [F# OptionBind](/languages/fsharp/fsharp-option-bind-error)
