---
title: "[Solution] Erlang Supervisor Error"
description: "Supervisor tree errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Supervisor Error

Supervisor tree errors.

### Common Causes
Wrong child spec; restart strategy

### How to Fix
```erlang
init(_) ->
    ChildSpec = #{
        id => my_worker,
        start => {my_worker, start_link, []},
        restart => permanent,
        type => worker
    },
    {ok, {#{strategy => one_for_one, intensity => 5, period => 10}, [ChildSpec]}}.
```

### Examples
```erlang
start_link() ->
    supervisor:start_link({local, ?MODULE}, ?MODULE, []).
```
