---
title: "[Solution] Elixir ListUpdateAtError - Brief Description"
description: "Fix Elixir List.update_at errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1029
---

A `List.update_at` error occurs when the index is out of bounds.

## Common Causes

- Using a negative index that exceeds list length
- Updating an index beyond the list length
- Assuming 1-based indexing

## How to Fix

Check bounds before updating:

```elixir
def safe_update(list, index, fun) do
  if index >= 0 and index < length(list) do
    List.update_at(list, index, fun)
  else
    list
  end
end
```

Use `Enum.with_index`:

```elixir
items = ["a", "b", "c"]
updated = items
|> Enum.with_index()
|> Enum.map(fn
  {item, 1} -> String.upcase(item)
  {item, _} -> item
end)
```

## Examples

```elixir
list = [1, 2, 3, 4, 5]
updated = List.update_at(list, 2, &(&1 * 10))
# [1, 2, 30, 4, 5]
```

## Related Errors

- [ArgumentError](/languages/elixir/elixir-argumenterror-elixir)
- [FunctionClauseError](/languages/elixir/elixir-function-clause)
