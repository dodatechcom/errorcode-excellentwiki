---
title: "[Solution] Erlang Macro Error"
description: "Macro definition and usage errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Macro Error

Macro definition and usage errors.

### Common Causes
Missing define; wrong expansion

### How to Fix
```erlang
-define(MAX(A, B), if A > B -> A; true -> B end).
```

### Examples
```erlang
-define(LOG(Msg), io:format("~p~n", [Msg])).
```
