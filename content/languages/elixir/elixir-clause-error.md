---
title: "[Solution] Elixir FunctionClauseError — No Function Clause Matching"
description: "Fix Elixir FunctionClauseError when no function clause matches input. Learn about pattern matching, guard clauses, and function head design."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `FunctionClauseError` is raised when a function is called with arguments that do not match any of its defined clauses. Unlike `CaseClauseError` which relates to `case` expressions, this error specifically relates to function heads that do not handle the given input.

## Why It Happens

The most common cause is calling a function with arguments that no clause handles. For example, if a function only handles `:ok` and `:error` tuples, calling it with `:pending` raises this error.

Another frequent cause is missing clauses for edge cases. Functions that handle the happy path but not edge cases like `nil`, empty lists, or unexpected types will fail when those cases occur.

Guard clause rejections can also cause this error. If a function clause matches structurally but the guard condition rejects the value, and no other clause matches, the error is raised.

Protocol implementation errors cause this error when you call a protocol function on a type that has not implemented the protocol.

Finally, behaviour callbacks that are not implemented by a module can cause this error when the behaviour framework tries to call the missing callback.

## How to Fix It

### Add a catch-all clause

```elixir
def process(:ok), do: "success"
def process(:error), do: "failure"
def process(other), do: "unknown: #{inspect(other)}"
```

### Use @callback and @behaviour for proper contracts

```elixir
defmodule MyBehaviour do
  @callback handle(term()) :: term()
end

defmodule MyModule do
  @behaviour MyBehaviour

  @impl true
  def handle(value), do: value
end
```

### Implement all protocol functions

```elixir
defprotocol MyProtocol do
  def to_string(value)
end

defimpl MyProtocol, for: Atom do
  def to_string(value), do: Atom.to_string(value)
end
```

### Add guards for better error messages

```elixir
def divide(_a, 0), do: raise(ArgumentError, "Cannot divide by zero")
def divide(a, b) when is_number(a) and is_number(b), do: a / b
```

### Use @spec to document expected types

```elixir
@spec process(term()) :: {:ok, term()} | {:error, atom()}
def process(value) do
  # ...
end
```

## Common Mistakes

- Not handling edge cases like nil, empty lists, or unexpected types
- Forgetting to implement all required protocol functions
- Not providing a catch-all clause for unknown inputs
- Using guards that are too restrictive
- Not implementing all behaviour callbacks

## Related Pages

- [Elixir CaseClauseError](/languages/elixir/elixir-caseclauseerror/)
- [Elixir CondClauseError](/languages/elixir/elixir-condclauseerror/)
- [Elixir UndefinedFunctionError](/languages/elixir/elixir-undefined-function/)
