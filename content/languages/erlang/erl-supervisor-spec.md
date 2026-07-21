---
title: "Supervisor spec error in Erlang OTP"
description: "Fix Erlang supervisor specification errors when defining child specs or restart strategies incorrectly."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A supervisor spec error occurs when the child specification or supervisor startup arguments are malformed. OTP supervisors are strict about the format of child specs, and errors here prevent the supervision tree from starting.

## Common Causes

- Missing required fields in child specification like `id` or `start`
- Using an invalid `restart` strategy (must be `permanent`, `transient`, or `temporary`)
- Specifying a `shutdown` value incompatible with the child type
- Module does not implement the expected callback interface
- Incorrect `modules` list in the child spec

## How to Fix

```erlang
%% WRONG: Missing required 'start' field
#{
    id => my_worker,
    type => worker
    %% missing 'start' key

%% CORRECT: Include all required fields
#{
    id => my_worker,
    start => {my_worker, start_link, []},
    restart => permanent,
    shutdown => 5000,
    type => worker,
    modules => [my_worker]
}.
```

```erlang
%% WRONG: Invalid restart strategy
{ok, {{one_for_onee, 5, 10}, [ChildSpec]}}.
%% typo in 'one_for_onee'

%% CORRECT: Valid restart strategies
{ok, {{one_for_one, 5, 10}, [ChildSpec]}}.
%% or one_for_all, rest_for_one
```

## Examples

```erlang
%% Example 1: Complete supervisor module
-module(my_sup).
-behaviour(supervisor).
-export([start_link/0, init/1]).

start_link() ->
    supervisor:start_link({local, ?MODULE}, ?MODULE, []).

init([]) ->
    Child = #{
        id => worker1,
        start => {my_worker, start_link, []},
        restart => permanent,
        shutdown => 5000,
        type => worker,
        modules => [my_worker]
    },
    {ok, {{one_for_one, 5, 10}, [Child]}}.

%% Example 2: Supervisor with multiple children
init([]) ->
    Children = [
        #{id => db, start => {db_pool, start_link, []}, type => supervisor},
        #{id => cache, start => {cache_server, start_link, []}, type => worker}
    ],
    {ok, {{rest_for_one, 5, 10}, Children}}.
```

## Related Errors

- [Supervisor restart error](erlang-supervisor-restart) -- child keeps crashing
- [GenServer error](erl-genserver-error) -- process initialization failures
