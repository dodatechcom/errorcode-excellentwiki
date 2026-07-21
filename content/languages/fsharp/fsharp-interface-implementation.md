---
title: "[Solution] F# Interface Implementation Error -- Fixing Missing Members"
description: "Fix F# interface implementation errors when required members are missing or have incorrect signatures."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Interface Implementation Error

This error occurs when a type declaration claims to implement an interface but does not provide all required members.

## Common Causes

- Forgetting to implement newly added interface members
- Incorrect parameter or return types on member definitions
- Using the wrong member name from the interface
- Not calling the base implementation when required

## How to Fix

### Implement all interface members

```fsharp
type ILogger =
    abstract member Log: string -> unit
    abstract member LogError: string -> unit

// WRONG: missing LogError implementation
type ConsoleLogger() =
    interface ILogger with
        member _.Log msg = printfn "%s" msg

// CORRECT: implement all members
type ConsoleLogger() =
    interface ILogger with
        member _.Log msg = printfn "%s" msg
        member _.LogError msg = eprintfn "ERROR: %s" msg
```

### Match exact signatures

```fsharp
type IProcessor =
    abstract Process: string -> int

type TextProcessor() =
    interface IProcessor with
        member _.Process(input: string) = input.Length
```

## Examples

```fsharp
type IRepository<'T> =
    abstract GetById: int -> 'T option
    abstract Save: 'T -> unit
    abstract Delete: int -> unit

type UserRepo() =
    let users = System.Collections.Generic.Dictionary<int, string>()

    interface IRepository<string> with
        member _.GetById id =
            if users.ContainsKey id then Some users.[id] else None
        member _.Save user = ()
        member _.Delete id = ()
```
