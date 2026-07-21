---
title: "[Solution] Erlang Type Error"
description: "Type specification errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Type Error

Type specification errors.

### Common Causes
Wrong type; spec doesn't match implementation

### How to Fix
```erlang
-spec func(integer()) -> integer().
func(X) -> X * 2.
```

### Examples
```erlang
-spec add(integer(), integer()) -> integer().
add(A, B) -> A + B.
```
