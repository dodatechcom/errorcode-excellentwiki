---
title: "ETS table creation error in Erlang"
description: "Fix Erlang ETS table errors when creating or accessing ETS tables with invalid options or permissions."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

ETS table errors occur when you try to create a table with invalid options, access a table owned by another process without proper permissions, or perform operations incompatible with the table type.

## Common Causes

- Using a table type that does not support duplicate keys with `set` type
- Accessing an ETS table from a process that did not create it (for protected/private)
- Passing invalid keypos value that exceeds the tuple size
- Creating a named table when one with that name already exists
- Exceeding system memory limits for table storage

## How to Fix

```erlang
%% WRONG: Creating a named table that already exists
ets:new(my_table, [set, public, named_table]),
ets:new(my_table, [set, public, named_table]).
%% error: table already exists

%% CORRECT: Check if table exists first
case ets:info(my_table) of
    undefined -> ets:new(my_table, [set, public, named_table]);
    _ -> ok
end.
```

```enrl
%% WRONG: Accessing protected table from wrong process
%% Process A owns the table, Process B tries to insert
ets:insert(protected_table, {key, value}).
%% error from Process B: not owner

%% CORRECT: Use public tables or insert from owner
ets:new(my_table, [set, public, named_table]).
```

## Examples

```erlang
%% Example 1: Create different table types
Ordered = ets:new(ordered, [ordered_set, public]),
Hashed = ets:new(hashed, [bag, public]),
Duplicate = ets:new(dups, [duplicate_bag, public]).

%% Example 2: Insert and lookup
ets:insert(my_table, {user1, "Alice", 30}),
[{user1, Name, Age}] = ets:lookup(my_table, user1).

%% Example 3: Match spec for complex queries
MatchSpec = [{{'_', "$1", '$2'}, [{'>', '$2', 25}], [{{'$1', '$2'}}]}],
Results = ets:select(my_table, MatchSpec).
```

## Related Errors

- [ETS error](erl-ets-error) -- general ETS operation failures
- [ETS match error](erl-ets-match) -- match specification problems
