---
title: "[Solution] Elixir RuntimeError — Raise With No Matching Rescue"
description: "Fix Elixir RuntimeError when raise is not caught by rescue. Learn about raise, exception types, and proper error propagation."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `RuntimeError` is raised when `raise` is called with a string message or when a function raises an exception that is not caught by any `rescue` clause. The error message shows the string passed to `raise` or the exception details.

## Why It Happens

The most common cause is calling `raise "message"` without wrapping it in a `try/rescue` block. The exception propagates up the call stack until it reaches the top level, causing the process to crash.

Another frequent cause is raising exceptions in GenServer callbacks. If a GenServer's `handle_call`, `handle_cast`, or `handle_info` raises, the GenServer process terminates.

Using `raise` with a string instead of a proper exception struct makes it harder to rescue specific errors. String-based raises create `RuntimeError` exceptions that cannot be pattern matched by type.

Not re-raising exceptions in rescue blocks can cause unexpected behavior. If you catch an exception but do not re-raise it, the caller may not know an error occurred.

Finally, raising in `Task.async` without handling in `Task.await` causes the task to fail and the error to be wrapped in `RuntimeError`.

## How to Fix It

### Use proper exception structs

```elixir
# Wrong — string-based raise
raise "Something went wrong"

# Correct — use exception struct
raise RuntimeError, message: "Something went wrong"
```

### Define custom exceptions

```elixir
defmodule MyApp.ValidationError do
  defexception [:field, :message]

  @impl true
  def message(%{field: field, message: msg}) do
    "Validation failed for #{field}: #{msg}"
  end
end

raise MyApp.ValidationError, field: :name, message: "required"
```

### Rescue and re-raise properly

```elixir
try do
  risky_operation()
rescue
  e in ArgumentError ->
    Logger.error("Argument error: #{e.message}")
    reraise e, __STACKTRACE__
end
```

### Use throws for non-exception control flow

```elixir
throw {:error, "something"}

catch
  {:error, msg} -> msg
end
```

### Handle GenServer errors

```elixir
def handle_call(:work, _from, state) do
  try do
    result = do_work(state)
    {:reply, {:ok, result}, state}
  rescue
    e -> {:reply, {:error, e}, state}
  end
end
```

## Common Mistakes

- Using `raise "string"` instead of proper exception structs
- Not defining `@impl true` for the `message/1` function in custom exceptions
- Catching exceptions without re-raising when needed
- Raising in GenServer callbacks without handling
- Not using `reraise` with `__STACKTRACE__` to preserve the stack trace

## Related Pages

- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir CaseClauseError](/languages/elixir/elixir-caseclauseerror/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
