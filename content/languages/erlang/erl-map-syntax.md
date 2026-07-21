---
title: "[Solution] Erlang Map Syntax"
description: "Map syntax errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Map Syntax

Map syntax errors.

### Common Causes
Wrong keys; missing values

### How to Fix
```erlang
#{key => value}.
#{key := Existing} = Map.
```

### Examples
```erlang
UpdatedMap = OldMap#{new_key := new_value, another_key => value}.
```
