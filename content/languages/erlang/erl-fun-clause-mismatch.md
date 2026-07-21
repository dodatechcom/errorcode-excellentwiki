---
title: "Fun clause mismatch error in Erlang"
description: "Fix Erlang fun clause mismatch when calling anonymous functions with arguments that do not match any clause."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A fun clause mismatch error occurs when you call a fun (anonymous function) with arguments that do not match any of its defined clauses. The error message shows the fun's expected patterns and the actual arguments provided.

## Common Causes

- Passing wrong number of arguments to a multi-clause fun
- Argument types do not match any clause pattern
- Calling a fun that has been partially applied with wrong arity
- Fun defined with guards that reject the input values
- Fun returned from a higher-order function has different expected arguments

## How to Fix

```erlang
%% WRONG: Calling fun with wrong arity
MyFun = fun(X, Y) -> X + Y end,
MyFun(1).  %% error: function_clause -- expects 2 args

%% CORRECT: Match the arity
MyFun(1, 2).
```

```erlang
%% WRONG: Argument type does not match clauses
MyFun = fun
    (X) when is_atom(X) -> atom_to_list(X);
    (X) when is_list(X) -> X
end,
MyFun(42).  %% error: no matching clause for integer

%% CORRECT: Add a clause for integers
MyFun2 = fun
    (X) when is_atom(X) -> atom_to_list(X);
    (X) when is_list(X) -> X;
    (X) when is_integer(X) -> integer_to_list(X)
end.
```

## Examples

```erlang
%% Example 1: Multi-clause fun
Format = fun
    ({ok, Val}) -> io:format("Value: ~p~n", [Val]);
    ({error, Msg}) -> io:format("Error: ~s~n", [Msg])
end,
Format({ok, 42}).

%% Example 2: Partially applied fun
Add = fun(X) -> fun(Y) -> X + Y end end,
Add5 = Add(5),
Add5(3).  %% 8

%% Example 3: Fun with complex patterns
Process = fun
    ({user, Name, Age}) when Age >= 18 -> {adult, Name};
    ({user, Name, _}) -> {minor, Name};
    (_) -> {error, invalid}
end.
```

## Related Errors

- [Function clause error](erl-function-clause) -- named function clause mismatch
- [Badfun error](badfun) -- argument is not a valid fun
