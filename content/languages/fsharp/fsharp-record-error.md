---
title: "[Solution] F# Record Type Mismatch — Copy and Update Expression Error"
description: "Fix F# record type mismatch in copy-and-update expressions. Learn record field types, structural equality, and copy syntax."
languages: ["fsharp"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A record type mismatch error occurs when you try to create or update a record with fields of the wrong type, or when using the copy-and-update syntax with incompatible values. F# records are nominally typed, and each field must match its declared type exactly.

## Why It Happens

The most common cause is passing a value of the wrong type to a record field. For example, if a record has `Name: string` and you try to set it to an `int`, the compiler reports a type mismatch.

Another frequent cause is using the copy-and-update syntax (`{ record with Field = value }`) where the new value has a different type than the original field. The compiler checks that the updated value matches the field's declared type.

Record field name typos produce a different error ("field not found"), but if the typo happens to match another field's name, you get a type mismatch instead.

Implicit conversions are not supported in F#, so you cannot assign an `int` to a `float` field without explicit conversion. This is different from C# where implicit numeric conversions are allowed.

Finally, generic record types can cause type inference issues. If the type parameter is inferred incorrectly, the fields may appear to have the wrong types.

## How to Fix It

### Match field types exactly

```fsharp
type User = {
    Name: string
    Age: int
    Email: string option
}

// Wrong — Age expects int
let user = { Name = "Alice"; Age = "30"; Email = None }

// Correct
let user = { Name = "Alice"; Age = 30; Email = Some "alice@example.com" }
```

### Use explicit type conversions

```fsharp
let user = {
    Name = "Alice"
    Age = string 30 |> int  // Convert explicitly
    Email = None
}

// Better — use the right type from the start
let user = { Name = "Alice"; Age = 30; Email = None }
```

### Use copy-and-update syntax correctly

```fsharp
let updatedUser = { user with Age = 31; Email = Some "new@example.com" }
```

### Handle optional fields properly

```fsharp
type Config = {
    Host: string
    Port: int option
    Timeout: int option
}

let defaultConfig = { Host = "localhost"; Port = Some 8080; Timeout = None }
let customConfig = { defaultConfig with Port = Some 3000 }
```

### Use anonymous records for quick data structures

```fsharp
let person = {| Name = "Alice"; Age = 30 |}
printfn "%s is %d" person.Name person.Age
```

## Common Mistakes

- Forgetting that F# records are nominally typed (same fields, different types are different records)
- Not using explicit conversions when assigning between numeric types
- Confusing record copy syntax with object initialization syntax
- Not handling `option` fields correctly in copy-and-update expressions
- Assuming anonymous records can be passed to functions expecting named records

## Related Pages

- [F# TypeMismatch Error](/languages/fsharp/fsharp-type-init-error/)
- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# MatchFailureException](/languages/fsharp/fsharp-match-failure/)
