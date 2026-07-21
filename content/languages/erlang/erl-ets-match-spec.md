---
title: "ETS match spec syntax error in Erlang"
description: "Fix Erlang ETS match specification errors when constructing complex match_spec tuples for select operations."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Match specification syntax errors occur when the match spec used with `ets:select/2` or `ets:match_object/2` contains malformed tuples, invalid operators, or incorrectly bound variables.

## Common Causes

- Using string variables like `$1` outside of match spec context
- Missing the head-tail structure in match spec tuples
- Using unsupported guard expressions in the match spec
- Incorrect number of elements in match spec tuples
- Forgetting that match specs use their own expression language

## How to Fix

```erlang
%% WRONG: Using Erlang expressions in match spec
MatchSpec = [{{'_', X}, [], [{{element(1, '$1')}}]}].
%% 'X' is not a valid match spec variable

%% CORRECT: Use numbered variables
MatchSpec = [{{'_', '$1'}, [], [{{element(1, '$1')}}]}].
```

```erlang
%% WRONG: Missing head in match spec tuple
MatchSpec = [{'_', [], ['$1']}].
%% error: match spec tuple must have head pattern

%% CORRECT: Include proper head pattern
MatchSpec = [{{'_', '_', '$1'}, [], ['$1']}].
```

## Examples

```erlang
%% Example 1: Simple match spec
ets:select(Table, [{{'$1', '$2'}, [{'>', '$2', 10}], ['$1']}]).

%% Example 2: Match spec with guards
MS = [{{name, '$1', '$2'},
       [{'andalso', {is_atom, '$1'}, {'>', '$2', 0}}],
       ['$1']}],
Results = ets:select(Table, MS).

%% Example 3: Using ets.fun2ms for easier syntax
-include_lib("stdlib/include/ms_transform.hrl").
MS2 = ets:fun2ms(fun({Name, Age}) when Age > 25 -> Name end).
```

## Related Errors

- [ETS error](erl-ets-error) -- general ETS operation problems
- [ETS table error](erl-ets-table-error) -- table creation and access issues
