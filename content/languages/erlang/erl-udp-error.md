---
title: "[Solution] Erlang UDP Error"
description: "UDP socket errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang UDP Error

UDP socket errors.

### Common Causes
Wrong port; broadcast; buffer size

### How to Fix
```erlang
{ok, Socket} = gen_udp:open(0, [binary]),
gen_udp:send(Socket, {127,0,0,1}, 8080, <<"data">>).
```

### Examples
```erlang
receive
    {udp, Socket, IP, Port, Data} -> handle(Data)
end.
```
