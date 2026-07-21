---
title: "[Solution] Erlang Proplists"
description: "Property list errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Proplists

Property list errors.

### Common Causes
Key not found; wrong access

### How to Fix
```erlang
Opts = [{key1, value1}, {key2, value2}],
Value = proplists:get_value(key1, Opts).
```

### Examples
```erlang
proplists:get_value(missing, Opts, default).
```
