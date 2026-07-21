---
title: "[Solution] Elixir Capture Operator Error -- Incorrect & Usage"
description: "Fix Elixir capture operator errors when the & operator is misused in function references."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Capture Operator Error

This error occurs when the `&` capture operator is used incorrectly, producing functions with wrong arity.

## Common Causes

- Using `&` with wrong number of placeholders
- Capturing functions with incorrect arity expectations
- Mixing `&` capture with anonymous function syntax
- Using `&` where a full anonymous function is needed

## How to Fix

### Match arity correctly

```elixir
# WRONG: &div/2 needs two arguments, but capture expects one
Enum.map([10, 20], &div(&1, 2))  # correct for one arg
Enum.map([10, 20], &div/2)       # error: &div/2 takes 2 args

# CORRECT: use partial application with &
Enum.map([10, 20], &div(&1, 2))  # [5, 10]
```

### Use full anonymous functions for complex cases

```elixir
# WRONG: too many captures
&(&1 + &2 + &3)  # confusing

# CORRECT: use full anonymous function
fn a, b, c -> a + b + c end
```

## Examples

```elixir
Enum.map([1, 2, 3], &(&1 * 2))         # [2, 4, 6]
Enum.filter([1, 2, 3, 4], &(&1 > 2))   # [3, 4]
Enum.reduce([1, 2, 3], 0, &+/2)         # 6
```
