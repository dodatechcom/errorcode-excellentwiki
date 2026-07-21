---
title: "[Solution] Erlang Ordsets"
description: "Ordered set errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Ordsets

Ordered set errors.

### Common Causes
Wrong operations; not sorted

### How to Fix
```erlang
Set1 = ordsets:from_list([1, 2, 3]),
Set2 = ordsets:from_list([2, 3, 4]),
Intersection = ordsets:intersection(Set1, Set2).
```

### Examples
```erlang
ordsets:add_element(4, Set1).
```
