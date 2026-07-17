---
title: "no function clause matching in X"
description: "A function_clause error occurs when calling a function with arguments that don't match any of its defined clauses."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `function_clause` error is raised when a function is called with arguments that don't match any of its defined clauses. Each function clause uses pattern matching, and if no pattern matches, this error occurs.

## Common Causes

- Missing clause for specific argument types
- Arguments don't match any clause pattern
- Function clauses ordered incorrectly
- Not handling edge cases like empty lists or atoms

## How to Fix

```erlang
%% WRONG: Missing clause for empty list
head([H | _]) -> H.
head([]).  %% error: no function clause matching in head/1

%% CORRECT: Add clause for empty list
head([H | _]) -> H;
head([]) -> {error, empty_list}.
```

```erlang
%% WRONG: No clause for specific type
double(X) when is_number(X) -> X * 2.
double(hello).  %% error: no function clause matching

%% CORRECT: Add type guard or clause
double(X) when is_number(X) -> X * 2;
double(_) -> {error, not_a_number}.
```

## Examples

```erlang
%% Example 1: No clause for atom
len([]) -> 0;
len([_ | T]) -> 1 + len(T).
len(hello).
%% error: no function clause matching in len/1

%% Example 2: Wrong argument count
add(X, Y) -> X + Y.
add(1).
%% error: no function clause matching in add/1

%% Example 3: No clause for negative
factorial(0) -> 1;
factorial(N) -> N * factorial(N - 1).
factorial(-1).
%% error: no function clause matching in factorial/1
```

## Related Errors

- [case_clause error](/languages/erlang/case-clause)
- [badmatch: no match of right hand side value](/languages/erlang/badmatch)
