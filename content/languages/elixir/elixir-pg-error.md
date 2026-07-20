---
title: "[Solution] Elixir PGError - Brief Description"
description: "Fix Elixir :pg process group errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1034
---

A `:pg` error occurs when using process groups for scalable group membership.

## Common Causes

- :pg scope not started
- Trying to join a non-existent group
- Scope name mismatch across nodes

## How to Fix

Start the pg scope:

```elixir
children = [
  {:pg, scope: MyApp.PGScope},
  MyApp.Worker
]
Supervisor.start_link(children, strategy: :one_for_one)
```

Get group members:

```elixir
case :pg.get_members(MyApp.PGScope, :my_group) do
  members when is_list(members) ->
    Enum.each(members, &send(&1, :message))
  {:error, _reason} ->
    Logger.warning("Group not found")
end
```

## Examples

```elixir
{:ok, _} = :pg.start_link(MyScope)
:pg.join(MyScope, :chat_room, self())
members = :pg.get_members(MyScope, :chat_room)
```

## Related Errors

- [GlobalRegistryError](/languages/elixir/elixir-global-registry-error)
- [RegistryError](/languages/elixir/elixir-registry-error)
