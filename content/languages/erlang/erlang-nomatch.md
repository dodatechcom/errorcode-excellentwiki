---
title: "nomatch Error in Erlang"
description: "Erlang raises nomatch when a pattern match assertion fails"
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `nomatch` error occurs when an assertion match (using `=`) fails at compile time or when the match operator encounters incompatible values. This is related to `badmatch` but occurs in different contexts.

## Common Causes

- Compile-time pattern match failure
- Record field mismatch
- Type assertion failure
- Incompatible types in match

## How to Fix

Ensure patterns are compatible:

```erlang
%% This would fail at compile time if types don't match
-record(user, {name :: string(), age :: integer()}).

%% Correct usage
User = #user{name = "Alice", age = 30},
#user{name = Name} = User.
```

Use runtime checks instead of compile-time assertions:

```erlang
%% Use case for runtime matching
case Value of
    {ok, Data} -> process(Data);
    _ -> error
end.
```

Verify record definitions:

```erlang
-record(point, {x, y}).

%% Ensure correct record creation
P = #point{x = 1, y = 2}.
```

## Examples

```erlang
{ok, X} = {error, no_value}.
%% ** badmatch error (nomatch in some contexts)
```

## Related Errors

- [badmatch]({{< relref "/languages/erlang/badmatch" >}})
- [case_clause]({{< relref "/languages/erlang/case-clause" >}})
