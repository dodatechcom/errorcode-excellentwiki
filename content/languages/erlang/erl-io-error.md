---
title: "[Solution] Erlang IO Error"
description: "IO operations errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang IO Error

IO operations errors.

### Common Causes
File not found; encoding; permissions

### How to Fix
```erlang
{ok, File} = file:open("data.txt", [read]),
{ok, Content} = file:read(File, all),
close(File).
```

### Examples
```erlang
file:write_file("out.txt", "content").
```
