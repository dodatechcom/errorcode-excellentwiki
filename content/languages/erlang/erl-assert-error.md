---
title: "[Solution] Erlang Assert Error"
description: "Assert macro errors"
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Assert Error

Assert macro errors

### Common Causes
Assert in production; wrong use

### How to Fix
```erlang
-include_lib("eunit/include/eunit.hrl").
my_test() -> ?assert(1 + 1 =:= 2).
```

### Examples
```erlang
assert(Condition) when is_boolean(Condition) ->
    case Condition of true -> ok; false -> error(assertion_failed) end.
```
