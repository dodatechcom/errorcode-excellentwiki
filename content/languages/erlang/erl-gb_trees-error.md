---
title: "[Solution] Erlang GB Trees"
description: "GB trees errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang GB Trees

GB trees errors.

### Common Causes
Key not found; not ordered

### How to Fix
```erlang
Tree = gb_trees:empty(),
Tree1 = gb_trees:insert(key1, value1, Tree),
Value = gb_trees:get(key1, Tree1).
```

### Examples
```erlang
{value, Value} = gb_trees:lookup(key1, Tree).
```
