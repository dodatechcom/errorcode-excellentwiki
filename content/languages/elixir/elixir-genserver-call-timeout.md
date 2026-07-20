---
title: "[Solution] Elixir GenServerCallTimeout - Brief Description"
description: "Fix Elixir GenServer.call timeout errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1015
---

A `GenServer.call/3` timeout error occurs when the GenServer does not respond within the timeout period.

## Common Causes

- GenServer performing slow operations in `handle_call`
- Deadlock: GenServer calling back to the caller
- Long-running database queries inside `handle_call`

## How to Fix

Increase timeout for long operations:

```elixir
GenServer.call(pid, {:process, data}, 60_000)
```

Avoid blocking in `handle_call`:

```elixir
def handle_call({:slow_operation}, _from, state) do
  Task.start(fn ->
    result = Repo.one!(slow_query())
    GenServer.cast(self(), {:operation_done, result})
  end)
  {:noreply, state}
end
```

## Examples

```elixir
case GenServer.call(pool, :checkout, 30_000) do
  {:ok, conn} -> use_connection(conn)
  {:error, :timeout} -> retry_checkout()
end
```

## Related Errors

- [GenServerError](/languages/elixir/elixir-genserver-error)
- [ProcessDied](/languages/elixir/elixir-process-died)
