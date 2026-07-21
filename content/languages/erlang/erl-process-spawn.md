---
title: "[Solution] Erlang Process Spawn"
description: "spawn and process errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Process Spawn

spawn and process errors.

### Common Causes
Wrong module; function not exported; linked

### How to Fix
```erlang
Pid = spawn(fun() ->
    receive stop -> ok end
end),
Pid ! stop.
```

### Examples
```erlang
Pid = spawn(?MODULE, my_func, [Arg1, Arg2]),
link(Pid).
```
