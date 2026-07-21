---
title: "[Solution] Erlang Debug"
description: "Debugging errors; trace; broken"
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Debug

Debugging errors; trace; broken

### Common Causes
Wrong breakpoint; trace format

### How to Fix
```erlang
tracer:start().
tracer:trace({self(), function}, my_func).
```

### Examples
```erlang
%% Use io:format for debugging
io:format("Value: ~p~n", [Value]).
```
