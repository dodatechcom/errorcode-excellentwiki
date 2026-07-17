---
title: "if_clause Error in Erlang"
description: "Erlang raises if_clause when no clause in an if expression matches"
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `if_clause` error occurs when none of the clauses in an `if` expression evaluate to `true`. In Erlang, `if` expressions require at least one clause to match.

## Common Causes

- All guard expressions evaluate to false
- Missing catch-all with `true` guard
- Guard expressions throw exceptions
- Boolean logic errors in conditions

## How to Fix

Always include a true clause:

```erlang
if
    X > 0 -> positive;
    X < 0 -> negative;
    true -> zero
end.
```

Check guard expressions:

```erlang
Value = 5,
Result = if
    is_integer(Value) andalso Value > 10 -> large;
    is_integer(Value) -> small;
    true -> not_an_integer
end.
```

Handle nil/undefined values:

```erlang
Config = #{debug => true},
DebugMode = if
    maps:get(debug, Config, false) -> true;
    true -> false
end.
```

## Examples

```erlang
if
    1 > 2 -> first;
    3 > 4 -> second
end.
%% ** error: no if clause matching
```

## Related Errors

- [case_clause]({{< relref "/languages/erlang/case-clause" >}})
- [badmatch]({{< relref "/languages/erlang/badmatch" >}})
