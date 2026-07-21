---
title: "[Solution] F# Module AutoOpen Error -- Unexpected Name Resolution"
description: "Fix F# module auto-open errors when modules marked with AutoOpen cause unexpected name resolution."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["warning"]
---

# F# Module AutoOpen Error

This error occurs when modules decorated with `[<AutoOpen>]` introduce unexpected names into scope, causing ambiguity or hiding intended identifiers.

## Common Causes

- Auto-opened module names shadowing user-defined identifiers
- Multiple auto-opened modules with conflicting names
- Auto-opened namespace bringing unintended types into scope
- Inherited auto-open from referenced NuGet packages

## How to Fix

### Avoid name collisions

```fsharp
// WRONG: auto-opened module hides your function
[<AutoOpen>]
module Helpers =
    let sum items = List.sum items  // name collision

// In your code
let sum = [1; 2; 3] |> Helpers.sum  // ambiguous

// CORRECT: use distinct names or qualified access
[<AutoOpen>]
module StringHelpers =
    let joinWords (words: string list) = String.concat " " words
```

### Check what is auto-opened

```fsharp
// Use fully qualified names to avoid auto-open conflicts
let mySum = FSharp.Collections.List.sum
```

## Examples

```fsharp
[<AutoOpen>]
module AppDefaults =
    let defaultTimeout = 5000
    let defaultRetries = 3

// Now defaultTimeout and defaultRetries are available everywhere
let config = { Timeout = defaultTimeout }
```
