---
title: "[Solution] Elixir Float Precision Error -- Arithmetic Rounding Issues"
description: "Fix Elixir float precision errors when performing floating-point arithmetic produces unexpected results."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["warning"]
---

# Elixir Float Precision Error

This error occurs when floating-point arithmetic produces results with unexpected precision due to IEEE 754 representation limitations.

## Common Causes

- Comparing floats with `==` instead of approximate comparison
- Accumulating many small float additions
- Displaying more decimal places than meaningful
- Mixing integers and floats causing implicit conversion

## How to Fix

### Use approximate comparison

```elixir
# WRONG: direct float comparison
0.1 + 0.2 == 0.3  # false

# CORRECT: use approximate comparison
def float_equal?(a, b, tolerance \\ 1.0e-10) do
  abs(a - b) < tolerance
end
```

### Use Decimal for financial calculations

```elixir
# WRONG: floats for money
total = 0.1 + 0.2

# CORRECT: use Decimal library
import Decimal
total = Decimal.add("0.1", "0.2")
```

## Examples

```elixir
defmodule Math do
  def float_equal?(a, b, tolerance \\ 1.0e-10) do
    abs(a - b) < tolerance
  end

  def round_to(value, decimals) do
    factor = :math.pow(10, decimals)
    round(value * factor) / factor
  end
end
```
