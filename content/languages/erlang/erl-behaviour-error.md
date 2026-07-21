---
title: "[Solution] Erlang Behaviour Error"
description: "Behaviour callback errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Behaviour Error

Behaviour callback errors.

### Common Causes
Missing callback; wrong return

### How to Fix
```erlang
-behaviour(gen_server).
init([]) -> {ok, State}.
```

### Examples
```erlang
handle_call(ping, _From, State) ->
    {reply, pong, State}.
```
