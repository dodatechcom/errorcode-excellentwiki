---
title: "[Solution] Erlang Distributed Error"
description: "Distributed Erlang errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Distributed Error

Distributed Erlang errors.

### Common Causes
Node not connected; wrong node name

### How to Fix
```erlang
net_adm:ping('node@host').
```

### Examples
```erlang
{ok, Node} = net_adm:host_file(),
erpc:call(Node, mod, func, [Arg]).
```
