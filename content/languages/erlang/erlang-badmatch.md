---
title: "badmatch Error in Erlang"
description: "Erlang raises badmatch when pattern matching fails on the right-hand side of = operator"
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `badmatch` error occurs when pattern matching fails on the right-hand side of the `=` operator. This happens when the value does not match the expected pattern.

## Common Causes

- Value does not match expected pattern
- Variable already bound to different value
- Incorrect pattern structure
- Pin operator mismatch

## How to Fix

Use case expressions for multiple patterns:

```erlang
Value = {ok, Result},
case Value of
    {ok, Data} -> process(Data);
    {error, Reason} -> handle_error(Reason)
end.
```

Ensure variables are unbound before matching:

```erlang
%% WRONG: X already bound
X = 1,
X = 2.  %% badmatch

%% CORRECT: use new variable
Y = 2.
```

Use match with proper structure:

```erlang
{ok, User} = find_user(Id),
Name = element(2, User).
```

## Examples

```erlang
{ok, Value} = {error, not_found}.
%% ** badmatch error: {error,not_found}
```

## Related Errors

- [badarg]({{< relref "/languages/erlang/badarg" >}})
- [case_clause]({{< relref "/languages/erlang/case-clause" >}})
