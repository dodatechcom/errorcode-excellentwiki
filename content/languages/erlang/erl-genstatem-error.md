---
title: "[Solution] Erlang gen_statem"
description: "gen_statem behavior errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang gen_statem

gen_statem behavior errors.

### Common Causes
Wrong state; missing events; callback errors

### How to Fix
```erlang
-behaviour(gen_statem).
callback_mode() -> state_functions.
start() -> gen_statem:start_link({local, ?MODULE}, ?MODULE, [], []).
```

### Examples
```erlang
idle({call, From}, start, Data) ->
    {next_state, running, Data, [{reply, From, ok}]}.
```
