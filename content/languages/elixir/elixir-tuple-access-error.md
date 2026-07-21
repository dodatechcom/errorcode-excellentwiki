---
title: "[Solution] Elixir Tuple Access Error -- Invalid Tuple Index"
description: "Fix Elixir tuple access errors when using elem/2 or pattern matching with incorrect tuple sizes."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Tuple Access Error

This error occurs when accessing tuple elements with `elem/2` using an out-of-bounds index, or pattern matching with wrong tuple size.

## Common Causes

- Index exceeds tuple size in `elem(tuple, index)`
- Pattern matching with fewer or more elements than the tuple contains
- Not considering that `put_elem` creates a new tuple
- Using negative indices (not supported)

## How to Fix

### Check tuple size before access

```elixir
# WRONG: index out of bounds
tuple = {:ok, "result"}
elem(tuple, 2)  # ArgumentError

# CORRECT: check size first
tuple = {:ok, "result"}
if tuple_size(tuple) > 2 do
  elem(tuple, 2)
else
  nil
end
```

### Pattern match correctly

```elixir
# WRONG: wrong pattern size
{:ok, value, extra} = {:ok, "result"}  # MatchError

# CORRECT: match actual shape
{:ok, value} = {:ok, "result"}
```

## Examples

```elixir
defmodule TupleUtils do
  def safe_elem(tuple, index) do
    if index >= 0 and index < tuple_size(tuple) do
      {:ok, elem(tuple, index)}
    else
      {:error, :out_of_bounds}
    end
  end
end
```
