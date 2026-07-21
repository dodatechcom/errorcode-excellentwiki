---
title: "[Solution] Erlang Cowboy Error"
description: "Cowboy web framework errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Cowboy Error

Cowboy web framework errors.

### Common Causes
Wrong router; handler issues

### How to Fix
```erlang
router = cowboy_router:compile([
    {'_', [{"/", index_handler, []}]}
]),
{ok, _} = cowboy:start_clear(my_http_listener, [{port, 8080}], #{env => #{dispatch => router}}).
```

### Examples
```erlang
init(Req, State) ->
    Req2 = cowboy_req:reply(200, #{"content-type" => "text/plain"}, "Hello", Req),
    {ok, Req2, State}.
```
