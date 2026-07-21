---
title: "[Solution] F# Record Update Error -- Updating Immutable Records"
description: "Fix F# record update errors when using the with keyword to create modified copies of records."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Record Update Error

This error occurs when the record update expression is syntactically incorrect or targets fields that do not exist.

## Common Causes

- Missing the `with` keyword in record update syntax
- Referencing a field name that does not exist on the record type
- Updating a record without a source record value
- Forgetting to specify all required fields when creating records without defaults

## How to Fix

### Use correct with syntax

```fsharp
type User = { Name: string; Age: int }

let alice = { Name = "Alice"; Age = 30 }

// WRONG: missing with keyword
let olderAlice = alice { Age = 31 }

// CORRECT: use with
let olderAlice = { alice with Age = 31 }
```

### Verify field names

```fsharp
type Config = { Host: string; Port: int }

let defaultConfig = { Host = "localhost"; Port = 8080 }

let devConfig = { defaultConfig with Port = 3000 }
```

## Examples

```fsharp
type Order =
    { Id: int
      Item: string
      Quantity: int
      Price: float }

let original = { Id = 1; Item = "Widget"; Quantity = 5; Price = 9.99 }
let discounted = { original with Price = original.Price * 0.9 }
```
