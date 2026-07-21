---
title: "[Solution] Erlang Guard Limits"
description: "Guard expression limitations."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Guard Limits

Guard expression limitations.

### Common Causes
Not boolean; limited expressions

### How to Fix
```erlang
% Guards cannot call arbitrary functions
is_valid(X) when is_integer(X), X > 0 -> true.
```

### Examples
```erlang
% Complex logic must be in the function body
check(X) ->
    case X of
        V when is_integer(V), V > 0 -> ok;
        _ -> error
    end.
```
