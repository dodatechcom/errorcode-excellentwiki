---
title: "[Solution] Elixir CaseClauseError — No Matching Case Clause"
description: "Fix Elixir CaseClauseError when no case clause matches. Learn about case expressions, pattern matching, and wildcard clauses in Elixir."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `CaseClauseError` is raised when none of the clauses in a `case` expression match the input value. The error message shows the value that could not be matched. This is different from `FunctionClauseError` because it specifically relates to `case` statements within function bodies.

## Why It Happens

The most common cause is a `case` expression that does not cover all possible values. If a new variant is added to a tagged tuple or enum but the `case` expression is not updated, the error occurs.

Another frequent cause is missing wildcard `_` clauses. Without a catch-all clause, any unexpected value causes the error.

Guard clause rejections cause this error when a clause matches structurally but the guard condition fails. If all other clauses also fail, the error is raised.

Pattern matching on nested structures can fail if the inner structure does not match expectations. For example, matching `{:ok, %{status: status}}` will fail if the map does not have a `:status` key.

Finally, comparing atoms with strings or other types in case clauses can cause unexpected non-matches.

## How to Fix It

### Always include a wildcard clause

```elixir
case status do
  :ok -> "Success"
  :error -> "Error"
  _ -> "Unknown"
end
```

### Handle all possible tagged tuple variants

```elixir
case result do
  {:ok, value} -> process(value)
  {:error, reason} -> handle_error(reason)
  {:pending, id} -> wait_for_completion(id)
end
```

### Use pin operator for literal matching

```elixir
expected = :ok
case result do
  ^expected -> "matched"
  _ -> "not matched"
end
```

### Match on nested structures completely

```elixir
case response do
  {:ok, %{status: 200, body: body}} -> parse_body(body)
  {:ok, %{status: 404}} -> {:error, :not_found}
  {:ok, %{status: status}} -> {:error, {:http_error, status}}
  {:error, reason} -> {:error, reason}
end
```

### Use if/else for simple conditions

```elixir
if status == :ok do
  "success"
else
  "failure"
end
```

## Common Mistakes

- Not covering all possible values in case expressions
- Forgetting that case clauses are evaluated in order
- Not handling nested pattern match failures
- Using case when function heads would be cleaner
- Not using wildcard clauses for unexpected values

## Related Pages

- [Elixir CondClauseError](/languages/elixir/elixir-condclauseerror/)
- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
