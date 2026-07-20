---
title: "[Solution] Elixir StreamRunError - Brief Description"
description: "Fix Elixir Stream.run errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1031
---

A `Stream.run` error occurs when trying to get a value from a stream that produces no output.

## Common Causes

- Using `Stream.run` and expecting a return value
- Stream pipeline raising during evaluation
- Mixing lazy Stream with eager Enum operations

## How to Fix

Understand Stream.run returns :ok:

```elixir
Stream.run(Stream.map([1, 2, 3], &(&1 * 2)))
# :ok - Use Enum.to_list to get results
```

Use Stream for large datasets:

```elixir
File.stream!("large.log")
|> Stream.map(&String.trim/1)
|> Stream.filter(&(String.length(&1) > 0))
|> Enum.take(10)
```

## Examples

```elixir
Stream.iterate(1, &(&1 * 2))
|> Stream.take(10)
|> Enum.to_list()
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

## Related Errors

- [EnumEmptyError](/languages/elixir/elixir-enum-empty)
- [EnumerableError](/languages/elixir/elixir-enumerable-error)
