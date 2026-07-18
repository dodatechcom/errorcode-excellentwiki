---
title: "[Solution] Erlang Try Catch Exception Error Handling"
description: "Fix Erlang try/catch exception errors. Learn proper exception handling with throw, error, and exit tuples."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An exception error in `try/catch` occurs when the catch block cannot handle the thrown or raised exception properly, or when the exception value does not match any catch pattern. Erlang has three exception classes: throw, error, and exit, and each must be handled appropriately.

## Why It Happens

- Catch clause does not match the exception class: You may be catching `error` when the exception is a `throw`.
- Exception raised inside try block with no matching handler: The exception type is not covered by any catch clause.
- Re-throwing exception without proper pattern: The re-thrown exception may not match the outer catch pattern.
- After clause raises its own exception: The cleanup code in the after block may fail, masking the original exception.
- Stacktrace not captured correctly: Using `erlang:get_stacktrace()` outside of a catch block returns undefined.

## How to Fix It

Handle all three exception classes explicitly to ensure comprehensive error handling:

```erlang
try dangerous_operation() of
    Result -> {ok, Result}
catch
    throw:Value -> {thrown, Value};
    error:Reason -> {error, Reason, erlang:get_stacktrace()};
    exit:Reason -> {exit, Reason}
end.
```

Use wildcard patterns to catch unexpected exceptions. This ensures your code handles even unforeseen error conditions:

```erlang
try process_request(Req) of
    Response -> send_response(Response)
catch
    throw:Data -> handle_throw(Data);
    error:_ -> handle_any_error();
    exit:Reason -> log_exit(Reason)
end.
```

Properly propagate exceptions when re-raising. Use `throw/1`, `error/1`, or `exit/1` to re-raise with the same exception class:

```erlang
try risky_call() of
    Value -> Value
catch
    error:badarith ->
        io:format("Arithmetic error caught~n"),
        exit({badarith, caught})
end.
```

Include the after block for cleanup operations. The after block always executes, whether the try block succeeds or fails:

```erlang
try acquire_lock(Resource) of
    ok -> do_work(Resource)
catch
    error:timeout -> {error, lock_timeout}
after
    release_lock(Resource)
end.
```

Use try-catch in function heads for cleaner error handling:

```erlang
process_data(Data) ->
    try validate(Data) of
        valid -> transform(Data)
    catch
        throw:invalid -> {error, validation_failed};
        error:badarg -> {error, invalid_argument}
    end.
```

## Common Mistakes

- Catching only one exception class and missing others. Always consider throw, error, and exit.
- Not capturing stacktrace with `erlang:get_stacktrace()`. The stacktrace is only available inside the catch block.
- Forgetting the after block for resource cleanup. Resources acquired in the try block should be released in after.
- Using catch in function head instead of try/catch expression. Function head catch only catches throws.
- Re-throwing exceptions with the wrong class. Ensure you maintain the original exception class when propagating.

## Related Pages

- [badmatch]({{< relref "/languages/erlang/erlang-badmatch" >}}) - pattern match failure
- [badarg]({{< relref "/languages/erlang/badarg" >}}) - bad argument error
- [process-crash]({{< relref "/languages/erlang/erlang-process-crash" >}}) - process crash
- [assertion-failed]({{< relref "/languages/erlang/erlang-assertion-failed" >}}) - gen_server assertion
