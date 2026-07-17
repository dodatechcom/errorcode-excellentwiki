---
title: "System.Collections.Generic.KeyNotFoundException"
description: "A KeyNotFoundException occurs when attempting to access a dictionary or map with a key that does not exist."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `KeyNotFoundException` is thrown when trying to access a value in a dictionary or map using a key that doesn't exist in the collection. In F#, this commonly occurs when using the `Item` property or the `find` function with a missing key.

## Common Causes

- Accessing a dictionary with a key that was never added
- Using `find` instead of `tryFind` when the key might not exist
- Typos in key names
- Assuming a key exists after a conditional check that may have failed

## How to Fix

```fsharp
// WRONG: Accessing missing key directly
let dict = Map.ofList [("a", 1); ("b", 2)]
let value = dict.["c"]        // KeyNotFoundException

// CORRECT: Use tryFind for safe access
let dict = Map.ofList [("a", 1); ("b", 2)]
let value = dict |> Map.tryFind "c"
match value with
| Some v -> printfn "Found: %d" v
| None -> printfn "Key not found"
```

```fsharp
// WRONG: Using find without handling missing key
let dict = Map.empty<string, int>
let value = Map.find "key" dict  // raises KeyNotFoundException

// CORRECT: Use find with a default or tryFind
let dict = Map.empty<string, int>
let value = dict |> Map.tryFind "key" |> Option.defaultValue 0
```

## Examples

```fsharp
// Example 1: Dictionary access
open System.Collections.Generic
let dict = Dictionary<string, int>()
dict.Add("x", 10)
let v = dict.["y"]           // KeyNotFoundException: The given key 'y' was not present

// Example 2: Map with wrong key
let ages = Map [("Alice", 30); ("Bob", 25)]
let age = ages.["Charlie"]   // KeyNotFoundException

// Example 3: Missing key after conditional
let config = Map [("debug", true)]
if config.["verbose"] then   // KeyNotFoundException
    printfn "Verbose mode"
```

## Related Errors

- [NullReferenceException](/languages/fsharp/null-reference)
