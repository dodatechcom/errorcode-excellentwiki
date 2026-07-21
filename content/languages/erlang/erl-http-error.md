---
title: "[Solution] Erlang HTTP Error"
description: "HTTP client/server errors (inets)."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang HTTP Error

HTTP client/server errors (inets).

### Common Causes
Wrong URL; SSL; timeout

### How to Fix
```erlang
inets:start(),
{ok, {{_, 200, _}, _, Body}} = httpc:request(get, {"https://example.com", []}, [], []).
```

### Examples
```erlang
ssl:start(),
{ok, Response} = httpc:request(get, {"https://api.example.com/data", []}, [{ssl, [{verify, verify_none}]}], []).
```
