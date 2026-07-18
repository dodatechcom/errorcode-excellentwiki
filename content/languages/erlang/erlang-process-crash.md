---
title: "[Solution] Fix process terminated with reason crash in Erlang"
description: "Resolve Erlang process crashes by adding error handling in gen_server callbacks, trapping exits with process_flag, and configuring OTP supervision trees."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A process crash error occurs when an Erlang process terminates abnormally, printing the process identifier and termination reason. In OTP applications, this is often accompanied by supervisor reports.

The error appears as:

```erlang
=ERROR REPORT==== 12-Jan-2025::14:30:22 ===
    Process <0.123.0> with 0 neighbours crashed
    with reason: function_clause
```

## Why It Happens

This error occurs due to unhandled exceptions in processes:

- Unhandled exceptions in gen_server callbacks
- No function clause matching in the process logic
- Bad argument passed to a process via message passing
- Process dictionary access to non-existent keys
- Linked process crashes propagating the exit signal

## How to Fix It

Add proper error handling in gen_server callbacks:

```erlang
-module(my_gen_server).
-behaviour(gen_server).

handle_call({process, Data}, _From, State) ->
    try
        Result = do_processing(Data),
        {reply, {ok, Result}, State}
    catch
        error:Reason ->
            {reply, {error, Reason}, State};
        exit:Reason ->
            {stop, Reason, State}
    end;
handle_call(_Request, _From, State) ->
    {reply, {error, unknown_request}, State}.
```

Trap exits to handle linked process crashes gracefully:

```erlang
init(_) ->
    process_flag(trap_exit, true),
    {ok, #{}}.

handle_info({'EXIT', Pid, Reason}, State) ->
    io:format("Linked process ~p exited: ~p~n", [Pid, Reason]),
    {noreply, State}.
```

Use supervisors to restart failed processes:

```erlang
-module(my_supervisor).
-behaviour(supervisor).

init(_) ->
    Children = [
        #{
            id => worker,
            start => {my_worker, start_link, []},
            restart => transient,
            type => worker,
            modules => [my_worker]
        }
    ],
    {ok, {#{strategy => one_for_one, intensity => 5, period => 10}, Children}}.
```

Handle message passing errors:

```erlang
%% WRONG: Assuming message format
loop(State) ->
    receive
        {process, Data} ->
            Result = Data  %% crashes if Data is not expected format
    end,
    loop(State).

%% CORRECT: Handle unexpected messages
loop(State) ->
    receive
        {process, Data} when is_list(Data) ->
            Result = process_data(Data),
            loop(#{result => Result});
        {process, Other} ->
            io:format("Unexpected data format: ~p~n", [Other]),
            loop(State);
        {'EXIT', _Pid, Reason} ->
            io:format("Linked exit: ~p~n", [Reason]);
        Other ->
            io:format("Unknown message: ~p~n", [Other]),
            loop(State)
    end.
```

## Common Mistakes

- Not setting `process_flag(trap_exit, true)` in supervisor-linked processes
- Using `exit(Pid, Reason)` without understanding the exit signal semantics
- Ignoring warning reports in the Erlang error logger
- Not implementing proper `terminate/2` callbacks in gen_servers
- Choosing the wrong supervision strategy for process dependency trees

## Related Pages

- [Function clause matching failed](/languages/erlang/erlang-functionclause)
- [badarg: bad argument in function call](/languages/erlang/badarg)
- [Supervisor terminated children](/languages/erlang/erlang-supervisor-restart)
