---
title: "Type spec error in Erlang -spec declaration"
description: "Fix Erlang type specification errors when -spec declarations use invalid types or incorrect syntax."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Type spec errors occur when the `-spec` declaration for a function uses invalid type syntax, references undefined types, or has argument/return type mismatches that the dialyzer or compiler can detect.

## Common Causes

- Using a type name that has not been defined or imported
- Mismatched number of arguments between spec and function clause
- Using `()` for void return when the function actually returns a value
- Incorrect union type syntax with missing pipes
- Referencing opaque types from other modules without proper import

## How to Fix

```erlang
%% WRONG: Undefined type
-spec process(input :: my_custom_type()) -> ok.
%% error: unknown type 'my_custom_type'

%% CORRECT: Use built-in or defined types
-spec process(input :: binary()) -> ok.
process(_Input) -> ok.
```

```erlang
%% WRONG: Argument count mismatch
-spec add(X :: integer(), Y :: integer()) -> integer().
add(X) -> X.  %% function takes 1 arg, spec says 2

%% CORRECT: Match spec to function
-spec add(X :: integer(), Y :: integer()) -> integer().
add(X, Y) -> X + Y.
```

## Examples

```erlang
%% Example 1: Correct union type spec
-spec status() -> ok | {error, term()}.
status() -> ok.

%% Example 2: Annotated return types
-spec fetch(Url :: string()) -> {ok, binary()} | {error, timeout}.
fetch(Url) ->
    case httpc:request(get, {Url, []}, [{timeout, 5000}], []) of
        {ok, {{_, 200, _}, _, Body}} -> {ok, list_to_binary(Body)};
        _ -> {error, timeout}
    end.

%% Example 3: Higher-order function spec
-spec apply_twice(F :: fun((A) -> B), Arg :: A) -> B.
apply_twice(F, Arg) -> F(F(Arg)).
```

## Related Errors

- [Type error](erl-type-error) -- runtime type mismatches
- [Dialyzer error](erl-dialyzer-error) -- static analysis findings
