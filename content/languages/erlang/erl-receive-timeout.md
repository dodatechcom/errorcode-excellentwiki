---
title: "Timer and timeout error in Erlang receive"
description: "Fix Erlang timer and receive timeout errors when message passing uses incorrect timeout specifications."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Timeout errors in receive expressions occur when a process waits for a message that never arrives within the specified time. The receive block's timeout clause fires, but if the logic does not handle it properly, the process may crash or enter an unexpected state.

## Common Causes

- Forgetting to include an `after` clause in a receive that needs timeout
- The sender process crashes before sending the expected reply
- Message is consumed by a different receive in the same process
- Timeout value is too short for network or processing delays
- Using `infinity` timeout that blocks the process forever

## How to Fix

```erlang
%% WRONG: No timeout clause
receive
    {reply, Result} -> Result
end.
%% blocks forever if sender never replies

%% CORRECT: Add timeout handling
receive
    {reply, Result} -> Result
after 5000 ->
    {error, timeout}
end.
```

```erlang
%% WRONG: Timeout too short for distributed system
call(Node, Msg) ->
    Ref = make_ref(),
    {Node, server} ! {self(), Ref, Msg},
    receive
        {Ref, Result} -> Result
    after 100 ->  %% 100ms too short for network
        {error, timeout}
    end.

%% CORRECT: Use appropriate timeout
call(Node, Msg) ->
    Ref = make_ref(),
    {Node, server} ! {self(), Ref, Msg},
    receive
        {Ref, Result} -> Result
    after 10000 ->  %% 10 seconds
        {error, timeout}
    end.
```

## Examples

```erlang
%% Example 1: Selective receive with timeout
loop() ->
    receive
        {data, D} -> process(D), loop();
        stop -> ok
    after 60000 ->
        io:format("No messages for 60 seconds, exiting~n"),
        ok
    end.

%% Example 2: Monitor-based timeout
call_server(Pid, Msg) ->
    Ref = monitor(process, Pid),
    Pid ! {self(), Msg},
    receive
        {reply, Ref, Result} ->
            demonitor(Ref, [flush]),
            Result;
        {'DOWN', Ref, process, Pid, Reason} ->
            {error, {server_died, Reason}}
    after 30000 ->
        demonitor(Ref, [flush]),
        {error, timeout}
    end.
```

## Related Errors

- [Timeout error](erlang-timeout-error) -- general timeout issues
- [Process crash](erlang-process-crash) -- processes dying unexpectedly
- [GenServer timeout](erl-genserver-timeout) -- GenServer-specific timeouts
