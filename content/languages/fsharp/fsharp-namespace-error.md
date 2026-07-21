---
title: "[Solution] F# Namespace Error -- Invalid Module Structure"
description: "Fix F# namespace errors when module and namespace declarations are incorrect or conflicting."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Namespace Error

This error occurs when namespace and module declarations conflict or are structured incorrectly in F# source files.

## Common Causes

- Declaring a module and namespace with conflicting names in the same file
- Using `module` declaration at the top of a file that already has a namespace
- Mismatched namespace hierarchy between files
- Missing required namespace declarations for type providers

## How to Fix

### Use correct file structure

```fsharp
// WRONG: module after namespace
namespace MyApp.Utilities
module MyApp.Utilities.StringHelper =  // error: redefining namespace

// CORRECT: single namespace with module inside
namespace MyApp.Utilities

module StringHelper =
    let capitalize (s: string) =
        s.[0].ToString().ToUpper() + s.[1..]
```

### Separate files with namespaces

```fsharp
// File1.fs
namespace MyApp.Models
type User = { Name: string; Age: int }

// File2.fs
namespace MyApp.Services
open MyApp.Models
let greet (user: User) = sprintf "Hello %s" user.Name
```

## Examples

```fsharp
namespace MyApp.Core

[<AutoOpen>]
module Utilities =
    let inline clamp min max value =
        if value < min then min
        elif value > max then max
        else value
```
