---
title: "[Solution] Erlang Function Clause"
description: "No function clause matching arguments."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Function Clause

No function clause matching arguments.

### Common Causes
Missing clause; wrong pattern; guard failure

### How to Fix
```erlang
add(X, Y) -> X + Y.
```

### Examples
```erlang
my_func(A) when is_integer(A) -> A * 2;
my_func(A) when is_list(A) -> length(A).
```
