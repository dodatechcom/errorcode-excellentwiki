---
title: "[Solution] Fix no function clause matching in Erlang"
description: "Resolve function clause matching errors in Erlang by adding catch-all clauses, handling all input patterns with guards, and validating argument types."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A function clause matching error occurs when none of the defined clauses for a function match the given arguments. Erlang uses pattern matching in function heads, and this error indicates no clause can handle the input.

The error appears as:

```erlang
** error: no function clause matching in my_module:my_func/1
    in function  my_module:my_func/1
    called as my_module:my_func({error, bad})
```

## Why It Happens

This error occurs when function arguments do not match any defined clause:

- Pattern in function head is too specific for the given input
- Missing a catch-all clause for unexpected arguments
- Wrong number of arguments passed to the function
- Guard expressions exclude valid inputs
- Data structure mismatch (e.g., tuple vs list)

## How to Fix It

Add a catch-all clause as the last function definition:

```erlang
%% WRONG: Only handles atoms
handle(ok) -> success;
handle(error) -> failure.

handle({error, timeout}).  %% no clause matching

%% CORRECT: Add catch-all clause
handle(ok) -> success;
handle(error) -> failure;
handle(Other) -> {error, {unexpected, Other}}.
```

Handle all expected patterns explicitly:

```erlang
%% Handle nested patterns
process({ok, Data}) when is_list(Data) ->
    {ok, length(Data)};
process({ok, Data}) when is_binary(Data) ->
    {ok, byte_size(Data)};
process({error, Reason}) ->
    {error, Reason};
process(Other) ->
    {error, {unexpected_input, Other}}.
```

Use guard expressions for type checking:

```erlang
%% Add guards to distinguish similar structures
double(X) when is_integer(X) -> X * 2;
double(X) when is_float(X) -> X * 2.0;
double(_) -> {error, not_a_number}.
```

Verify argument count matches function definition:

```erlang
%% If function expects 2 args but you call with 3
my_func(A, B) -> A + B.
my_func(A, B, C).  %% Error - wrong arity

%% Fix: Define correct arity or update call
my_func(A, B, C) -> A + B + C.
```

Debug with `io:format`:

```erlang
handle(Input) ->
    io:format("Received: ~p~n", [Input]),
    process_input(Input).
```

## Common Mistakes

- Not including a catch-all clause `(_)` as the last function clause
- Placing catch-all clause before more specific ones (order matters)
- Forgetting that Erlang matches clauses in definition order
- Not using guards when patterns overlap in structure
- Assuming pattern matching will coerce types between clauses

## Related Pages

- [badarg: bad argument in function call](/languages/erlang/badarg)
- [undef: function not defined](/languages/erlang/erlang-undef)
- [badmatch: no match of right hand side value](/languages/erlang/badmatch)
