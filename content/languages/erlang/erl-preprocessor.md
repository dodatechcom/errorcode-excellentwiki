---
title: "[Solution] Erlang Preprocessor"
description: "Preprocessor directive errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Preprocessor

Preprocessor directive errors.

### Common Causes
Wrong define; missing endif

### How to Fix
```erlang
-ifdef(DEBUG).
-define(LOG(X), io:format("~p~n", [X])).
-else.
-define(LOG(X), ok).
-endif.
```

### Examples
```erlang
-ifndef(MYMACRO).
-define(MYMACRO, value).
-endif.
```
