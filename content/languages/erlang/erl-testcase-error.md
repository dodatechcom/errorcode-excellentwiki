---
title: "[Solution] Erlang Test Case"
description: "Test case definition errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Test Case

Test case definition errors.

### Common Causes
Missing assertion; wrong setup

### How to Fix
```erlang
my_test_ ->
    ?assertEqual(5, 2 + 3),
    ?assert(length([1,2,3]) =:= 3).
```

### Examples
```erlang
setup_test() ->
    ?assert(length([]) =:= 0),
    ?assert(lists:member(1, [1,2,3])).
```
