---
title: "[Solution] Erlang Orddict"
description: "Ordered dictionary errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Orddict

Ordered dictionary errors.

### Common Causes
Key not found; wrong operations

### How to Fix
```erlang
Dict = orddict:new(),
Dict1 = orddict:store(key1, value1, Dict),
{ok, Value} = orddict:find(key1, Dict1).
```

### Examples
```erlang
orddict:update_counter(counter, 1, Dict).
```
