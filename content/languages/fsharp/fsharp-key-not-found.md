---
title: "[Solution] F# KeyNotFoundException — Key Not Found in Map or Dictionary"
description: "Fix F# KeyNotFoundException when accessing map or dictionary keys. Learn safe access with tryFind, containsKey, and Map.find patterns."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `KeyNotFoundException` is thrown when you access a `Map` or `Dictionary` with a key that does not exist. In F#, `Map.[key]` throws this exception if the key is missing. The .NET `Dictionary` class also throws this exception when using the indexer without first checking if the key exists.

## Why It Happens

The most common cause is accessing a map with `map.[key]` without first checking whether the key exists. Unlike some languages that return a default value, F# throws an exception for missing keys.

Another frequent cause is using `dict` (which is a .NET `Dictionary`) instead of F#'s immutable `Map`. The `dict` type throws `KeyNotFoundException` on missing keys, while `Map.find` also throws but `Map.tryFind` returns `Option`.

Race conditions in concurrent code can cause keys to be present when checked but absent when accessed. Between the check and the access, another thread may have removed the key.

Converting between `Dictionary` and `Map` can also cause issues. If the source dictionary has keys that are not preserved during conversion, subsequent lookups fail.

Finally, using case-sensitive key comparisons when the data is case-insensitive (like usernames or email addresses) causes unexpected missing keys.

## How to Fix It

### Use Map.tryFind for safe access

```fsharp
let value = myMap |> Map.tryFind "key"
match value with
| Some v  -> printfn "Found: %A" v
| None    -> printfn "Key not found"
```

### Check containsKey before access

```fsharp
if myMap.ContainsKey("key") then
    let value = myMap.["key"]
    printfn "Value: %A" value
```

### Use Map.defaultValue for default values

```fsharp
let value = myMap |> Map.tryFind "key" |> Option.defaultValue "default"
```

### Use Map.find with a default fallback

```fsharp
let value =
    myMap
    |> Map.tryFind "key"
    |> function
    | Some v -> v
    | None   -> defaultValue
```

### Convert Dictionary to Map safely

```fsharp
let mapFromDict (dict: System.Collections.Generic.Dictionary<_,_>) =
    dict |> Seq.map (fun kv -> kv.Key, kv.Value) |> Map.ofSeq
```

## Common Mistakes

- Using `map.[key]` instead of `Map.tryFind` without checking first
- Not handling the `None` case when using `Map.tryFind`
- Using case-sensitive key comparisons for case-insensitive data
- Mixing `dict` (mutable Dictionary) with `Map` (immutable) without conversion
- Assuming `Map.containsKey` followed by `Map.[key]` is thread-safe

## Related Pages

- [F# IndexOutOfRangeException](/languages/fsharp/fsharp-indexoutofrange/)
- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# InvalidOperation](/languages/fsharp/fsharp-invalidoperation/)
