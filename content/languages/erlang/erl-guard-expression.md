---
title: "Guard expression error in Erlang clause"
description: "Resolve Erlang guard expression errors caused by using non-guard-safe functions in clause guards."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Guard expression errors occur when you use a function or expression inside a guard clause that is not allowed. Erlang restricts guards to a specific set of expressions to ensure they cannot have side effects and always terminate.

## Common Causes

- Using `io:format` or any I/O function in a guard
- Calling user-defined functions inside a guard
- Using list comprehensions or case expressions in guards
- Attempting string operations that are not guard-safe
- Using operations that might throw exceptions inside guards

## How to Fix

```erlang
%% WRONG: Using io:format in a guard
handle(X) when io:format("~p~n", [X]) -> ok.
%% error: 'io' is not allowed in guard

%% CORRECT: Move the I/O outside the guard
handle(X) ->
    io:format("~p~n", [X]),
    ok.
```

```erlang
%% WRONG: Using a case expression in a guard
f(X) when case X of _ -> true end -> X.
%% error: 'case' is not allowed in guard

%% CORRECT: Use guard-safe comparisons
f(X) when is_atom(X) -> X;
f(X) when is_number(X) -> X.
```

## Examples

```erlang
%% Example 1: Guard-safe BIFs
%% Allowed: is_atom, is_binary, is_integer, length, element, etc.
member(X, [X | _]) -> true;
member(X, [_ | T]) -> member(X, T);
member(_, []) -> false.

%% Example 2: Using 'andalso' and 'orelse' in guards
safe_div(X, Y) when Y =/= 0 andalso is_number(X) -> X div Y.

%% Example 3: Building complex guards
classify(X) when is_integer(X), X > 0, X < 100 -> small;
classify(X) when is_integer(X), X >= 100 -> large.
```

## How to Debug

- Review the list of allowed expressions in the Erlang reference manual
- Replace non-guard-safe calls with equivalent guard-safe alternatives
- Use `if` expressions or `case` instead of complex guard bodies
- Check dialyzer output for guard-related warnings

## Related Errors

- [Guard limits error](erl-guard-limits) -- exceeding maximum guard complexity
- [Function clause error](erl-function-clause) -- no matching clause after guard fails
