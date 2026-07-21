---
title: "[Solution] Erlang List Comprehension"
description: "List comprehension errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang List Comprehension

List comprehension errors.

### Common Causes
Wrong syntax; guard issues

### How to Fix
```erlang
[X * 2 || X <- [1, 2, 3]].
```

### Examples
```erlang
[X || X <- [1..10], X rem 2 =:= 0].
```
