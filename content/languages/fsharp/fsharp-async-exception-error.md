---
title: "[Solution] F# Async Exception Error -- Unhandled Async Exceptions"
description: "Fix F# async exception errors when exceptions in async workflows are not properly caught."
languages: ["fsharp"]
error-types: ["runtime"]
severities: ["error"]
---

# F# Async Exception Error

This error occurs when exceptions thrown inside async computation expressions are not caught, leading to silent failures or unhandled exceptions.

## Common Causes

- Exceptions in async blocks not wrapped in try-with
- Using Async.Start without checking for faults
- Child async workflows throwing exceptions that propagate unexpectedly
- Missing error handling in parallel async sequences

## How to Fix

### Wrap async operations with try-with

```fsharp
// WRONG: no error handling
let fetchAll urls =
    urls |> List.map (fun url ->
        async {
            let! response = Http.Get url  // exception not caught
            return response
        })

// CORRECT: handle exceptions in each async
let fetchAll urls =
    urls |> List.map (fun url ->
        async {
            try
                let! response = Http.Get url
                return Ok response
            with
            | ex -> return Error (url, ex.Message)
        })
```

### Use Async.Catch

```fsharp
let safeFetch url =
    async {
        let! result = Async.Catch(async { return! Http.Get url })
        match result with
        | Choice1Of2 value -> return value
        | Choice2Of2 ex -> return raise ex
    }
```

## Examples

```fsharp
let parallelFetch urls =
    urls
    |> List.map (fun url ->
        async {
            try
                let! data = fetchData url
                return Some data
            with ex ->
                eprintfn "Failed: %s - %s" url ex.Message
                return None
        })
    |> Async.Parallel
    |> Async.RunSynchronously
```
