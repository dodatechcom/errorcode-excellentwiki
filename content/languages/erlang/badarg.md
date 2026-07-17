---
title: "error: bad argument in call to X"
description: "A badarg error occurs when a function receives an argument of an unexpected or invalid type."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `badarg` error in Erlang is raised when a BIF (Built-In Function) or standard library function receives an argument that is not of the expected type or value. This is one of the most common runtime errors in Erlang and typically indicates a type mismatch.

## Common Causes

- Passing a non-numeric value to arithmetic operations
- Using a non-atom where an atom is expected
- Passing the wrong type to string or list operations
- Providing invalid arguments to built-in functions

## How to Fix

```erlang
%% WRONG: Adding a number to an atom
Result = 1 + atom.          %% error: bad argument in call to erlang:'+'/2

%% CORRECT: Ensure proper types
Result = 1 + 2.             %% 3
```

```erlang
%% WRONG: Using list_to_atom on invalid input
Atom = list_to_atom(123).   %% error: bad argument in call to list_to_atom/1

%% CORRECT: Validate input first
Input = "hello",
case is_list(Input) of
    true -> Atom = list_to_atom(Input);
    false -> {error, invalid_input}
end.
```

## Examples

```erlang
%% Example 1: Wrong type to math function
X = math:sqrt("hello").
%% error: bad argument in call to math:sqrt/1

%% Example 2: Invalid list operation
Y = lists:nth(0, [1, 2, 3]).
%% error: bad argument in call to lists:nth/2 (index must be >= 1)

%% Example 3: Wrong argument to iolist_to_binary
Z = iolist_to_binary(42).
%% error: bad argument in call to iolist_to_binary/1
```

## How to Debug

- Check the stack trace with `erlang:get_stacktrace()` in try/catch
- Use `io:format` to print argument types before the failing call
- Add type guards with `is_number/1`, `is_list/1`, etc.
- Use dialyzer for static type analysis

## Related Errors

- [badmatch: error: no match of right hand side value](/languages/erlang/badmatch)
