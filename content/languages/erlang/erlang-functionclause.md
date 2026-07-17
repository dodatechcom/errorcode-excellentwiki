---
title: "function_clause Error in Erlang"
description: "Erlang raises function_clause when no function clause matches the given arguments"
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `function_clause` error occurs when a function is called with arguments that don't match any of its defined clauses. This is one of the most common Erlang runtime errors.

## Common Causes

- Missing clause for specific argument type
- Function clauses ordered incorrectly
- Passing unexpected types or values
- Forgetting to handle edge cases

## How to Fix

Add clauses for edge cases:

```erlang
%% WRONG: no clause for empty list
head([H | _]) -> H.

%% CORRECT: handle all cases
head([H | _]) -> H;
head([]) -> {error, empty_list}.
```

Order clauses correctly:

```erlang
%% More specific clauses first
parse(Binary) when is_binary(Binary) -> {string, Binary};
parse(List) when is_list(List) -> {list, List};
parse(Other) -> {other, Other}.
```

Add guard clauses:

```erlang
divide(A, B) when B =/= 0 -> A / B;
divide(_, 0) -> {error, division_by_zero}.
```

## Examples

```erlang
head([]).
%% ** error: function_clause
%%     in function  head/1
```

## Related Errors

- [badarg]({{< relref "/languages/erlang/badarg" >}})
- [case_clause]({{< relref "/languages/erlang/case-clause" >}})
