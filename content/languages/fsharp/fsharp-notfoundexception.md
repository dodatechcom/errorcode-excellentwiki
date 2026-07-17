---
title: "KeyNotFoundException in F#"
description: "F# raises KeyNotFoundException when accessing a dictionary key that doesn't exist"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `KeyNotFoundException` occurs when accessing a key in a dictionary or map that does not exist. This is thrown by the indexer `dict.[key]` when the key is missing.

## Common Causes

- Accessing non-existent key with indexer
- Typo in key name
- Key not added to dictionary
- Case sensitivity mismatch

## How to Fix

Use `TryGetValue`:

```fsharp
open System.Collections.Generic

let dict = Dictionary<string, int>()
dict.Add("one", 1)

match dict.TryGetValue("two") with
| true, value -> printfn "Found: %d" value
| false, _ -> printfn "Key not found"
```

Use `Map.tryFind`:

```fsharp
let map = Map [("one", 1); ("two", 2)]

match Map.tryFind "three" map with
| Some value -> printfn "Found: %d" value
| None -> printfn "Key not found"
```

Use `Map.defaultValue`:

```fsharp
let value = map |> Map.tryFind "missing" |> Option.defaultValue 0
```

Check before access:

```fsharp
let safeGet key (dict: Dictionary<_, _>) =
    if dict.ContainsKey(key) then Some dict.[key]
    else None
```

## Examples

```fsharp
let dict = dict [("a", 1); ("b", 2)]
let value = dict.["c"]  // KeyNotFoundException
```

## Related Errors

- [IndexOutOfRangeException]({{< relref "/languages/fsharp/index-out-of-range" >}})
- [NullReferenceException]({{< relref "/languages/fsharp/null-reference5" >}})
