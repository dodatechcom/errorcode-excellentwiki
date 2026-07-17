---
title: "[Solution] F# KeyNotFoundException"
description: "Fix F# KeyNotFoundException when accessing dictionary keys that don't exist. Use TryGetValue or Map.tryFind."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["key", "not-found", "dictionary", "map", "lookup", "fsharp"]
weight: 5
---

## What This Error Means

A `KeyNotFoundException` occurs when you access a dictionary or map with a key that doesn't exist. This is thrown by the indexer `.[key]` on Dictionary.

## Common Causes

- Accessing non-existent key in Dictionary
- Key name typo
- Case sensitivity mismatch
- Key not added before access
- Concurrent modification

## How to Fix

```fsharp
// WRONG: Accessing non-existent key
let dict = dict [ ("a", 1); ("b", 2) ]
let value = dict.["c"]  // KeyNotFoundException

// CORRECT: Use TryGetValue or ContainsKey
let dict = dict [ ("a", 1); ("b", 2) ]
if dict.ContainsKey("c") then
    printfn "%d" dict.["c"]
else
    printfn "Key not found"
```

```fsharp
// WRONG: F# Map indexer
let map = Map [("a", 1); ("b", 2)]
let value = map.["c"]  // KeyNotFoundException

// CORRECT: Use Map.tryFind
let map = Map [("a", 1); ("b", 2)]
match Map.tryFind "c" map with
| Some v -> printfn "%d" v
| None -> printfn "Key not found"
```

```fsharp
// WRONG: Dictionary without default
let cache = System.Collections.Generic.Dictionary<string, int>()
let value = cache.["missing"]  // KeyNotFoundException

// CORRECT: Check or provide default
let mutable value = 0
if cache.TryGetValue("missing", &value) then
    printfn "%d" value
else
    printfn "Not in cache"
```

## Examples

```fsharp
// Example 1: Safe dictionary access
let safeGet key (dict: System.Collections.Generic.IDictionary<_, _>) =
    match dict.TryGetValue(key) with
    | true, value -> Some value
    | false, _ -> None

// Example 2: F# Map with default
let mapWithDefault = Map [("a", 1)] |> Map.add "b" 2
let value = mapWithDefault |> Map.tryFind "c" |> Option.defaultValue 0

// Example 3: Dictionary with default value
let getOrDefault key defaultValue (dict: Map<_, _>) =
    dict |> Map.tryFind key |> Option.defaultValue defaultValue
```

## Related Errors

- [fsharp-indexoutofrange]({{< relref "/languages/fsharp/fsharp-indexoutofrange" >}}) — index out of range
- [fsharp-matcherror]({{< relref "/languages/fsharp/fsharp-matcherror" >}}) — match failure
- [fsharp-nullreference]({{< relref "/languages/fsharp/fsharp-nullreference" >}}) — null reference
