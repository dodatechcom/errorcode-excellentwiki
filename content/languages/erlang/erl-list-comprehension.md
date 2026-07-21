---
title: "List comprehension error in Erlang generator"
description: "Fix Erlang list comprehension errors caused by invalid generators or filters in comprehension expressions."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

List comprehension errors occur when the syntax or semantics of an Erlang list comprehension are invalid. This includes problems with generator expressions, filter clauses, or the expression producing each element.

## Common Causes

- Using `=` instead of `<-` in generator expressions
- Placing a generator after a filter in the wrong order
- Using a non-boolean expression as a filter
- Incorrect use of multiple generators without proper nesting
- Missing the `||` separator between expression and generators

## How to Fix

```erlang
%% WRONG: Using = instead of <-
[X * 2 || X = [1,2,3]].
%% error: syntax error before '='

%% CORRECT: Use <- for generators
[X * 2 || X <- [1,2,3]].
```

```erlang
%% WRONG: Filter not evaluating to boolean
[X || X <- [1,2,3,4,5], X + 1].
%% error: guard expression not boolean

%% CORRECT: Use a boolean guard
[X || X <- [1,2,3,4,5], X rem 2 =:= 0].
```

## Examples

```erlang
%% Example 1: Basic comprehension with filter
Evens = [X || X <- lists:seq(1, 10), X rem 2 =:= 0].

%% Example 2: Multiple generators (nested)
Pairs = [{X, Y} || X <- [1,2,3], Y <- [a,b,c]].

%% Example 3: Comprehension with string processing
Words = ["hello", "world", "foo"],
Uppers = [string:to_upper(W) || W <- Words].
```

## Related Errors

- [List error](erl-list-error) -- general list operation failures
- [Pattern match error](erl-pattern-match) -- incorrect pattern in generator
