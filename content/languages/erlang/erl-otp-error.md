---
title: "[Solution] Erlang OTP Behavior"
description: "OTP behavior errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang OTP Behavior

OTP behavior errors.

### Common Causes
Wrong callback; gen_server; supervisor

### How to Fix
```erlang
-behaviour(gen_server).
-export([init/1, handle_call/3, handle_cast/2]).
init([]) -> {ok, #{}}.
handle_call(ping, _From, State) -> {reply, pong, State}.
```

### Examples
```erlang
start_link() ->
    gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).
```
