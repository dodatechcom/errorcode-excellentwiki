---
title: "badarg Error in Erlang"
description: "Erlang raises badarg when a BIF receives an argument of unexpected type or value"
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["badarg", "argument", "type-error", "bif"]
weight: 5
---

## What This Error Means

The `badarg` error is raised when a BIF (Built-In Function) or standard library function receives an argument that is not of the expected type or value.

## Common Causes

- Passing non-numeric value to arithmetic operations
- Using non-atom where atom expected
- Wrong type to string or list operations
- Invalid arguments to built-in functions

## How to Fix

Ensure proper types:

```erlang
%% WRONG
Result = 1 + atom.

%% CORRECT
Result = 1 + 2.
```

Validate input first:

```erlang
Input = "hello",
case is_list(Input) of
    true -> Atom = list_to_atom(Input);
    false -> {error, invalid_input}
end.
```

Add type guards:

```erlang
safe_divide(A, B) when is_number(A), is_number(B), B =/= 0 ->
    A / B;
safe_divide(_, _) ->
    {error, invalid_arguments}.
```

## Examples

```erlang
X = math:sqrt("hello").
%% error: bad argument in call to math:sqrt/1

Y = lists:nth(0, [1, 2, 3]).
%% error: bad argument in call to lists:nth/2
```

## Related Errors

- [badmatch]({{< relref "/languages/erlang/badmatch" >}})
- [case_clause]({{< relref "/languages/erlang/case-clause" >}})
