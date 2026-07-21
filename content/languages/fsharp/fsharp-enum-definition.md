---
title: "[Solution] F# Enum Definition Error -- Fixing DU and Enum Types"
description: "Fix F# enum definition errors when discriminated unions or CLI enums are incorrectly defined."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Enum Definition Error

This error occurs when enum or discriminated union types are defined incorrectly, such as using invalid values or duplicate cases.

## Common Causes

- Duplicate case names in a discriminated union
- Invalid values in [<Flags>] enum definitions
- Using non-constant values for enum members
- Missing [<CLIEvent>] on interface events

## How to Fix

### Use unique case names

```fsharp
// WRONG: duplicate case names
type Color =
    | Red
    | Red  // duplicate

// CORRECT: unique names
type Color =
    | Red
    | DarkRed
    | LightRed
```

### Define Flags enums correctly

```fsharp
// WRONG: overlapping flags values
[<Flags>]
type Permissions =
    | Read = 1
    | Write = 1  // overlaps with Read
    | Execute = 4

// CORRECT: use powers of two
[<Flags>]
type Permissions =
    | Read = 1
    | Write = 2
    | Execute = 4
    | All = 7
```

## Examples

```fsharp
type HttpMethod = Get | Post | Put | Delete

let toString = function
    | Get -> "GET"
    | Post -> "POST"
    | Put -> "PUT"
    | Delete -> "DELETE"
```
