---
title: "[Solution] Elixir Map Merge Error -- Conflicting Key Resolution"
description: "Fix Elixir map merge errors when Map.merge encounters duplicate keys between two maps."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Map Merge Error

This error occurs when `Map.merge/2` encounters duplicate keys and the conflict resolution function is not provided or incorrect.

## Common Causes

- Two maps have the same key but different values
- Using `Map.merge/2` without conflict resolution
- Nested maps being overwritten instead of deep merged
- Map merge returning unexpected types for values

## How to Fix

### Use Map.merge/3 for conflicts

```elixir
# WRONG: second map wins
map1 = %{a: 1, b: 2}
map2 = %{b: 3, c: 4}
Map.merge(map1, map2)  # %{a: 1, b: 3, c: 4}

# CORRECT: resolve conflicts explicitly
Map.merge(map1, map2, fn _key, _v1, v2 -> v2 end)
```

### Deep merge nested maps

```elixir
def deep_merge(map1, map2) do
  Map.merge(map1, map2, fn
    _key, v1, v2 when is_map(v1) and is_map(v2) ->
      deep_merge(v1, v2)
    _key, _v1, v2 ->
      v2
  end)
end
```

## Examples

```elixir
def merge_configs(default, overrides) do
  Map.merge(default, overrides, fn
    :env, _default, override -> override
    key, default_val, override -> Map.merge(default_val, override)
  end)
end
```
