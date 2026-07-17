---
title: "case_clause Error in Erlang"
description: "Erlang raises case_clause when no clause in a case expression matches the given value"
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `case_clause` error occurs when none of the clauses in a `case` expression match the input value. This is similar to `FunctionClauseError` but specifically for case expressions.

## Common Causes

- Missing catch-all clause
- Not all possible values covered
- Guard clauses rejecting all values
- Incorrect pattern matching

## How to Fix

Always include a catch-all clause:

```erlang
case Status of
    ok -> "Success";
    error -> "Error";
    _ -> "Unknown"
end.
```

Cover all possible values:

```erlang
case Type of
    admin -> "Administrator";
    user -> "Regular user";
    guest -> "Guest";
    Other -> "Unknown: " ++ atom_to_list(Other)
end.
```

Use guards for complex conditions:

```erlang
case Value of
    X when X > 0 -> positive;
    X when X < 0 -> negative;
    0 -> zero
end.
```

## Examples

```erlang
case unknown of
    ok -> success;
    error -> failure
end.
%% ** error: no case clause matching: unknown
```

## Related Errors

- [badmatch]({{< relref "/languages/erlang/badmatch" >}})
- [function_clause]({{< relref "/languages/erlang/function-clause2" >}})
