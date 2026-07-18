---
title: "[Solution] Erlang Case Clause Error - No Matching Clause"
description: "Fix Erlang case clause error when no branch matches. Learn to add catch-all clauses and handle all patterns."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `case_clause` error occurs when a `case` expression receives a value that does not match any of the defined clauses. The Erlang runtime cannot find a suitable branch to execute, so it raises this error. The error message includes the exact value that failed to match, which is invaluable for debugging.

## Why It Happens

- Missing catch-all clause in case expression: If all clauses have specific patterns and none match the input value, the error is raised.
- New enum or tuple variant added without updating case branches: When the data model evolves, existing case expressions may not handle new variants.
- Unexpected nil or empty value reaching case expression: Functions that return `undefined` or empty values can trigger case clause errors.
- Data shape changed in upstream function: If a function that previously returned `{ok, Data}` now returns `{ok, Data, Timestamp}`, existing case patterns will not match.
- Guard clause too restrictive for valid input: Guard conditions may reject values that should be handled.

## How to Fix It

Always include a catch-all clause to handle unexpected values. The wildcard `_` pattern matches any value:

```erlang
case Status of
    active -> handle_active();
    inactive -> handle_inactive();
    _ -> handle_unknown(Status)
end.
```

Handle nil or empty values explicitly before the main case expression:

```erlang
case Input of
    undefined -> default_value();
    [] -> [];
    Value when is_list(Value) -> process_list(Value);
    _ -> {error, unexpected_input}
end.
```

Add logging before the case to debug unexpected values. This helps you understand what values are actually reaching the case expression:

```erlang
io:format("Received value: ~p~n", [Value]),
case Value of
    {ok, Data} -> Data;
    {error, Reason} -> throw(Reason)
end.
```

Use multiple clauses with complex patterns for message handling:

```erlang
case Message of
    {send, To, Body} -> do_send(To, Body);
    {receive_msg, Filter} -> do_receive(Filter);
    {timeout, Ms} -> schedule_timeout(Ms);
    _ -> {error, {unknown_message, Message}}
end.
```

Consider using function clauses instead of case when the logic is complex:

```erlang
handle_status(active) -> handle_active();
handle_status(inactive) -> handle_inactive();
handle_status(Other) -> handle_unknown(Other).
```

## Common Mistakes

- Forgetting the wildcard `_` clause for unexpected values. This is the most common cause of case_clause errors.
- Guard conditions that reject valid but uncommon inputs. Ensure your guards cover all valid input ranges.
- Not updating case clauses when the data model evolves. Maintain case expressions as part of your data model refactoring process.
- Assuming enum values are exhaustive without verification. Always include a catch-all clause even if you believe all cases are covered.
- Using complex nested case expressions when function clauses would be clearer and more maintainable.

## Related Pages

- [badmatch]({{< relref "/languages/erlang/erlang-badmatch" >}}) - pattern match failure
- [if-clause]({{< relref "/languages/erlang/erlang-ifclause" >}}) - no if clause matching
- [function-clause]({{< relref "/languages/erlang/erlang-functionclause" >}}) - no function clause
