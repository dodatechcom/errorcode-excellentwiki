---
title: "[Solution] Erlang Cowboy WebSocket"
description: "Cowboy websocket errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Cowboy WebSocket

Cowboy websocket errors.

### Common Causes
Wrong callback; missing frames

### How to Fix
```erlang
init(Req, State) ->
    {cowboy_websocket, Req, State}.
```

### Examples
```erlang
websocket_init(State) -> {ok, State}.
websocket_handle({text, Msg}, State) ->
    {reply, {text, <<"echo: ", Msg/binary>>}, State}.
```
