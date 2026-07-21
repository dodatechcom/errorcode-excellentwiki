---
title: "[Solution] Elixir Logger Error -- Incorrect Logger Metadata Usage"
description: "Fix Elixir logger errors when Logger metadata is not set correctly or causes compilation issues."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Logger Error

This error occurs when Logger functions are called with incorrect arguments or metadata format.

## Common Causes

- Passing non-atom keys in metadata keyword list
- Using Logger macros without proper compilation flags
- Log level strings instead of atoms
- Metadata values not being strings or atoms

## How to Fix

### Use correct Logger syntax

```elixir
# WRONG: metadata must be keyword list
Logger.info("Starting", %{request_id: "123"})

# CORRECT: use keyword list
Logger.info("Starting", request_id: "123")
```

### Use Logger macros correctly

```elixir
# WRONG: using Logger.info as function in compile-time
Logger.info("Version: #{version}")  # version not available at compile time

# CORRECT: use Logger macro at runtime
def start do
  Logger.info("Version: #{version()}")
end
```

## Examples

```elixir
defmodule MyApp.Logger do
  require Logger

  def log_request(conn) do
    Logger.info("Request processed",
      method: conn.method,
      path: conn.request_path,
      status: conn.status
    )
  end
end
```
