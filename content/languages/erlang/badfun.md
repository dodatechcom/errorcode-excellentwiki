---
title: "error: bad function"
description: "A badfun error occurs when attempting to call a value that is not a function."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `badfun` error is raised when you try to apply a value as a function using the `Fun(Arg)` syntax or `apply/3`, but the value is not a function (fun). This commonly happens when a variable that should hold a function holds something else instead.

## Common Causes

- Variable holding non-function value used in function call
- Module:Function syntax errors
- Incorrect function reference
- Function not properly returned from higher-order function

## How to Fix

```erlang
%% WRONG: Calling non-function value
F = not_a_function,
F(1).  %% error: bad function

%% CORRECT: Ensure value is a function
F = fun(X) -> X * 2 end,
F(1).  %% 2
```

```erlang
%% WRONG: Wrong function reference
F = lists:reverse,   %% works
F = lists:revers,    %% undefined
F([1, 2, 3]).        %% error: bad function

%% CORRECT: Verify function exists
F = fun lists:reverse/1,
F([1, 2, 3]).        %% [3, 2, 1]
```

## Examples

```erlang
%% Example 1: Atom used as function
Atom = hello,
Atom(world).
%% error: bad function

%% Example 2: Integer used as function
N = 42,
N(1).
%% error: bad function

%% Example 3: Wrong function reference
M = string,
M:to_upper("hello").
%% error: bad function (to_upper not in string module)
```

## Related Errors

- [badarg: error: bad argument in call to X](/languages/erlang/badarg)
- [function_clause error](/languages/erlang/function-clause2)
