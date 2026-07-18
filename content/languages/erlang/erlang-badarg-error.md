---
title: "[Solution] Fix bad argument in function call Erlang error"
description: "Resolve badarg errors in Erlang by validating argument types with type guards, using try-catch for external input, and ensuring full type compatibility."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

The `badarg` error is raised when a BIF (Built-In Function) or standard library function receives an argument of an unexpected or invalid type. This is one of the most common runtime errors in Erlang.

The error appears as:

```erlang
** error: badarg
    in function  erlang:'+'/2
    called as 1 + atom
```

## Why It Happens

This error occurs due to type mismatches in function arguments:

- Passing a non-numeric value to arithmetic operations
- Using a non-atom where an atom is expected
- Passing wrong type to string or list operations
- Providing invalid arguments to built-in functions
- Attempting operations on the wrong data type

## How to Fix It

Validate argument types before calling BIFs:

```erlang
%% WRONG: Adding atom to number
Result = 1 + atom.

%% CORRECT: Validate type first
safe_add(A, B) when is_number(A), is_number(B) ->
    A + B;
safe_add(_, _) ->
    {error, not_a_number}.
```

Use type guards in function heads:

```erlang
%% Guard against bad types
safe_length(X) when is_list(X) -> length(X);
safe_length(X) when is_binary(X) -> byte_size(X);
safe_length(_) -> {error, not_a_list_or_binary}.
```

Check input before list operations:

```erlang
%% WRONG: Non-list to lists module
lists:nth(0, [1, 2, 3]).

%% CORRECT: Validate index
safe_nth(Index, List) when is_integer(Index), Index >= 1, is_list(List) ->
    lists:nth(Index, List);
safe_nth(_, _) ->
    {error, invalid_arguments}.
```

Use `try-catch` for external input handling:

```erlang
try
    list_to_integer("not_a_number")
catch
    error:badarg ->
        {error, invalid_integer_format}
end.
```

Convert types explicitly:

```erlang
%% WRONG: Direct type mismatch
atom_to_list(42).

%% CORRECT: Ensure correct input
case is_atom(Input) of
    true -> atom_to_list(Input);
    false -> {error, not_an_atom}
end.
```

## Common Mistakes

- Assuming Erlang will auto-convert between types
- Not using guards for type validation in function clauses
- Forgetting that `0` and `1.0` are different types
- Passing tuples or maps where lists or binaries are expected
- Not checking if a list contains integers before calling math functions on elements

## Related Pages

- [undef: function not defined](/languages/erlang/erlang-undef)
- [badmatch: no match of right hand side value](/languages/erlang/badmatch)
- [Function clause matching failed](/languages/erlang/erlang-functionclause)
