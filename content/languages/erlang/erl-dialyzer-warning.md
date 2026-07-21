---
title: "Dialyzer warning and error in Erlang type analysis"
description: "Resolve Erlang Dialyzer warnings about type mismatches, underspecified functions, and contract violations."
languages: ["erlang"]
error-types: ["type-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Dialyzer errors are static analysis warnings indicating that the code has type inconsistencies, unreachable code paths, or functions that can never return certain values. Unlike compiler errors, Dialyzer analyzes the whole program.

## Common Causes

- Function spec declares a return type that the function can never produce
- Pattern matching on a value that Dialyzer knows cannot match
- Calling a function with an argument type that does not match the spec
- Using `catch` on an exception type that is never thrown
- Unreachable code after an always-true or always-false guard

## How to Fix

```erlang
%% WRONG: Spec says atom but function returns integer
-spec get_status() -> ok.
get_status() -> 42.
%% Dialyzer: function cannot return 42

%% CORRECT: Match spec to actual return
-spec get_status() -> integer().
get_status() -> 42.
```

```erlang
%% WRONG: Catching exception type never thrown
safe_div(A, B) ->
    try A div B of
        Result -> Result
    catch
        error:badarith -> 0  %% Dialyzer: only possible in certain cases
    end.

%% CORRECT: Catch all possible errors
safe_div(A, B) ->
    try A div B of
        Result -> Result
    catch
        error:badarith -> 0;
        error:badarg -> 0
    end.
```

## Examples

```erlang
%% Example 1: Underspecified function
-spec identity(X) -> X.
identity(X) -> X.  %% Dialyzer may warn about polymorphism

%% Example 2: Unreachable clause
-spec check(atom()) -> ok.
check(ok) -> ok;
check(error) -> ok;
check(other) -> ok.  %% Dialyzer: this clause may be unreachable

%% Example 3: Using Dialyzer from command line
%% dialyzer --plt .plt -r _build/default/lib/my_app/ebin/
```

## How to Debug

- Run dialyzer with `--Wunderspecs` for more detailed output
- Use `-Wunmatched_returns` to catch ignored return values
- Review the PLT (Persistent Lookup Table) is up to date
- Fix warnings from least severe to most severe

## Related Errors

- [Type spec error](erl-type-spec-error) -- incorrect -spec declarations
- [Type error](erl-type-error) -- runtime type mismatches
