---
title: "[Solution] Erlang Rebar3 Error"
description: "Rebar3 command errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Rebar3 Error

Rebar3 command errors.

### Common Causes
Wrong command; missing plugin

### How to Fix
```shell
$ rebar3 new app my_app
$ rebar3 compile
$ rebar3 release
```

### Examples
```shell
$ rebar3 upgrade cowboy
$ rebar3 tree
```
