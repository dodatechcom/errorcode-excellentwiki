---
title: "[Solution] Erlang Port Error"
description: "Port (external process) errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Port Error

Port (external process) errors.

### Common Causes
Wrong command; not reading output

### How to Fix
```erlang
Port = open_port({spawn, "ls"}, [binary, stream]),
receive
    {Port, {data, Data}} -> Data
end.
```

### Examples
```erlang
port_command(Port, <<"input">>).
```
