---
title: "[Solution] F# Named Argument Error -- Incorrect Named Parameters"
description: "Fix F# named argument errors when calling functions with named parameters incorrectly."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Named Argument Error

This error occurs when named arguments are used incorrectly in function calls or when the argument name does not match.

## Common Causes

- Misspelling the parameter name in a named argument
- Using named arguments with positional arguments in wrong order
- Passing named arguments to functions that do not name their parameters
- Using named arguments with partial application

## How to Fix

### Use correct parameter names

```fsharp
// WRONG: misspelled parameter name
let connect host port = ()
connect hosst "localhost" portt 42  // two errors

// CORRECT: match parameter names
connect host="localhost" port=42
```

### Order named arguments after positional

```fsharp
// WRONG: named before positional
connect port=42 "localhost"

// CORRECT: positional first, then named
connect "localhost" port=42
```

## Examples

```fsharp
let fetchData (url: string) (timeout: int) (retries: int) =
    sprintf "Fetching %s with timeout %d, retries %d" url timeout retries

let result =
    fetchData "https://api.example.com"
              timeout=5000
              retries=3
```
