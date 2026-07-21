---
title: "[Solution] Erlang Receive Error"
description: "receive block errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Receive Error

receive block errors.

### Common Causes
Missing after; infinite wait; wrong message

### How to Fix
```erlang
receive
    {ok, Data} -> {ok, Data};
    {error, Reason} -> {error, Reason}
after 5000 -> {error, timeout}
end.
```

### Examples
```erlang
receive
    stop -> ok;
    {process, Msg} -> handle(Msg)
after 1000 -> timeout
end.
```
