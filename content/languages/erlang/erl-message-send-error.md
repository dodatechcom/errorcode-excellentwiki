---
title: "[Solution] Erlang Message Send"
description: "Message sending errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Message Send

Message sending errors.

### Common Causes
Wrong PID; message not received

### How to Fix
```erlang
Pid ! {self(), hello}.
receive
    {Pid, Reply} -> Reply
end.
```

### Examples
```erlang
spawn(fun() ->
    receive
        {From, Msg} -> From ! {self(), processed(Msg)}
    end
end).
```
