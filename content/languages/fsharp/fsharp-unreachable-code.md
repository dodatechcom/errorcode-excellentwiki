---
title: "[Solution] F# Unreachable Code Warning -- Fixing Dead Code Blocks"
description: "Fix F# unreachable code warnings by removing dead branches, unreachable match cases, and statements after return."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["warning"]
---

# F# Unreachable Code Warning

The F# compiler warns when it detects code that can never be executed due to preceding return statements, pattern matches, or control flow.

## Common Causes

- Statements placed after a return or raise expression
- Unreachable branches in if/else or match expressions
- Code after an infinite loop without a break equivalent
- Redundant match cases covered by earlier patterns

## How to Fix

### Remove dead code after return

```fsharp
// WRONG: code after return
let getValue x =
    if x > 0 then
        x
        "done"  // unreachable

// CORRECT: remove the dead line
let getValue x =
    if x > 0 then
        x
    else
        0
```

### Fix wildcard match ordering

```fsharp
// WRONG: wildcard covers everything first
match 42 with
| _ -> "anything"
| x when x > 100 -> "large"  // unreachable

// CORRECT: place specific patterns first
match 42 with
| x when x > 100 -> "large"
| _ -> "anything"
```

## Examples

```fsharp
let processList items =
    match items with
    | [] -> "empty"
    | [x] -> sprintf "single: %A" x
    | first :: rest -> sprintf "first: %A, rest: %d" first (List.length rest)
```
