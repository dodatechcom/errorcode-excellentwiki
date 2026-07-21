---
title: "[Solution] Erlang Case Error"
description: "case expression errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Case Error

case expression errors.

### Common Causes
Missing clause; no match; wrong syntax

### How to Fix
```erlang
case Value of
    {ok, V} -> V;
    {error, E} -> error(E)
end.
```

### Examples
```erlang
case X of
    1 -> one;
    2 -> two;
    _ -> other
end.
```
