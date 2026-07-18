---
title: "[Solution] F# Quotation Evaluation Error — Invalid Expression in Quotation"
description: "Fix F# quotation evaluation errors. Learn about typed quotations, expression trees, and why some code cannot be quoted."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A quotation evaluation error occurs when an F# quotation (`<@ ... @>` or `<@@ ... @@>`) contains expressions that cannot be represented as an expression tree. The error message typically indicates which expression is not supported, such as "quotations cannot contain mutable values" or "unsupported expression type".

## Why It Happens

The most common cause is using mutable variables inside quotations. F# quotations represent code as data structures, and mutable bindings cannot be represented in the expression tree.

Another frequent cause is using .NET methods that are not supported by the quotation compiler. Some methods (like those with `outref` parameters or certain generic constraints) cannot be represented as quotation expressions.

Using `printfn` or other I/O functions inside quotations also fails because these are not pure expressions that can be evaluated symbolically.

Side effects in quotations are not supported. Assigning to mutable fields, calling void methods, or performing any I/O operation inside a quotation causes an error.

Finally, some language constructs like `match` with complex guards or `try-catch` blocks may not be fully supported in all quotation contexts.

## How to Fix It

### Remove mutable variables from quotations

```fsharp
// Wrong — mutable variable in quotation
let mutable x = 10
let expr = <@ x + 1 @>  // Error

// Correct — use immutable binding
let x = 10
let expr = <@ x + 1 @>
```

### Use expression builders for complex quotations

```fsharp
open Microsoft.FSharp.Quotations

// Build expressions programmatically
let addExpr = Expr.Call(
    typeof<int>.GetMethod("op_Addition"),
    [Expr.Value(1); Expr.Value(2)]
)
```

### Avoid side effects in quotations

```fsharp
// Wrong — I/O in quotation
let expr = <@ printfn "hello" @>

// Correct — separate I/O from quotation
let expr = <@ 1 + 1 @>
printfn "%A" (expr.Eval())
```

### Use typed quotations for type safety

```fsharp
// Typed quotation — type checked at compile time
let expr : Expr<int> = <@ 1 + 1 @>

// Untyped quotation — more flexible but less safe
let expr = <@@ 1 + 1 @@>
```

### Evaluate quotations safely

```fsharp
let result = <@ 2 + 3 @>.Eval()  // Returns 5
```

## Common Mistakes

- Using mutable variables inside quotations
- Putting I/O operations or side effects in quotation expressions
- Assuming all F# code can be quoted (some constructs are not supported)
- Not understanding the difference between `<@ @>` (typed) and `<@@ @@>` (untyped)
- Trying to evaluate quotations that reference external assemblies not available at runtime

## Related Pages

- [F# Type Provider Error](/languages/fsharp/fsharp-type-provider/)
- [F# Computation Expression Error](/languages/fsharp/fsharp-computation-expression/)
- [F# MatchFailureException](/languages/fsharp/fsharp-match-failure/)
