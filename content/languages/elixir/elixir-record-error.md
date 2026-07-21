---
title: "[Solution] Elixir Record Error -- Erlang Record Interop Issues"
description: "Fix Elixir record errors when working with Erlang records and accessing record fields."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Record Error

This error occurs when Elixir code incorrectly accesses Erlang record fields or defines records with invalid syntax.

## Common Causes

- Using dot notation instead of record macros for field access
- Wrong field name in record access
- Records defined without requiring the record header file
- Accessing tuple-based records as if they were structs

## How to Fix

### Use Erlang record macros correctly

```elixir
# WRONG: accessing Erlang record as struct
:user.name  # error

# CORRECT: use record accessor macro
:user.name(record)
# or
record.name
```

### Define records properly

```elixir
defmodule MyRecord do
  require Record

  Record.defrecord(:user, name: "", age: 0, email: nil)

  def create_user(name, age) do
    user(name: name, age: age)
  end
end
```

## Examples

```elixir
defmodule Config do
  Record.defrecordp(:config,
    host: "localhost",
    port: 4000,
    ssl: false
  )

  def default do
    config(host: "localhost", port: 4000)
  end
end
```
