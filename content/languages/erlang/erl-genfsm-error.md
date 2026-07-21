---
title: "[Solution] Erlang gen_fsm"
description: "gen_fsm deprecated behavior"
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang gen_fsm

gen_fsm deprecated behavior

### Common Causes
Use gen_statem instead

### How to Fix
```erlang
% Deprecated - use gen_statem
-behaviour(gen_fsm).
```

### Examples
```erlang
-behaviour(gen_statem).
init(_) -> {ok, idle, #{}}.
idle(info, go, State) -> {next_state, active, State}.
```
