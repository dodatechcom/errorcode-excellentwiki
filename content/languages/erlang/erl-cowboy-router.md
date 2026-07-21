---
title: "[Solution] Erlang Cowboy Router"
description: "Cowboy router errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Cowboy Router

Cowboy router errors.

### Common Causes
Wrong dispatch; handler not found

### How to Fix
```erlang
Dispatch = cowboy_router:compile([
    {'_', [
        {"/", index_handler, []},
        {"/api/:action", api_handler, []}
    ]}
]),
{ok, _} = cowboy:start_clear(my_http, [{port, 8080}], #{env => #{dispatch => Dispatch}}).
```

### Examples
```erlang
init(Req, State) ->
    Action = cowboy_req:binding(action, Req),
    handle(Action, Req, State).
```
