---
title: "[Solution] Erlang Rebar Error"
description: "Rebar3 build tool errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Rebar Error

Rebar3 build tool errors.

### Common Causes
Wrong config; missing dependency

### How to Fix
```erlang
{deps, [
    {cowboy, "2.10.0"}
]}.
```

### Examples
```shell
$ rebar3 compile
$ rebar3 shell
```
