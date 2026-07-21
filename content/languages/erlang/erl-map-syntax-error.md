---
title: "Map syntax error in Erlang expression"
description: "Fix Erlang map literal syntax errors when creating or pattern matching maps with incorrect notation."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Map syntax errors occur when you use incorrect notation for Erlang map literals or map patterns. Maps in Erlang use `#{}` for creation and `:=` or `=>` for pattern matching, and confusing these operators or misplacing keys causes compilation failures.

## Common Causes

- Using `=>` instead of `:=` when you need exact key match in patterns
- Placing a comma after the last element in a map literal
- Using atoms as keys without quoting when they contain special characters
- Mixing map update syntax `K => V` with `K := V` incorrectly
- Forgetting curly braces around key-value pairs in older Erlang syntax

## How to Fix

```erlang
%% WRONG: Comma after last element
Map = #{a => 1, b => 2,}.
%% error: syntax error before '}'

%% CORRECT: No trailing comma
Map = #{a => 1, b => 2}.
```

```erlang
%% WRONG: Using => in pattern match (adds new key)
case #{a => 1} of
    #{a => X, c => _} -> X.  %% error: c does not exist
    _ -> 0
end.

%% CORRECT: Use := for exact match
case #{a => 1} of
    #{a := X} -> X;
    _ -> 0
end.
```

## Examples

```erlang
%% Example 1: Map update syntax
M = #{x => 10},
M2 = M#{x := 20, y => 30}.  %% correct: update x, add y

%% Example 2: Nested map syntax
Nested = #{outer => #{inner => 42}}.
#{outer := #{inner := Val}} = Nested.  %% correct pattern

%% Example 3: Map with variable key
Key = name,
M = #{Key => "Alice"}.  %% correct: variable as key
```

## Related Errors

- [Map error](erl-map-error) -- runtime errors with map operations
- [Pattern match error](erl-pattern-match) -- general pattern matching failures
