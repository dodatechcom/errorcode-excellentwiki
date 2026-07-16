---
title: "SyntaxError: unexpected token"
description: "A SyntaxError occurs when Julia encounters code that violates the language's syntax rules during parsing."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["syntax", "parser", "token", "syntaxerror"]
weight: 5
---

## What This Error Means

A `SyntaxError` is raised when Julia's parser encounters a token or construct that doesn't conform to the language's syntax rules. This is typically a compile-time error that prevents the code from running.

## Common Causes

- Missing or mismatched parentheses, brackets, or braces
- Incorrect operator usage
- Missing keywords like `end`
- Invalid character or encoding in source file

## How to Fix

```julia
# WRONG: Missing closing parenthesis
x = (1 + 2     # SyntaxError: unexpected token

# CORRECT: Balance parentheses
x = (1 + 2)    # 3
```

```julia
# WRONG: Missing end keyword
function greet(name)
    println("Hello, $name")
# SyntaxError: unexpected token

# CORRECT: Close function with end
function greet(name)
    println("Hello, $name")
end
```

## Examples

```julia
# Example 1: Mismatched brackets
arr = [1, 2, 3   # SyntaxError: unexpected token

# Example 2: Invalid operator
x = 5 +* 3       # SyntaxError: unexpected token *

# Example 3: Missing expression
if true
    x =
end             # SyntaxError: unexpected token
```

## Related Errors

- [UndefVarError: X not defined](/languages/julia/undefined-sym)
- [MethodError: no method matching X](/languages/julia/type-error)
