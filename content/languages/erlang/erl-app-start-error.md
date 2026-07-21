---
title: "Application start error in Erlang release"
description: "Fix Erlang application start failures when the application callback module returns invalid start spec."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An application start error occurs when an OTP application's `mod` callback (usually `start/2`) returns a value that does not match the expected `{ok, Pid}` or `{ok, Pid, State}` format, or when the supervision tree fails to initialize.

## Common Causes

- `start/2` function returns `ok` instead of `{ok, Pid}`
- The application resource file (.app) has incorrect `mod` specification
- Supervision tree startup fails due to child spec errors
- Required applications are not listed in the `applications` key
- Environment variables are missing or have wrong types

## How to Fix

```erlang
%% WRONG: start/2 returns wrong format
start(_StartType, _StartArgs) ->
    ok.
%% error: expected {ok, Pid} or {ok, Pid, State}

%% CORRECT: Return proper start specification
start(_StartType, _StartArgs) ->
    my_sup:start_link().
```

```erlang
%% WRONG: .app file missing applications key
{application, my_app, [
    {vsn, "1.0.0"},
    {mod, {my_app, []}}
    %% missing 'applications' key
]}.

%% CORRECT: List all required applications
{application, my_app, [
    {vsn, "1.0.0"},
    {applications, [kernel, stdlib, mnesia]},
    {mod, {my_app, []}}
]}.
```

## Examples

```erlang
%% Example 1: Application module callback
-module(my_app).
-behaviour(application).
-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    case my_sup:start_link() of
        {ok, Pid} -> {ok, Pid};
        Error -> Error
    end.

stop(_State) -> ok.

%% Example 2: Using application:get_env
init_config() ->
    case application:get_env(my_app, db_host) of
        {ok, Host} -> Host;
        undefined -> "localhost"
    end.
```

## Related Errors

- [Supervisor spec error](erl-supervisor-spec) -- child spec problems
- [OTP error](erl-otp-error) -- general OTP framework issues
