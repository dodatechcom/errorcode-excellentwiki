---
title: "[Solution] Elixir AgentUpdateError - Brief Description"
description: "Fix Elixir Agent update errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1017
---

An Agent update error occurs when `Agent.update` fails or the Agent is not running.

## Common Causes

- Agent process crashed or was stopped
- Update function raising an exception
- Agent timeout exceeded

## How to Fix

Use `get_and_update` for atomic operations:

```elixir
{old_val, new_val} = Agent.get_and_update(:counter, fn state ->
  {state, state + 1}
end)
```

Set appropriate timeouts:

```elixir
Agent.update(:my_agent, fn state ->
  expensive_computation(state)
end, 30_000)
```

## Examples

```elixir
{:ok, _} = Agent.start_link(fn -> 0 end, name: Counter)
Agent.update(Counter, &(&1 + 1))
count = Agent.get(Counter, & &1)
```

## Related Errors

- [AgentError](/languages/elixir/elixir-agent-error)
- [GenServerError](/languages/elixir/elixir-genserver-error)
