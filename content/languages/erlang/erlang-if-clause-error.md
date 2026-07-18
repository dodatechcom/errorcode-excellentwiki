---
title: "[Solution] Erlang If Clause Error - No Matching Guard"
description: "Fix Erlang if clause error when no guard expression matches. Add else branches and validate guard conditions."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `if_clause` error is raised when an `if` expression has no clause whose guard evaluates to `true`. Unlike `case` expressions which match on patterns, `if` clauses rely entirely on guard conditions to determine which branch to execute.

## Why It Happens

- All guard conditions evaluate to false for the given value: The input does not satisfy any of the boolean expressions in the guard clauses.
- Guard syntax error prevents proper evaluation: Incorrectly formed guard expressions may silently fail to match.
- Comparing against wrong types in guards: Guard conditions may expect a number but receive an atom, causing the guard to fail.
- Missing catch-all clause for else-like behavior: Without a `true` clause, the if expression has no fallback.
- Variable scope issues in guard expressions: Variables used in guards must be bound in the scope where the if expression appears.

## How to Fix It

Always include a catch-all clause that evaluates to `true`. This acts as the else branch:

```erlang
if
    Value > 100 -> large(Value);
    Value > 10 -> medium(Value);
    true -> small(Value)
end.
```

Verify guard conditions handle all possible inputs, including edge cases like zero, negative numbers, and empty lists:

```erlang
if
    is_atom(Status) -> handle_atom(Status);
    is_list(Status) -> handle_list(Status);
    is_tuple(Status) -> handle_tuple(Status);
    true -> {error, {unexpected_type, Status}}
end.
```

Use simpler logic with case expressions when guards become complex. Case expressions are often more readable:

```erlang
case Value of
    V when V > 100 -> large(V);
    V when V > 0 -> small(V);
    _ -> invalid(V)
end.
```

Debug by checking guard evaluation. Print the value and test each guard condition:

```erlang
io:format("Value: ~p, IsPositive: ~p~n", [Value, Value > 0]),
if
    Value > 0 -> positive;
    true -> non_positive
end.
```

Remember that guards have strict limitations on what operations are allowed. Only a small set of BIFs can be used in guards:

```erlang
%% ALLOWED in guards:
%% is_atom, is_binary, is_boolean, is_float, is_integer, is_list, is_number, is_pid, is_port, is_reference, is_tuple
%% element, hd, tl, length, map_size, node, round, self, trunc
%% +, -, *, div, rem, band, bor, bnot, bxor, bsl, bsr
%% ==, /=, =<, <, >=, >, =:=, =/=
```

## Common Mistakes

- Using floating point operations in guards which are not allowed. Use `round/1` or `trunc/1` first.
- Calling functions inside guard expressions. Only BIFs are permitted in guards.
- Forgetting that `true` acts as the else clause in if expressions.
- Using boolean operators incorrectly in complex guards. Remember that `not`, `and`, `or`, `andalso`, `orelse` have different precedence.
- Not understanding that if expressions are syntactic sugar for case expressions with boolean guards.

## Related Pages

- [case-clause]({{< relref "/languages/erlang/case-clause" >}}) - case clause error
- [badmatch]({{< relref "/languages/erlang/erlang-badmatch" >}}) - pattern match failure
- [function-clause]({{< relref "/languages/erlang/erlang-functionclause" >}}) - function clause error
