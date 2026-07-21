---
title: "[Solution] Elixir Enum Slice Error -- Invalid Range Operations"
description: "Fix Elixir enum slice errors when Enum.slice is called with invalid ranges or indices."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Enum Slice Error

This error occurs when `Enum.slice/2` is called with ranges or indices that are out of bounds or invalid.

## Common Causes

- Slicing with negative ranges that exceed collection length
- Using Enum.slice on non-enumerable types
- Passing start index greater than collection length
- Incompatible range types (first..last where first > last without step)

## How to Fix

### Use valid ranges

```elixir
# WRONG: range exceeds collection length
list = [1, 2, 3]
Enum.slice(list, 0..10)  # may return partial results

# CORRECT: use within bounds or dynamic ranges
Enum.slice(list, 0..min(2, length(list) - 1))
```

### Use Enum.take for head elements

```elixir
# Instead of slice for head elements
Enum.take(list, 5)

# For tail elements
Enum.take(list, -5)
```

## Examples

```elixir
def paginate(list, page, per_page) do
  offset = (page - 1) * per_page
  Enum.slice(list, offset..(offset + per_page - 1))
end
```
