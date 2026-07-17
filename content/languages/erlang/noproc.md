---
title: "error: noproc"
description: "A noproc error occurs when trying to send a message or make a call to a process that doesn't exist."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `noproc` error is raised when you try to send a message to, or make a synchronous call to, a process that doesn't exist or has already terminated. This commonly happens with registered process names or stale PIDs.

## Common Causes

- Sending message to a terminated process
- Using a stale PID after process restart
- Calling registered process that was never started
- Typo in registered process name

## How to Fix

```erlang
%% WRONG: Sending to potentially dead process
Pid = whereis(my_server),
Pid ! {request, self()}.

%% CORRECT: Check if process exists first
case whereis(my_server) of
    undefined -> {error, not_started};
    Pid -> Pid ! {request, self()}
end.
```

```erlang
%% WRONG: gen_server call to non-existent process
gen_server:call(my_server, request).

%% CORRECT: Start process first or handle noproc
try gen_server:call(my_server, request)
catch
    exit:{noproc, _} -> {error, server_not_running}
end.
```

## Examples

```erlang
%% Example 1: Send to dead process
Pid = spawn(fun() -> ok end),
%% Process terminates immediately
Pid ! hello.
%% error: noproc

%% Example 2: Registered name not started
whereis(nonexistent).
%% undefined (no error, but subsequent message send will fail)

%% Example 3: gen_server call
gen_server:call(nonexistent_server, ping).
%% ** (exit) noproc
```

## Related Errors

- [timeout error](/languages/erlang/timeout-error6)
- [badarg: error: bad argument in call to X](/languages/erlang/badarg)
