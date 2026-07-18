---
title: "[Solution] Erlang BadMatch Error in Pattern Matching"
description: "Fix Erlang badmatch error when pattern matching fails. Learn to handle variable binding and match operator issues."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `badmatch` error occurs when a pattern match fails on the right-hand side of the `=` operator in Erlang. Pattern matching is fundamental to Erlang programming, and this error indicates that the actual value received does not correspond to the expected pattern structure. The error message typically includes the value that failed to match, making it possible to diagnose the root cause.

## Why It Happens

There are several common reasons for encountering a `badmatch` error in your Erlang code. Understanding these causes will help you resolve the issue quickly and prevent it from recurring.

- Variable already bound to a different value: In Erlang, once a variable is bound, it cannot be rebound to a different value using the match operator. If you attempt `X = 1, X = 2`, the second match will fail because X is already bound to 1.
- Value structure does not match expected pattern: When you expect a tuple like `{ok, Data}` but receive `{error, Reason}`, the pattern match fails.
- Incorrect use of pin operator: The pin operator `^` is used to match against an already bound variable, but if the pinned value does not match, a badmatch error occurs.
- Attempting to match atomic values that differ: Matching `ok` against `error` or other mismatched atoms will always fail.
- Recursive function passes unexpected data shape: A function that processes recursive data structures may receive unexpected shapes from deeper recursion levels.

## How to Fix It

Use case expressions to handle multiple possible outcomes safely instead of relying on pattern matching with `=`:

```erlang
Result = fetch_data(Id),
case Result of
    {ok, Data} -> process(Data);
    {error, Reason} -> log_error(Reason)
end.
```

Ensure variables are unbound before pattern matching. If you need to reuse a variable, consider using a new variable name:

```erlang
%% WRONG: X is already bound
X = 1,
X = 2.  %% badmatch error

%% CORRECT: Use a new variable
Y = 2.
```

Use the match operator with proper structure, ensuring that the value on the right matches the expected pattern:

```erlang
{ok, UserProfile} = find_user(UserId),
Name = maps:get(name, UserProfile).
```

Debug by printing the actual value before attempting to match it. This helps you understand what the runtime is actually providing:

```erlang
Value = compute(),
io:format("Value is: ~p~n", [Value]),
{ok, Result} = Value.
```

When working with records, ensure the record structure is correct:

```erlang
-record(user, {name, age, email}),

process_user(#user{name = Name, age = Age}) ->
    io:format("User ~s is ~p years old~n", [Name, Age]).
```

## Common Mistakes

- Forgetting that `=` is a match operator, not an assignment operator. This is the most common source of confusion for developers coming from imperative languages.
- Reusing variable names across different match contexts without understanding that Erlang variables are single-assignment.
- Not handling error tuples returned by library functions, which often return `{ok, Value}` or `{error, Reason}` tuples.
- Assuming match will create a new binding instead of checking equality. Once a variable is bound, the match operator checks equality rather than creating a new binding.
- Not using the underscore `_` as a wildcard when you do not need to bind certain values in a pattern.

## Related Pages

- [case-clause]({{< relref "/languages/erlang/case-clause" >}}) - no case clause matching
- [function-clause]({{< relref "/languages/erlang/erlang-functionclause" >}}) - function clause error
- [badarg]({{< relref "/languages/erlang/badarg" >}}) - bad argument error
- [if-clause]({{< relref "/languages/erlang/erlang-ifclause" >}}) - no if clause matching
