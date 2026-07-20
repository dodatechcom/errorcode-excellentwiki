---
title: "FSharp QueryExpressionError"
description: "Fix query expression errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1090
---

A query expression error occurs when LINQ-style queries are used incorrectly.

## Common Causes

- Using query expressions with non-IQueryable sources
- Missing required LINQ extensions
- Incorrect query syntax

## How to Fix

Use correct query syntax:

```fsharp
let numbers = [1; 2; 3; 4; 5]
let result = query {
    for n in numbers do
        where (n > 2)
        select n
}
```

Use query with database:

```fsharp
let adults = query {
    for person in dbContext.People do
        where (person.Age >= 18)
        select person.Name
}
```

## Examples

```fsharp
let products = [
    { Name = "A"; Price = 10 }
    { Name = "B"; Price = 25 }
]

let expensive = query {
    for p in products do
        where (p.Price > 15)
        sortByDescending p.Price
        select p.Name
}
```

## Related Errors

- [F# SeqComprehension](/languages/fsharp/fsharp-seq-comprehension-error)
- [F# ListComprehension](/languages/fsharp/fsharp-list-comprehension-error)
