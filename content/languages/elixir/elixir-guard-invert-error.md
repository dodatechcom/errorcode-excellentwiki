---
title: "[Solution] Elixir Guard Invert Error -- Incorrect Boolean Logic in Guards"
description: "Fix Elixir guard invert errors when using not, or, and operators incorrectly in guard expressions."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Guard Invert Error

This error occurs when boolean operators in guard expressions are used incorrectly, such as using `!` instead of `not`.

## Common Causes

- Using `!` instead of `not` for negation in guards
- Using `||` and `&&` instead of `or` and `and`
- Using `==` with nil instead of `is_nil/1`
- Negating complex expressions that cannot be inverted in guards

## How to Fix

### Use correct guard operators

```elixir
# WRONG: wrong operator for guard
def process(x) when !is_nil(x) and x > 0, do: x

# CORRECT: use 'not' and 'and'
def process(x) when not is_nil(x) and x > 0, do: x
```

### Use is_nil guard

```elixir
# WRONG: x == nil not allowed in all guard contexts
def handle(x) when x == nil, do: :none

# CORRECT: use is_nil
def handle(x) when is_nil(x), do: :none
def handle(x), do: {:ok, x}
```

## Examples

```elixir
def classify(value) when not is_nil(value) and value > 0, do: :positive
def classify(value) when not is_nil(value) and value < 0, do: :negative
def classify(nil), do: :missing
def classify(_), do: :zero
```
