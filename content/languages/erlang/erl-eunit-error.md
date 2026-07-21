---
title: "[Solution] Erlang EUnit Error"
description: "EUnit test errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang EUnit Error

EUnit test errors.

### Common Causes
Missing include; wrong assertion

### How to Fix
```erlang
-include_lib("eunit/include/eunit.hrl").
add_test() -> ?assertEqual(4, add(2, 2)).
```

### Examples
```erlang
my_test_ ->
    [?_assertEqual(4, add(2, 2)),
     ?_assertError(badarith, 1/0)].
```
