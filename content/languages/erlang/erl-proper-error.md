---
title: "[Solution] Erlang PropEr Testing"
description: "PropEr property-based testing errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang PropEr Testing

PropEr property-based testing errors.

### Common Causes
Wrong property; generator issues

### How to Fix
```erlang
-include_lib("proper/include/proper.hrl").
prop_add() ->
    ?FORALL({A, B}, {integer(), integer()},
        A + B =:= B + A).
```

### Examples
```erlang
-include_lib("proper/include/proper.hrl").
prop_list_reverse() ->
    ?FORALL(L, list(integer()),
        lists:reverse(lists:reverse(L)) =:= L).
```
