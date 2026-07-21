---
title: "[Solution] Erlang File Error"
description: "File system operation errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang File Error

File system operation errors.

### Common Causes
Path not found; permissions; encoding

### How to Fix
```erlang
{ok, Binary} = file:read_file("data.txt"),
Content = binary_to_list(Binary).
```

### Examples
```erlang
filelib:is_file("path/to/file").
```
