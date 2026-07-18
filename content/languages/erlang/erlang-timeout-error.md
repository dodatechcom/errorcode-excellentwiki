---
title: "[Solution] Fix gen_server call timed out error in Erlang"
description: "Resolve gen_server timeout errors in Erlang by optimizing callback performance, adjusting call timeouts properly, and using async casts for non-blocking work."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A gen_server timeout error occurs when a synchronous call to a gen_server process does not receive a response within the specified timeout period. This is common when server callbacks take too long to complete.

The error appears as:

```erlang
{timeout, {gen_server, call, [Server, Request, Timeout]}}
```

or:

```erlang
** exit: {timeout, {gen_server, call, [my_server, get_state, 5000]}}
```

## Why It Happens

This error occurs when gen_server processes are too slow:

- Callback function performs blocking operations (file I/O, network calls)
- Server process is overloaded with too many requests
- Server process is stuck in an infinite loop
- Server is blocked waiting for another resource
- Default timeout of 5000ms is too short for the workload
- Server process priority is too low

## How to Fix It

Increase timeout for known slow operations:

```erlang
%% Default 5 second timeout may not be enough
gen_server:call(my_server, {slow_operation, Data}, 30000).
```

Use async calls when synchronous response is not needed:

```erlang
%% WRONG: Synchronous call for fire-and-forget
gen_server:call(my_server, {log_event, Event}).

%% CORRECT: Async cast for non-blocking notification
gen_server:cast(my_server, {log_event, Event}).
```

Optimize the gen_server callback:

```erlang
%% WRONG: Blocking I/O in callback
handle_call({read_file, Path}, _From, State) ->
    {ok, Data} = file:read_file(Path),  %% Blocks process
    {reply, {ok, Data}, State};

%% CORRECT: Offload heavy work or use async patterns
handle_call({read_file, Path}, _From, State) ->
    case file:read_file(Path) of
        {ok, Data} -> {reply, {ok, Data}, State};
        {error, Reason} -> {reply, {error, Reason}, State}
    end;
handle_call(_Request, _From, State) ->
    {reply, {error, unknown_request}, State}.
```

Use `gen_server:cast` for fire-and-forget operations:

```erlang
%% Fire-and-forget pattern
handle_cast({process_event, Event}, State) ->
    %% Do not reply - cast does not wait
    NewState = update_state(State, Event),
    {noreply, NewState}.
```

Monitor server health and queue length:

```erlang
handle_info(check_health, #{queue := Queue} = State) ->
    io:format("Queue length: ~p~n", [queue:len(Queue)]),
    {noreply, State}.
```

Use `gen_statem` for complex state machines with timeout handling:

```erlang
%% Built-in state timeout
state_name ->
    {next_state, next_state_name, NewData, [{state_timeout, 10000, trigger}]}.
```

## Common Mistakes

- Using `gen_server:call` for operations that do not need a synchronous response
- Not monitoring gen_server process health in production
- Defaulting to 5000ms timeout without considering workload requirements
- Blocking the gen_server process with large data processing
- Not using `gen_server:cast` for logging and metric collection

## Related Pages

- [Process terminated with reason crash](/languages/erlang/erlang-process-crash)
- [Application start failed](/languages/erlang/erlang-application-failed)
- [nodedown: no connection to node](/languages/erlang/erlang-nodedown)
