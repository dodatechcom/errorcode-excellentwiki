---
title: "error: bad arithmetic"
description: "A badarith error occurs when performing arithmetic operations on non-numeric values."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["arithmetic", "badarith", "math", "type-error"]
weight: 5
---

## What This Error Means

A `badarith` error is raised when you attempt to perform arithmetic operations (addition, subtraction, multiplication, division) on values that are not numbers. Erlang is strict about types in arithmetic operations.

## Common Causes

- Adding, subtracting, or multiplying atoms with numbers
- Dividing non-numeric values
- Using arithmetic operators on lists or tuples
- Passing strings where numbers are expected

## How to Fix

```erlang
%% WRONG: Arithmetic on atom
Result = hello + 1.  %% error: bad arithmetic in '+' operator

%% CORRECT: Ensure numeric values
Result = 1 + 2.     %% 3
```

```erlang
%% WRONG: Arithmetic on list
Result = [1] + [2].  %% error: bad arithmetic

%% CORRECT: Use list operations
Result = [1] ++ [2]. %% [1, 2]
```

## Examples

```erlang
%% Example 1: Atom with number
X = hello + 1.
%% error: bad arithmetic in '+' operator

%% Example 2: List with number
Y = [1, 2] * 3.
%% error: bad arithmetic in '*' operator

%% Example 3: String with number
Z = "hello" - 1.
%% error: bad arithmetic in '-' operator
```

## Related Errors

- [badarg: error: bad argument in call to X](/languages/erlang/badarg)
- [badmatch: no match of right hand side value](/languages/erlang/badmatch)
