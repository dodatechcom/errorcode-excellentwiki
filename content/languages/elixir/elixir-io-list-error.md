---
title: "[Solution] Elixir IO List Error -- Incorrect IO List Construction"
description: "Fix Elixir IO list errors when building IO lists with incorrect data types or structure."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir IO List Error

This error occurs when IO lists are constructed with incorrect data types that cannot be converted to iodata.

## Common Causes

- Using non-binary, non-integer, non-io_list items
- Mixing iolists with raw binaries incorrectly
- Forgetting that IO lists are deeply nested lists
- Usingiodata instead ofiodiolist for specific functions

## How to Fix

### Use correct iodata types

```elixir
# WRONG: integer not valid iodata directly
IO.puts([65, 66, 67])  # needs to be characters or binaries

# CORRECT: use binaries or character lists
IO.puts(["A", "B", "C"])
IO.puts([65, 66, 67])  # actually works as charlist
```

### Build IO lists properly

```elixir
iolist = ["Hello", " ", "World"]
iodata = [<<1, 2, 3>>, "text", [<<4, 5>>, "more"]]
:erlang.iolist_to_binary(iodata)
```

## Examples

```elixir
defmodule HTML do
  defp tag(name, content) do
    [~s(<), name, ~s(>), content, ~s(</), name, ~s(>)]
  end

  def paragraph(text), do: tag("p", text)
  def heading(text, level), do: tag("h#{level}", text)
end
```
