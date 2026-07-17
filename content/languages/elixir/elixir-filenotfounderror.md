---
title: "File.Error - File Not Found in Elixir"
description: "Elixir raises File.Error when a file operation fails due to missing file or permission issues"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `File.Error` is raised when a file operation (read, write, delete) fails. The most common cause is the file not existing (`ENOENT`), but it can also be caused by permission issues.

## Common Causes

- File does not exist at specified path
- Insufficient permissions to access file
- File path is incorrect or contains typos
- Directory does not exist for file creation
- Symlink target does not exist

## How to Fix

Check file existence before operations:

```elixir
path = "data/config.json"

if File.exists?(path) do
  {:ok, content} = File.read(path)
else
  {:error, :not_found}
end
```

Handle file errors gracefully:

```elixir
case File.read("config.txt") do
  {:ok, content} ->
    parse_config(content)
  {:error, :enoent} ->
    IO.puts("Config file not found, using defaults")
    default_config()
  {:error, reason} ->
    IO.puts("File error: #{reason}")
end
```

Ensure directories exist:

```elixir
File.mkdir_p!("output/reports")
File.write!("output/reports/report.txt", "Report content")
```

Use proper path handling:

```elixir
path = Path.join(["data", "config", "app.json"])
File.mkdir_p!(Path.dirname(path))
File.write!(path, "{}")
```

## Examples

```elixir
File.read!("nonexistent.txt")
# ** (File.Error) could not read "nonexistent.txt": no such file or directory
```

## Related Errors

- [ArgumentError]({{< relref "/languages/elixir/argument-error4" >}})
- [KeyError]({{< relref "/languages/elixir/keyerror-elixir" >}})
