---
title: "[Solution] Erlang Release Error"
description: "Release building errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Release Error

Release building errors.

### Common Causes
Wrong config; missing relx

### How to Fix
```erlang
{relx, [
    {release, {my_app, "1.0"}, [my_app, sasl]},
    {dev_mode, true},
    {include_erts, false}
]}.
```

### Examples
```shell
$ rebar3 release
$ _build/default/rel/my_app/bin/my_app
```
