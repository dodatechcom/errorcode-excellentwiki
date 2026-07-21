---
title: "Application environment variable error in Erlang"
description: "Fix Erlang application:get_env errors when accessing undefined or incorrectly typed environment variables."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An environment variable error occurs when `application:get_env/2` or `application:get_env/3` returns `undefined` because the variable was never set, or when the value has an unexpected type.

## Common Causes

- Variable not set in the .app file or via `application:set_env`
- Typo in the variable name
- Variable is set for a different application
- Value is the wrong type (atom when string expected)
- Application has not started yet when the variable is queried

## How to Fix

```erlang
%% WRONG: Not handling undefined case
{ok, Host} = application:get_env(my_app, db_host),
%% crashes if db_host is not set

%% CORRECT: Provide default value
Host = application:get_env(my_app, db_host, "localhost").
```

```enrl
%% WRONG: Assuming correct type
Port = application:get_env(my_app, port),
%% could be {ok, "8080"} instead of {ok, 8080}

%% CORRECT: Validate and convert
case application:get_env(my_app, port) of
    {ok, Port} when is_integer(Port) -> Port;
    {ok, PortStr} when is_list(PortStr) -> list_to_integer(PortStr);
    _ -> 8080
end.
```

## Examples

```erlang
%% Example 1: Setting environment variables
application:set_env(my_app, db_host, "db.example.com"),
application:set_env(my_app, db_port, 5432).

%% Example 2: Loading from sys.config
%% {my_app, [{db_host, "localhost"}, {db_port, 5432}]}.

%% Example 3: Required variable check at startup
require_env(Key) ->
    case application:get_env(my_app, Key) of
        {ok, Val} -> Val;
        undefined -> error({missing_config, Key})
    end.

DbHost = require_env(db_host).
```

## Related Errors

- [Application start error](erl-app-start-error) -- application startup failures
- [OTP error](erl-otp-error) -- general OTP configuration issues
