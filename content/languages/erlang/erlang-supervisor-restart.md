---
title: "[Solution] Fix supervisor terminated children error in Erlang"
description: "Resolve Erlang supervisor crashes by tuning restart intensity and period, choosing correct supervision strategies, and fixing child spec configuration."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A supervisor termination error occurs when an OTP supervisor terminates all its children and then shuts down, usually because the maximum restart intensity has been exceeded. This indicates a child process is repeatedly crashing.

The error appears as:

```erlang
=SUPERVISOR REPORT==== 12-Jan-2025::14:30:22 ===
    Supervisor: {local, my_supervisor}
    Context:    child_terminated
    Reason:     {badarg, [{module, function, 1, [...]}]}
    Offender:   [{pid, <0.123.0>}, {name, my_worker}, ...]
```

## Why It Happens

This error occurs due to repeated child process crashes:

- Child process crashes faster than supervisor can recover
- Intensity threshold (5 restarts in 10 seconds) is exceeded
- Child spec has wrong arguments causing immediate crash on start
- Dependent resources (databases, files) are unavailable
- Bug in child process init causes repeated failures

## How to Fix It

Adjust supervisor intensity for expected transient failures:

```erlang
init(_) ->
    Children = [#{id => worker, start => {worker, start_link, []}, type => worker}],
    Strategy = #{
        strategy => one_for_one,
        intensity => 10,     %% Allow 10 restarts
        period => 60         %% Within 60 seconds
    },
    {ok, {Strategy, Children}}.
```

Use appropriate restart strategies:

```erlang
%% one_for_one: Only the crashed child restarts
#{strategy => one_for_one}

%% rest_for_one: Crashed child and all children started after it restart
#{strategy => rest_for_one}

%% one_for_all: All children restart when any crashes
#{strategy => one_for_all}
```

Fix child spec arguments:

```erlang
%% WRONG: Wrong arguments cause immediate crash
#{id => worker,
  start => {worker, start_link, [wrong_arg]},
  type => worker}

%% CORRECT: Verify arguments match start_link/1
#{id => worker,
  start => {worker, start_link, [correct_arg]},
  type => worker}
```

Add init error handling in child process:

```erlang
-module(my_worker).
-behaviour(gen_server).

init(Args) ->
    try
        {ok, init_state(Args)}
    catch
        error:Reason ->
            io:format("Worker init failed: ~p~n", [Reason]),
            {stop, Reason}
    end.
```

Use `temporary` restart type for non-critical processes:

```erlang
#{id => worker,
  start => {worker, start_link, []},
  restart => temporary,  %% Does not restart on crash
  type => worker}
```

Check for cyclic dependencies in supervision tree:

```erlang
%% Ensure workers do not depend on each other through the supervisor
%% Use application order to handle dependencies
```

## Common Mistakes

- Using `one_for_all` strategy when processes are independent
- Not testing child spec arguments before deploying
- Defaulting to `permanent` restart for non-critical workers
- Not monitoring supervisor status in production systems
- Forgetting that `temporary` processes never restart, even on abnormal exit
- Not accounting for resource availability during child init

## Related Pages

- [Application start failed](/languages/erlang/erlang-application-failed)
- [Process terminated with reason crash](/languages/erlang/erlang-process-crash)
- [gen_server call timed out](/languages/erlang/erlang-timeout-error)
