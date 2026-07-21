---
title: "[Solution] Erlang Syntax Error"
description: "Erlang parser encounters invalid syntax."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Syntax Error

Erlang parser encounters invalid syntax.

### Common Causes
Missing period; wrong bracket; semicolon misuse

### How to Fix
```erlang
X = 5,
Y = X + 1.
```

### Examples
```erlang
-module(my_module).
-export([my_function/0]).
my_function() -> ok.
```
