---
title: "Erlang catch and try expression error"
description: "Fix Erlang try-catch expression errors when exception classes or pattern matches in catch clauses are invalid."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Try-catch expression errors occur when the syntax of the `try ... of ... catch ... after ... end` block is invalid, such as using incorrect exception class names or malformed pattern matching in catch clauses.

## Common Causes

- Using `error` instead of `throw`, `exit`, or `error` in catch clauses
- Missing the `of` keyword between expression and pattern match
- Catch clause patterns do not match the exception format
- Using `catch` without `try`
- After clause placed before catch clause

## How to Fix

```erlang
%% WRONG: Catch clause uses wrong class
try risky_operation() of
    Result -> Result
catch
    exception:Reason -> {error, Reason}
    %% 'exception' is not a valid class
end.

%% CORRECT: Use throw, exit, or error
try risky_operation() of
    Result -> Result
catch
    error:Reason -> {error, Reason};
    throw:Reason -> {caught, Reason};
    exit:Reason -> {exit, Reason}
end.
```

```erlang
%% WRONG: Catch without try
catch some_function().  %% syntax error

%% CORRECT: Use try-catch
try some_function() of
    Val -> Val
catch
    _:_ -> error_value
end.
```

## Examples

```erlang
%% Example 1: Basic try-catch
try list_to_integer("abc") of
    N -> N
catch
    error:badarg -> {error, not_a_number}
end.

%% Example 2: Catch with wildcard
try risky() of
    ok -> success
catch
    _:_ -> failure  %% catches any exception
end.

%% Example 3: Try-catch-after
try file:read_file("data.txt") of
    {ok, Data} -> Data
catch
    error:Reason -> {error, Reason}
after
    cleanup_resources()
end.
```

## Related Errors

- [Try-catch error](erl-try-catch) -- exception handling patterns
- [Badmatch error](badmatch) -- match failures in try-of clause
