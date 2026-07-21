---
title: "[Solution] Erlang Fun Error"
description: "Anonymous function errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Fun Error

Anonymous function errors.

### Common Causes
Wrong syntax; capture; clause mismatch

### How to Fix
```erlang
F = fun(X) -> X * 2 end,
lists:map(F, [1, 2, 3]).
```

### Examples
```erlang
apply(fun(A, B) -> A + B end, [3, 4]).
```
