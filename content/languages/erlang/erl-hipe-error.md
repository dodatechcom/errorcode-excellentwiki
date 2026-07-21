---
title: "[Solution] Erlang HiPE Error"
description: "High Performance Erlang errors"
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang HiPE Error

High Performance Erlang errors

### Common Causes
Compilation issues; incompatibility

### How to Fix
```erlang
-compile([native, {hipe, [o3]}]).
```

### Examples
```erlang
$ erlc +native +"{hipe, [o3]}" my_module.erl
```
