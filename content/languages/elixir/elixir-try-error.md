---
title: "[Solution] Elixir MatchError in Rescue — Pattern Match Failed in Rescue"
description: "Fix Elixir MatchError inside rescue clauses. Learn about rescue pattern matching, exception types, and proper error handling."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `MatchError` inside a `rescue` clause occurs when the rescue pattern does not match the actual exception that was raised. Elixir's rescue clause uses pattern matching to catch specific exception types, and if the pattern does not match, a `MatchError` is raised inside the rescue block.

## Why It Happens

The most common cause is rescuing for a specific exception type that was not raised. For example, `rescue RuntimeError ->` will not catch `ArgumentError`, and attempting to match on the wrong type causes this error.

Another frequent cause is trying to pattern match on exception attributes that do not exist. If you write `rescue e in RuntimeError -> e.message` but the exception does not have a `message` field, the match fails.

Using `rescue` without specifying the exception type catches all exceptions, but if you try to access properties that do not exist on the caught exception, a `MatchError` occurs.

Finally, rescuing in a `try` block that does not raise any exceptions can cause issues if the rescue clause has complex pattern matching.

## How to Fix It

### Rescue on the correct exception type

```elixir
try do
  risky_operation()
rescue
  RuntimeError -> "runtime error"
  ArgumentError -> "argument error"
  _ -> "other error"
end
```

### Use the exception variable correctly

```elixir
try do
  risky_operation()
rescue
  e in RuntimeError -> e.message
  e in ArgumentError -> "Bad argument: #{e.message}"
end
```

### Catch all exceptions with a wildcard

```elixir
try do
  risky_operation()
rescue
  _ -> "caught an exception"
end
```

### Use after for cleanup

```elixir
try do
  risky_operation()
rescue
  e -> Logger.error("Error: #{inspect(e)}")
after
  cleanup()
end
```

### Use catch for throws and exits

```elixir
try do
  risky_operation()
catch
  :exit, reason -> {:exit, reason}
  :throw, value -> {:throw, value}
end
```

## Common Mistakes

- Rescuing the wrong exception type
- Trying to match on exception fields that do not exist
- Not re-raising exceptions that should propagate
- Using rescue when catch would be more appropriate
- Forgetting that rescue only catches exceptions, not throws or exits

## Related Pages

- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir RuntimeError](/languages/elixir/elixir-rescueerror/)
