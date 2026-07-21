---
title: "[Solution] Erlang Compile Error"
description: "Compilation errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Compile Error

Compilation errors.

### Common Causes
Wrong syntax; missing export; include

### How to Fix
```erlang
-module(my_module).
-export([func/1]).
func(X) -> X * 2.
```

### Examples
```erlang
$ erlc my_module.erl
$ erl -pa . -s my_module func -s init stop
```
