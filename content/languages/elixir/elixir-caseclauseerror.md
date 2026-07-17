---
title: "CaseClauseError - No Matching Clause in Elixir"
description: "Elixir raises CaseClauseError when no clause in a case expression matches the given value"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["case", "clause", "match", "caseclauseerror", "pattern"]
weight: 5
---

## What This Error Means

A `CaseClauseError` is raised when none of the clauses in a `case` expression match the input value. Unlike `FunctionClauseError`, this specifically relates to `case` statements.

## Common Causes

- Missing wildcard `_` clause in case
- Not all possible values covered
- Case clause ordering issues
- Guard clauses rejecting all values

## How to Fix

Always include a wildcard clause:

```elixir
case status do
  :ok -> "Success"
  :error -> "Error"
  _ -> "Unknown status"
end
```

Cover all possible values:

```elixir
case type do
  :admin -> "Administrator"
  :user -> "Regular user"
  :guest -> "Guest"
  other -> "Unknown type: #{inspect(other)}"
end
```

Handle complex patterns:

```elixir
case response do
  {:ok, %{status: 200, body: body}} -> parse_body(body)
  {:ok, %{status: 404}} -> {:error, :not_found}
  {:ok, %{status: status}} -> {:error, {:http_error, status}}
  {:error, reason} -> {:error, reason}
end
```

## Examples

```elixir
case :unknown do
  :ok -> "Success"
  :error -> "Error"
end
# ** (CaseClauseError) no case clause matching: :unknown
```

## Related Errors

- [MatchError]({{< relref "/languages/elixir/match-error" >}})
- [CondClauseError]({{< relref "/languages/elixir/condclauseerror" >}})
