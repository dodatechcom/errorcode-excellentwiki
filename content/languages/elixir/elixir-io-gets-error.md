---
title: "[Solution] Elixir IOGetsError - Brief Description"
description: "Fix Elixir IO.gets errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1023
---

An `IO.gets` error occurs when reading from an unavailable IO device.

## Common Causes

- Calling `IO.gets` in a test or non-interactive process
- IO device closed or unavailable
- Using `IO.gets` without handling `:eof`

## How to Fix

Use `ExUnit.CaptureIO` for testing:

```elixir
test "gets user input" do
  output = ExUnit.CaptureIO.capture_io(fn ->
    IO.gets("Enter name: ")
  end)
  assert output =~ "Enter name:"
end
```

Use `StringIO` for simulated IO:

```elixir
{:ok, pid} = StringIO.open("input data\nsecond line")
{:ok, line} = IO.read(pid, :line)
StringIO.close(pid)
```

## Examples

```elixir
{:ok, io} = StringIO.open("hello")
data = IO.read(io, :line)
IO.puts(data)
```

## Related Errors

- [IOPutsError](/languages/elixir/elixir-io-puts-error)
- [FileError](/languages/elixir/elixir-file-error)
