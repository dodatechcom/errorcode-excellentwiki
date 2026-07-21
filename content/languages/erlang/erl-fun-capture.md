---
title: "[Solution] Erlang Fun Capture"
description: "Function capture errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Fun Capture

Function capture errors.

### Common Causes
Wrong arity; module not loaded

### How to Fix
```erlang
F = fun lists:reverse/1,
F([1, 2, 3]).
```

### Examples
```erlang
F = fun ?MODULE:my_func/2,
F(Arg1, Arg2).
```
