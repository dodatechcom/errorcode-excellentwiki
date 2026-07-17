---
title: "CondClauseError - No Matching Clause in Cond"
description: "Elixir raises CondClauseError when no condition in a cond expression evaluates to true"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `CondClauseError` is raised when none of the conditions in a `cond` expression evaluate to `true`. Unlike `case`, `cond` evaluates boolean expressions.

## Common Causes

- No condition evaluates to true
- All conditions evaluate to false or nil
- Missing `true` catch-all condition
- Logic error in condition expressions

## How to Fix

Always include a `true` catch-all:

```elixir
cond do
  score >= 90 -> "A"
  score >= 80 -> "B"
  score >= 70 -> "C"
  true -> "F"
end
```

Check conditions carefully:

```elixir
user = %{role: :guest, active: false}

cond do
  user.role == :admin -> "Admin panel"
  user.role == :user and user.active -> "User dashboard"
  user.role == :guest -> "Guest view"
  true -> "Default view"
end
```

Handle nil values:

```elixir
config = %{}

cond do
  config[:debug_mode] -> "Debug"
  config[:verbose] -> "Verbose"
  true -> "Normal"
end
```

## Examples

```elixir
cond do
  1 > 2 -> "First"
  3 > 4 -> "Second"
end
# ** (CondClauseError) no cond clauses matching
```

## Related Errors

- [CaseClauseError]({{< relref "/languages/elixir/caseclauseerror" >}})
- [MatchError]({{< relref "/languages/elixir/match-error" >}})
