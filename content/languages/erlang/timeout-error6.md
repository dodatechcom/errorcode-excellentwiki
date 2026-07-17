---
title: "timeout error"
description: "A timeout error occurs when a receive statement or synchronous call exceeds the specified time limit."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A timeout error occurs when a `receive` expression or a synchronous function call (like `gen_server:call`) doesn't receive a matching message within the specified timeout period. This is common in concurrent and distributed Erlang programming.

## Common Causes

- Receive statement with too short timeout
- Process not sending expected response
- Network delays in distributed systems
- Deadlock between processes

## How to Fix

```erlang
%% WRONG: Too short timeout
receive
    {response, Msg} -> Msg
after 100 ->  %% 100ms too short
    timeout
end.

%% CORRECT: Increase timeout or handle gracefully
receive
    {response, Msg} -> Msg
after 5000 ->  %% 5 seconds
    {error, timeout}
end.
```

```erlang
%% WRONG: gen_server call without timeout
gen_server:call(ServerRef, {do_something, Data}).  %% default 5000ms

%% CORRECT: Set appropriate timeout
gen_server:call(ServerRef, {do_something, Data}, 30000).  %% 30 seconds
```

## Examples

```erlang
%% Example 1: Receive timeout
Pid = spawn(fun() ->
    receive
        go -> ok
    after 1000 ->
        timeout
    end
end),
%% If no message sent in 1 second, returns timeout

%% Example 2: gen_server timeout
try gen_server:call(registered_name, request, 100)
catch
    exit:{timeout, _} -> io:format("Server timed out~n")
end.

%% Example 3: httpc timeout
httpc:request(get, {"http://example.com", []}, [{timeout, 5000}], []).
```

## Related Errors

- [noproc error](/languages/erlang/noproc)
- [badarg: error: bad argument in call to X](/languages/erlang/badarg)
