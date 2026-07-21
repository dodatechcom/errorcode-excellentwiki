---
title: "[Solution] Erlang Port Driver"
description: "Port driver errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Port Driver

Port driver errors.

### Common Causes
Wrong driver; not linked; crash

### How to Fix
```erlang
Port = open_port({spawn_driver, "my_driver"}, [binary]).
```

### Examples
```erlang
port_command(Port, <<"data">>).
receive
    {Port, {data, Data}} -> process(Data)
end.
```
