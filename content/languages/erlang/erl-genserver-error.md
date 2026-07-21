---
title: "[Solution] Erlang gen_server Error"
description: "gen_server callback errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang gen_server Error

gen_server callback errors.

### Common Causes
Wrong return tuple; missing handle_call

### How to Fix
```erlang
init([]) -> {ok, initial_state}.
handle_call(get_state, _From, State) -> {reply, State, State}.
handle_cast(stop, State) -> {stop, normal, State}.
```

### Examples
```erlang
handle_info(timeout, State) -> {noreply, State}.
terminate(_Reason, _State) -> ok.
```
