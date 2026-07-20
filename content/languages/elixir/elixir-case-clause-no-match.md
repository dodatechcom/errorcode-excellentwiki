---
title: "[Solution] Elixir CaseNoMatchError - Brief Description"
description: "Fix Elixir case expression errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1038
---

A `CaseClauseError` occurs when a `case` expression encounters an unmatched value.

## Common Causes

- Not all possible values covered by case clauses
- Adding new variants without updating case
- Guard clauses rejecting values without fallback

## How to Fix

Add a catch-all clause:

```elixir
case status do
  :active -> "Active"
  :inactive -> "Inactive"
  other -> "Unknown: #{inspect(other)}"
end
```

Handle nil explicitly:

```elixir
case result do
  {:ok, value} -> value
  {:error, reason} -> raise reason
  nil -> "No result"
end
```

## Examples

```elixir
case File.read(path) do
  {:ok, content} -> process(content)
  {:error, :enoent} -> create_file(path)
  {:error, reason} -> IO.error("File error: #{inspect(reason)}")
end
```

## Related Errors

- [CaseClauseError](/languages/elixir/elixir-caseclauseerror)
- [MatchError](/languages/elixir/elixir-matcherror)
