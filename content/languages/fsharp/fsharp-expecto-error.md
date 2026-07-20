---
title: "FSharp ExpectoError"
description: "Fix Expecto test framework errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1113
---

An Expecto error occurs when writing tests with the Expecto framework incorrectly.

## Common Causes

- Missing testList or test case definitions
- Incorrect test assertions
- Not running test suite properly

## How to Fix

Define tests correctly:

```fsharp
open Expecto

let tests = testList "MyTests" [
    test "addition" {
        Expect.equal (2 + 2) 4 "2+2 should equal 4"
    }
    test "list length" {
        Expect.equal (List.length [1;2;3]) 3 "list should have 3 items"
    }
]

[<EntryPoint>]
let main argv = runTestsWithCLIArgs [] argv tests
```

Use async tests:

```fsharp
testAsync "async test" {
    let! result = asyncOperation()
    Expect.equal result expected "async result"
}
```

## Examples

```fsharp
let testConnection =
    test "database connection" {
        let conn = createConnection()
        Expect.isSome conn "connection should exist"
    }
```

## Related Errors

- [F# FsCheck](/languages/fsharp/fsharp-fscheck-error)
- [F# TaskComputation](/languages/fsharp/fsharp-task-computation-error)
