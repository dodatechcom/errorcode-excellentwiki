---
title: "Record syntax error in Erlang definition"
description: "Fix Erlang record syntax errors when defining or using records with incorrect field notation."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Record syntax errors appear when the Erlang compiler encounters malformed record definitions or record operations. Records in Erlang are syntactic sugar over tuples, and the compiler validates the syntax during preprocessing.

## Common Causes

- Using `#` without a record name in expressions
- Field names that conflict with Erlang reserved words
- Missing comma between field definitions in record declaration
- Using `:=` inside a record literal instead of `=>` or `=` for defaults
- Incorrect record update syntax with `#record_name{}`

## How to Fix

```erlang
%% WRONG: Record definition with reserved word
-record(user, {name, class, end}).
%% 'end' is a reserved word

%% CORRECT: Rename the field
-record(user, {name, class, status}).
```

```enrl
%% WRONG: Record literal missing field separator
#person{name = "Alice" age = 30}.
%% missing comma between fields

%% CORRECT
#person{name = "Alice", age = 30}.
```

## Examples

```erlang
%% Example 1: Creating a record
-record(point, {x = 0, y = 0}).
P = #point{x = 5, y = 10}.

%% Example 2: Pattern matching a record
case P of
    #point{x = X, y = Y} -> {X, Y};
    _ -> {0, 0}
end.

%% Example 3: Updating a record
P2 = P#point{x = 99}.
```

## Related Errors

- [Record include error](erl-record-include) -- missing header file for record
- [Record syntax error](erl-record-syntax) -- malformed record operations
