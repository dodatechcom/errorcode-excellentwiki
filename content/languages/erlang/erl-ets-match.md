---
title: "[Solution] Erlang ETS Match"
description: "ETS match/spec errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang ETS Match

ETS match/spec errors.

### Common Causes
Wrong match spec; key not found

### How to Fix
```erlang
ets:match_object(Tab, {'_', '_', value}).
```

### Examples
```erlang
ets:select(Tab, [{{'_', '_', '$1'}, [{'=:=', '$1', value}], ['$_']}]).
```
