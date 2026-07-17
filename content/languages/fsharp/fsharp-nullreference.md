---
title: "NullReferenceException in F#"
description: "F# raises NullReferenceException when accessing a null reference"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `NullReferenceException` occurs when attempting to access a member or dereference a null reference. While F# discourages null, it can occur through .NET interop or explicit null assignment.

## Common Causes

- Java/.NET interop returning null
- Explicitly assigned null values
- Uninitialized object references
- Missing null checks on .NET types

## How to Fix

Use Option types instead of null:

```fsharp
// Wrong
let name: string = null
let length = name.Length  // NullReferenceException

// Correct
let name: string option = None
let length = name |> Option.map String.length |> Option.defaultValue 0
```

Handle null from .NET interop:

```fsharp
open System

let safeGetString (dict: System.Collections.Generic.Dictionary<string, string>) key =
    match dict.TryGetValue(key) with
    | true, value -> Some value
    | false, _ -> None
```

Use null checking:

```fsharp
let processValue (obj: obj) =
    if obj <> null then
        obj.ToString()
    else
        "null value"
```

Use option of nullable:

```fsharp
let fromNullable (value: Nullable<'a>) =
    if value.HasValue then Some value.Value else None
```

## Examples

```fsharp
let list : string list = null
let count = list.Length  // NullReferenceException
```

## Related Errors

- [IndexOutOfRangeException]({{< relref "/languages/fsharp/index-out-of-range" >}})
- [KeyNotFoundException]({{< relref "/languages/fsharp/notfoundexception" >}})
