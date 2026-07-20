---
title: "[Solution] Elixir ETSMatchError - Brief Description"
description: "Fix Elixir ETS table match errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1020
---

An ETS match error occurs when a match specification is invalid or the table does not exist.

## Common Causes

- Using match spec syntax incorrectly
- Table created with wrong access type
- Table was deleted or owner process died

## How to Fix

Use correct match specification:

```elixir
:ets.new(:my_table, [:set, :public, :named_table])
:ets.match(:my_table, {:"$1", :"$2", :"$3"})
```

Handle table lookup safely:

```elixir
case :ets.lookup(:my_table, key) do
  [{^key, value}] -> {:ok, value}
  [] -> {:error, :not_found}
end
```

## Examples

```elixir
:ets.insert(:my_table, {:key1, 42, "hello"})
results = :ets.match_object(:my_table, {:_, 42, :_})
```

## Related Errors

- [DETSOpenError](/languages/elixir/elixir-dets-open-error)
- [ArgumentError](/languages/elixir/elixir-argumenterror-elixir)
