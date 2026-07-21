---
title: "[Solution] Erlang Pattern Match"
description: "Pattern match fails at runtime."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Pattern Match

Pattern match fails at runtime.

### Common Causes
Clause doesn't match; wrong pattern

### How to Fix
```erlang
factorial(0) -> 1;
factorial(N) when N > 0 -> N * factorial(N - 1).
```

### Examples
```erlang
handle({ok, Value}) -> Value;
handle({error, Reason}) -> error(Reason).
```
