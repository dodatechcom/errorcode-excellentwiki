---
title: "[Solution] Erlang Supervisor Tree"
description: "Supervisor tree construction errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Supervisor Tree

Supervisor tree construction errors.

### Common Causes
Wrong strategy; child spec

### How to Fix
```erlang
init(_) ->
    Children = [
        #{id => worker1, start => {worker1, start_link, []}}
    ],
    {ok, {#{strategy => one_for_one}, Children}}.
```

### Examples
```erlang
start_link(Args) ->
    supervisor:start_link({local, ?MODULE}, ?MODULE, Args).
```
