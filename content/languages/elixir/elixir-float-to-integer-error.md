---
title: "[Solution] Elixir Float to Integer Error -- Lossy Conversion Issues"
description: "Fix Elixir float to integer errors when truncating or converting floats loses precision."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Float to Integer Error

This error occurs when converting a float to an integer using `round/1`, `trunc/1`, or `:erlang.float_to_list/1`.

## Common Causes

- Using `trunc` on a float that represents a whole number but has precision issues
- Not using `round` when rounding is intended
- Float values that overflow integer range
- Converting very large floats that lose precision

## How to Fix

### Choose the right conversion

```elixir
# trunc removes decimal (toward zero)
trunc(3.7)  # 3
trunc(-3.7) # -3

# round rounds to nearest integer
round(3.5)  # 4
round(3.4)  # 3

# Float.to_string for display
Float.to_string(3.14159, decimals: 2)  # "3.14"
```

### Handle precision carefully

```elixir
# WRONG: potential precision issues
result = 0.1 + 0.2  # 0.30000000000000004
round(result)  # 0

# CORRECT: use Decimal for precise arithmetic
Decimal.add("0.1", "0.2") |> Decimal.round()
```

## Examples

```elixir
defmodule NumberUtils do
  def to_int(value) when is_float(value), do: round(value)
  def to_int(value) when is_integer(value), do: value
end
```
