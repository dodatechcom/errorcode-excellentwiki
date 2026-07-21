---
title: "[Solution] Erlang IO Format"
description: "io:format errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang IO Format

io:format errors.

### Common Causes
Wrong format string; argument count

### How to Fix
```erlang
io:format("Hello ~s~n", ["World"]).
io:format("Value: ~p~n", [42]).
```

### Examples
```erlang
io:format("~w~n", [List]).  % raw format
io:format("~p~n", [List]).  % pretty format
```
