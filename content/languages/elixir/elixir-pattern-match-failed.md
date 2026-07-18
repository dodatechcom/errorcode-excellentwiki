---
title: "[Solution] Fix no match of right hand side value in Elixir"
description: "Resolve MatchError in Elixir by understanding pattern matching failures, using case expressions, and restructuring your match logic to handle all cases."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A `MatchError` is raised when the left-hand side of a pattern match expression does not match the right-hand side value. This is one of the most common errors in Elixir since pattern matching is fundamental to the language.

The error appears as:

```elixir
** (MatchError) no match of right hand side value: {:error, :timeout}
```

## Why It Happens

This error occurs when patterns are too specific or values are unexpected:

- Matching against a specific tuple structure when the value has a different shape
- Using `=` assignment when expecting a particular pattern
- Forgetting that match errors also occur in function heads
- Not accounting for all possible return values from a function
- Assuming a value has one structure when it actually has another

## How to Fix It

Use broader patterns and handle all cases:

```elixir
# WRONG: Only matches {:ok, result}
{:ok, result} = fetch_data()

# CORRECT: Use case to handle all possibilities
case fetch_data() do
  {:ok, result} -> process(result)
  {:error, reason} -> handle_error(reason)
end
```

Avoid direct assignment matches for values you cannot control:

```elixir
# WRONG: Crashes if status is not :active
{:ok, user} = get_user(id)
:active = user.status

# CORRECT: Use pattern matching in case
case get_user(id) do
  {:ok, %{status: :active} = user} -> process_active_user(user)
  {:ok, %{status: :inactive}} -> {:error, :inactive}
  {:error, reason} -> {:error, reason}
end
```

Use the pin operator `^` when matching against existing variables:

```elixir
expected = :admin
role = :admin
^expected = role  # matches

expected = :admin
role = :user
^expected = role  # MatchError
```

Use `Kernel.elem/2` for partial tuple matching without full destructure:

```elixir
value = {:ok, 42, :extra}
if elem(value, 0) == :ok do
  elem(value, 1)
end
```

## Common Mistakes

- Using `=` for assignment when `case` or `with` would be safer
- Assuming pattern matches will bind new variables instead of matching existing ones
- Not realizing that `<<>>` binary pattern matches can fail on unexpected lengths
- Forgetting that `_` ignores values while `_name` still binds without warning
- Using strict pattern matches on external data like API responses or file contents

## Related Pages

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [CaseClauseError in Elixir](/languages/elixir/elixir-caseclauseerror)
- [KeyError: key not found](/languages/elixir/elixir-keyerror-elixir)
