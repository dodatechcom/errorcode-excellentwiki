---
title: "error: no match of right hand side value"
description: "A badmatch error occurs when a pattern match fails because the value doesn't match the expected pattern."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `badmatch` error is raised when a pattern match operation fails. In Erlang, the `=` operator performs pattern matching, and if the right-hand side value doesn't match the left-hand side pattern, this error occurs.

## Common Causes

- Pattern doesn't match the actual data structure
- Using variable binding when you meant matching
- Incorrect tuple or list structure
- Wrong type in pattern

## How to Fix

```erlang
%% WRONG: Pattern doesn't match
{A, B} = [1, 2].    %% error: no match of right hand side value [1, 2]

%% CORRECT: Match with correct structure
{A, B} = {1, 2}.    %% A=1, B=2
```

```erlang
%% WRONG: Variable already bound
X = 1,
{X, Y} = {1, 2}.    %% works (X matches 1)
{X, Y} = {3, 4}.    %% error: no match, X already bound to 1

%% CORRECT: Use new variable names
X = 1,
{X, Y} = {1, 2},
{X2, Y2} = {3, 4}.  %% works
```

## Examples

```erlang
%% Example 1: Wrong tuple size
{A, B, C} = {1, 2}.
%% error: no match of right hand side value {1, 2}

%% Example 2: Wrong list pattern
[H | T] = [].
%% error: no match of right hand side value []

%% Example 3: Type mismatch
N = not_a_number,
N + 1.
%% error: bad argument (not a match error, but related)
```

## Related Errors

- [badarg: error: bad argument in call to X](/languages/erlang/badarg)
- [case_clause error](/languages/erlang/case-clause)
