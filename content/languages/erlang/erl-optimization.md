---
title: "[Solution] Erlang Optimization"
description: "Compiler optimization errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Optimization

Compiler optimization errors.

### Common Causes
Wrong optimization; performance

### How to Fix
```erlang
-module(my_module).
-compile([inline]).
```

### Examples
```erlang
% Tail recursion is optimized
sum(List) -> sum(List, 0).
sum([], Acc) -> Acc;
sum([H|T], Acc) -> sum(T, Acc + H).
```
