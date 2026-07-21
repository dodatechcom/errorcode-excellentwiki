---
title: "[Solution] Erlang ETS Error"
description: "ETS table operations errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang ETS Error

ETS table operations errors.

### Common Causes
Wrong table type; key not found; full

### How to Fix
```erlang
Tab = ets:new(my_table, [set, public]),
ets:insert(Tab, {key, value}),
[{key, Value}] = ets:lookup(Tab, key).
```

### Examples
```erlang
ets:delete(Tab).
```
