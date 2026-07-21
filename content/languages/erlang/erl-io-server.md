---
title: "[Solution] Erlang IO Server"
description: "IO server errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang IO Server

IO server errors.

### Common Causes
Wrong protocol; not implementing callbacks

### How to Fix
```erlang
start_link() ->
    gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).
```

### Examples
```erlang
init([]) -> {ok, #{}}.
handle_call({io_request, From, ReplyAs, Request}, _From, State) ->
    handle_io_request(From, ReplyAs, Request, State).
```
