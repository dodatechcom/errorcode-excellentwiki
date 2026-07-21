---
title: "[Solution] Erlang Mnesia Error"
description: "Mnesia database errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Mnesia Error

Mnesia database errors.

### Common Causes
Transaction failed; table not created

### How to Fix
```erlang
mnesia:create_table(user, [{attributes, [id, name, email]}]),
{atomic, ok} = mnesia:transaction(fun() ->
    mnesia:write(#user{id = 1, name = "John", email = "j@x.com"})
end).
```

### Examples
```erlang
{atomic, Results} = mnesia:transaction(fun() ->
    mnesia:match_object(#user{_ = '_'})
end).
```
