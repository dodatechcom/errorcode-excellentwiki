---
title: "[Solution] Fix application start failed error in Erlang"
description: "Resolve Erlang application start failures by verifying dependencies in .app.src, checking sys.config environment, and validating supervisor tree init."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 9
---

## What This Error Means

An application start error occurs when an OTP application fails to initialize. This typically happens during the `start/2` callback of the application behaviour or when supervisor tree setup fails.

The error appears as:

```erlang
{error, {bad_return_value, {error, Reason}}}
```

or:

```erlang
=CRASH REPORT==== 12-Jan-2025::14:30:22 ===
    application: my_app
    exited: {bad_start_type, permanent}
```

## Why It Happens

This error occurs during application initialization:

- Application callback `start/2` returns invalid format
- Required configuration is missing from sys.config
- Dependent applications fail to start first
- Supervisor child specs have errors
- Port or resource initialization fails
- Mnesia or database tables not created before start

## How to Fix It

Return correct format from application callback:

```erlang
-module(my_app).
-behaviour(application).

%% WRONG: Invalid return value
start(_StartType, _StartArgs) ->
    {error, something_went_wrong}.

%% CORRECT: Return supervisor PID
start(_StartType, _StartArgs) ->
    case my_supervisor:start_link() of
        {ok, Pid} -> {ok, Pid};
        {error, Reason} -> {error, Reason}
    end.
```

Ensure required configuration exists:

```erlang
%% In sys.config
[{my_app, [
    {host, "localhost"},
    {port, 8080}
]}].

%% In application module
start(_StartType, _StartArgs) ->
    case application:get_env(my_app, host) of
        {ok, Host} ->
            {ok, Pid} = my_supervisor:start_link(Host),
            {ok, Pid};
        undefined ->
            {error, missing_host_config}
    end.
```

List dependent applications in the app file:

```erlang
%% In my_app.app.src
{applications, [
    kernel,
    stdlib,
    sasl,
    crypto,
    ssl
]}.
```

Verify supervisor child specs:

```erlang
init(_) ->
    Children = [
        #{
            id => my_worker,
            start => {my_worker, start_link, []},
            restart => permanent,
            shutdown => 5000,
            type => worker,
            modules => [my_worker]
        }
    ],
    {ok, {#{strategy => one_for_one, intensity => 5, period => 10}, Children}}.
```

Test application start independently:

```erlang
%% Start application manually
application:ensure_all_started(my_app).

%% Check application status
application:which_applications().
```

## Common Mistakes

- Not returning `{ok, Pid}` from the application `start/2` callback
- Forgetting to list dependent applications in the `.app.src` file
- Using `permanent` restart type without a working supervisor
- Not handling errors from dependent application starts
- Missing environment variables in sys.config for production deployments

## Related Pages

- [Supervisor terminated children](/languages/erlang/erlang-supervisor-restart)
- [gen_server call timed out](/languages/erlang/erlang-timeout-error)
- [Process terminated with reason crash](/languages/erlang/erlang-process-crash)
