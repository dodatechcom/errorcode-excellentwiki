---
title: "[Solution] Elixir CollectableError - Brief Description"
description: "Fix Elixir Collectable protocol errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1028
---

A Collectable error occurs when using `Enum.into/2` with a non-collectable target.

## Common Causes

- Collecting into a struct without Collectable
- Using `Enum.into` with a binary or tuple

## How to Fix

Collect into built-in types:

```elixir
Enum.into([{:a, 1}, {:b, 2}], %{})
Enum.into(1..5, [])
Enum.into([1, 2, 2, 3], MapSet.new())
```

## Examples

```elixir
Enum.into(["hello", "world"], MapSet.new())
```

## Related Errors

- [EnumerableError](/languages/elixir/elixir-enumerable-error)
- [EnumEmptyError](/languages/elixir/elixir-enum-empty)
