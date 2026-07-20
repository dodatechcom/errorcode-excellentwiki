---
title: "[Solution] Elixir DETSOpenError - Brief Description"
description: "Fix Elixir DETS table open errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1021
---

A DETS open error occurs when a Disk-ETS table cannot be opened or is corrupted.

## Common Causes

- DETS file corrupted due to unclean shutdown
- Table exceeds 2GB size limit
- Permission denied on file path

## How to Fix

Use `open_file` with recovery:

```elixir
case :dets.open_file(:my_table, file: "data/dets/table.bin") do
  {:ok, ref} -> {:ok, ref}
  {:error, reason} ->
    IO.error("DETS open failed: #{inspect(reason)}")
end
```

Repair corrupted tables:

```elixir
case :dets.recover("data/table.bin") do
  {:ok, ref} -> IO.puts("Table repaired")
  {:error, reason} -> IO.error("Repair failed: #{inspect(reason)}")
end
```

## Examples

```elixir
{:ok, ref} = :dets.open_file(:cache, file: "cache.bin", type: :set)
:dets.insert(ref, {:key, "value"})
```

## Related Errors

- [ETSMatchError](/languages/elixir/elixir-ets-match-error)
- [FileError](/languages/elixir/elixir-file-error)
