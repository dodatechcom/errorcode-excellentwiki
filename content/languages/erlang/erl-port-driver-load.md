---
title: "Erlang port driver loading error"
description: "Fix Erlang port driver loading failures when NIF or linked-in drivers cannot be initialized at runtime."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Port driver loading errors occur when Erlang cannot load a native code module (NIF shared library or linked-in driver) due to missing dependencies, incompatible architecture, or incorrect initialization.

## Common Causes

- Shared library (.so) file not found in code path
- Missing system library dependencies (libssl, libc, etc.)
- Architecture mismatch (32-bit driver on 64-bit BEAM or vice versa)
- Driver init function returns error code
- Insufficient memory to load the driver

## How to Fix

```erlang
%% WRONG: Incorrect library path
erlang:load_nif("/wrong/path/libdriver.so", 0).
%% {error, {open, _}}

%% CORRECT: Use code:priv_dir to find correct path
PrivDir = code:priv_dir(my_app),
LibPath = filename:join([PrivDir, "lib", "libdriver.so"]),
case erlang:load_nif(LibPath, 0) of
    ok -> ok;
    {error, {reload, _}} -> ok;  %% already loaded
    {error, Reason} -> {error, Reason}
end.
```

```erlang
%% WRONG: Not handling load failure
{ok, _} = erlang:load_nif(LibPath, 0).  %% crashes on failure

%% CORRECT: Graceful fallback
case erlang:load_nif(LibPath, 0) of
    ok -> 
        io:format("NIF loaded~n");
    {error, Reason} -> 
        io:format("NIF load failed: ~p~n", [Reason]),
        %% implement pure Erlang fallback
        ok
end.
```

## Examples

```erlang
%% Example 1: NIF module initialization
-module(my_nif).
-export([fast_compute/1]).

init() ->
    PrivDir = code:priv_dir(my_app),
    LibPath = filename:join(PrivDir, "my_nif"),
    erlang:load_nif(LibPath, 0).

fast_compute(_) ->
    erlang:nif_error(nif_not_loaded).

%% Example 2: Check NIF loaded
is_nif_loaded() ->
    try fast_compute(1) of
        _ -> true
    catch
        error:nif_not_loaded -> false
    end.

%% Example 3: Driver info
erlang:system_info(otp_release).  %% check BEAM version compatibility
```

## Related Errors

- [NIF error](erl-nif-error) -- NIF-specific runtime issues
- [Port error](erl-port-error) -- port communication failures
