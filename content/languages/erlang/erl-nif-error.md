---
title: "[Solution] Erlang NIF Error"
description: "Native Implemented Functions errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang NIF Error

Native Implemented Functions errors.

### Common Causes
Load error; wrong C code; crash

### How to Fix
```erlang
-nif(add/2).
add(A, B) -> erlang:nif_error(nif_not_loaded).
```

### Examples
```erlang
init() ->
    erlang:load_nif(filename:join("priv", "my_nif"), 0).
```
