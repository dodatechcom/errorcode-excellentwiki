---
title: "no case clause matching X"
description: "A case_clause error occurs when no clause in a case expression matches the given value."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `case_clause` error is raised when none of the clauses in a `case` expression match the value being evaluated. The error message shows the value that couldn't be matched.

## Common Causes

- Missing catch-all clause (after)
- Value type doesn't match any clause pattern
- Missing clauses for edge cases
- Using case instead of if for simple conditions

## How to Fix

```erlang
%% WRONG: Missing clause for value
case 3 of
    1 -> one;
    2 -> two
end.
%% error: no case clause matching 3

%% CORRECT: Add catch-all clause
case 3 of
    1 -> one;
    2 -> two;
    _ -> other
end.
%% other
```

```erlang
%% WRONG: Missing nil/undefined handling
case get_value(Key) of
    {ok, Value} -> Value
end.
%% error if get_value returns error

%% CORRECT: Handle all possible outcomes
case get_value(Key) of
    {ok, Value} -> Value;
    error -> undefined
end.
```

## Examples

```erlang
%% Example 1: Integer without catch-all
case 5 of
    1 -> one;
    2 -> two
end.
%% error: no case clause matching 5

%% Example 2: Atom without catch-all
case hello of
    world -> "world"
end.
%% error: no case clause matching hello

%% Example 3: Complex pattern
case {ok, 42} of
    {error, Msg} -> Msg
end.
%% error: no case clause matching {ok, 42}
```

## Related Errors

- [function_clause error](/languages/erlang/function-clause2)
- [badmatch: no match of right hand side value](/languages/erlang/badmatch)
