---
title: "[Solution] Erlang TCP Error"
description: "TCP socket errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang TCP Error

TCP socket errors.

### Common Causes
Connection refused; timeout; buffer

### How to Fix
```erlang
{ok, Socket} = gen_tcp:connect("localhost", 8080, [binary, {packet, 0}]),
gen_tcp:send(Socket, <<"hello">>).
```

### Examples
```erlang
receive
    {tcp, Socket, Data} -> process(Data);
    {tcp_closed, Socket} -> closed
end.
```
