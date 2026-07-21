---
title: "[Solution] F# Attribute Error -- Incorrect Attribute Usage"
description: "Fix F# attribute errors when custom or built-in attributes are applied incorrectly."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Attribute Error

This error occurs when attributes are applied to incompatible code elements or have invalid constructor arguments.

## Common Causes

- Applying an attribute to a code element it does not support
- Missing required constructor arguments on an attribute
- Using obsolete attributes without checking their signature
- Placing attributes in the wrong position relative to the declaration

## How to Fix

### Check attribute target

```fsharp
// WRONG: [<Obsolete>] applied to a field
[<Obsolete>]
type Config = { Field: string }

// CORRECT: apply to individual members
type Config = {
    [<Obsolete("Use NewField instead")>]
    Field: string
    NewField: string
}
```

### Provide required arguments

```fsharp
// WRONG: missing required argument
[<StructLayout>]  // may need LayoutKind
type Point = { X: float; Y: float }

// CORRECT: provide LayoutKind
[<StructLayout(LayoutKind.Sequential)>]
type Point = { X: float; Y: float }
```

## Examples

```fsharp
[<RequireQualifiedAccess>]
type Color =
    | Red
    | Green
    | Blue

// Must use Color.Red, not just Red
let c = Color.Red
```
