---
title: "try Expression Error in Erlang"
description: "Erlang try expressions raise errors when exception handling is incorrect"
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Errors in `try` expressions occur when exception handling is misconfigured, the wrong exception class is caught, or the `after` block itself throws an exception. Erlang's `try-catch` has specific syntax requirements.

## Common Causes

- Wrong exception class (error, throw, exit)
- Missing catch clause for expected exceptions
- After block throwing exceptions
- Stack trace not properly captured
- Incomplete exception handling

## How to Fix

Use proper try-catch structure:

```erlang
try risky_operation() of
    Result -> {ok, Result}
catch
    error:Reason -> {error, {error, Reason}};
    throw:Value -> {error, {throw, Value}};
    exit:Reason -> {error, {exit, Reason}}
after
    cleanup_resources()
end.
```

Capture stack traces:

```erlang
try process_data(Data)
catch
    error:Reason:Stacktrace ->
        io:format("Error: ~p~nStack: ~p~n", [Reason, Stacktrace]),
        {error, Reason}
end.
```

Handle all exception classes:

```erlang
safe_call(M, F, A) ->
    try apply(M, F, A) of
        Result -> {ok, Result}
    catch
        error:undef -> {error, {undef, {M, F, A}}};
        error:badarg -> {error, {badarg, {M, F, A}}};
        _:Reason -> {error, Reason}
    end.
```

## Examples

```erlang
try 1 / 0 of
    Result -> Result
catch
    error:badarith -> "division by zero"
end.
```

## Related Errors

- [badarg]({{< relref "/languages/erlang/badarg" >}})
- [function_clause]({{< relref "/languages/erlang/function-clause2" >}})
