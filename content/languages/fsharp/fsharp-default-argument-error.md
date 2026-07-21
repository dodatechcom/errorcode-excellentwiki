---
title: "[Solution] F# Default Argument Error -- Optional Parameter Issues"
description: "Fix F# default argument errors when optional parameters are not handled correctly."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Default Argument Error

This error occurs when optional parameters or default arguments are defined or called incorrectly.

## Common Causes

- F# functions do not have default parameters like C#
- Using `?` operator incorrectly for optional arguments
- Forgetting to handle None case for optional parameters
- Mixing optional and non-optional parameters incorrectly

## How to Fix

### Use Option type for optional parameters

```fsharp
// F# does not have default parameters in the C# sense
// WRONG: trying to use default parameter syntax
let fetchData (url: string) (timeout: int = 5000) = // not valid F#

// CORRECT: use Option type
let fetchData (url: string) (timeout: int option) =
    let actualTimeout = Option.defaultValue 5000 timeout
    sprintf "Fetching %s with timeout %d" url actualTimeout

// Call with or without timeout
fetchData "https://api.example.com" None
fetchData "https://api.example.com" (Some 3000)
```

### Use optional members with [<Optional>]

```fsharp
open System.Runtime.InteropServices

let process
    (name: string)
    ([<Optional; DefaultParameterValue(10)>] count: int) =
    sprintf "%s x%d" name count
```

## Examples

```fsharp
type ServiceConfig =
    { Url: string
      Timeout: int
      Retries: int }

let defaultConfig url =
    { Url = url
      Timeout = 5000
      Retries = 3 }

let withTimeout timeout config =
    { config with Timeout = timeout }
```
