---
title: "[Solution] F# String Concat Error -- Incorrect String Operations"
description: "Fix F# string concatenation errors when using + operator or String.concat incorrectly."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# String Concat Error

This error occurs when string concatenation operations fail due to type mismatches or incorrect use of string functions.

## Common Causes

- Using `+` operator with non-string types without conversion
- Passing wrong separator type to String.concat
- Not calling .ToString() on objects before concatenation
- Mixing `+` with null strings causing NullReferenceException

## How to Fix

### Use sprintf for complex formatting

```fsharp
// WRONG: manual concatenation with type issues
let name = "Alice"
let age = 30
let msg = name + " is " + age + " years old"  // error: int + string

// CORRECT: use sprintf
let msg = sprintf "%s is %d years old" name age
```

### Use String.concat correctly

```fsharp
// WRONG: wrong separator type
let result = String.concat ", " [1; 2; 3]  // error: needs string list

// CORRECT: convert to string list first
let result = String.concat ", " (List.map string [1; 2; 3])
```

## Examples

```fsharp
let joinWords (words: string list) =
    String.concat " " words

let formatList items =
    items
    |> List.map string
    |> String.concat ", "
    |> sprintf "[%s]"
```
