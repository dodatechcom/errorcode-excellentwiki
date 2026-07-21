---
title: "GenServer call timeout error in Erlang"
description: "Fix Erlang GenServer timeout errors when gen_server:call exceeds the default or specified timeout value."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A GenServer call timeout occurs when `gen_server:call/2` or `gen_server:call/3` does not receive a reply within the specified timeout period. The calling process receives `{timeout, ...}` and terminates unless caught.

## Common Causes

- The GenServer process is blocked in a long-running operation
- Deadlock where two GenServers call each other simultaneously
- GenServer process has crashed and is not responding
- Using default 5000ms timeout for operations that need more time
- Too many messages queued in the GenServer's mailbox

## How to Fix

```erlang
%% WRONG: Using default timeout for slow operation
Result = gen_server:call(server_name, {slow_computation, Data}).
%% timeout after 5000ms if computation is slow

%% CORRECT: Specify a longer timeout
Result = gen_server:call(server_name, {slow_computation, Data}, 60000).
```

```erlang
%% WRONG: Deadlock between two servers
%% Server A calls Server B while Server B calls Server A
handle_call({query, From}, _From, State) ->
    Result = gen_server:call(From, {result, self()}),
    {reply, Result, State}.

%% CORRECT: Use gen_server:cast or asynchronous patterns
handle_call({query, From}, _From, State) ->
    gen_server:cast(From, {result, self()}),
    {reply, ok, State}.
```

## Examples

```erlang
%% Example 1: Handling timeout gracefully
try
    Result = gen_server:call(my_server, fetch_data, 10000),
    Result
catch
    exit:{timeout, _} ->
        io:format("Server did not respond in time~n"),
        {error, timeout}
end.

%% Example 2: infinity timeout for critical operations
Config = gen_server:call(config_server, get_config, infinity).

%% Example 3: Supervised GenServer with timeout
init([]) ->
    {ok, #{}, 0}.  %% timeout of 0 triggers handle_info immediately
```

## Related Errors

- [GenServer error](erl-genserver-error) -- general GenServer issues
- [Timeout error](erlang-timeout-error) -- other timeout scenarios
- [Process crash](erlang-process-crash) -- GenServer process dying
