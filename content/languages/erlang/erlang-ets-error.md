---
title: "[Solution] Fix ETS table already exists and undefined table in Erlang"
description: "Resolve ETS table errors in Erlang by checking table ownership with ets:whereis, using named tables safely, and managing tables with process lifecycle."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 7
---

## What This Error Means

An ETS (Erlang Term Storage) error occurs when operations on ETS tables fail due to ownership issues, missing tables, or conflicting table names. ETS tables are owned by the creating process and destroyed when that process exits.

The error appears as:

```erlang
** error: badarg
    in function  ets:new/2
    called as ets:new(my_table, [named_table, public])

{error, {already_started, my_table}}
```

or:

```erlang
** error: {badarg, {ets, lookup, [my_table, key]}}
```

## Why It Happens

This error occurs due to ETS table management issues:

- Table already exists with the same name (named_table)
- Table was created by a process that has since exited
- Accessing a table that has been deleted
- Using `named_table` option on multiple process starts
- Wrong access rights (private table from different process)
- Table creation fails because table limit is reached

## How to Fix It

Check if table exists before creating:

```erlang
create_table(Name) ->
    case ets:whereis(Name) of
        undefined ->
            ets:new(Name, [named_table, public, {read_concurrency, true}]);
        TableId ->
            TableId
    end.
```

Use `ets:info/1` to inspect table state:

```erlang
case ets:info(my_table) of
    undefined ->
        %% Table does not exist
        create_table();
    Info ->
        io:format("Table info: ~p~n", [Info])
end.
```

Handle table ownership properly:

```erlang
%% Create table in a long-lived process (e.g., gen_server init)
init(_) ->
    TabId = ets:new(my_table, [set, public, {read_concurrency, true}]),
    {ok, #{table => TabId}}.

%% Access from other processes
read_data(TableId, Key) ->
    case ets:lookup(TableId, Key) of
        [{Key, Value}] -> {ok, Value};
        [] -> {error, not_found}
    end.
```

Use `ets:delete/1` and recreate when needed:

```erlang
%% Clean up and recreate table
case ets:whereis(old_table) of
    undefined -> ok;
    _ -> ets:delete(old_table)
end,
ets:new(old_table, [named_table, public, set]).
```

Use `heir` option for table ownership transfer:

```erlang
%% Table survives process restart via heir process
ets:new(my_table, [
    named_table,
    public,
    {heir, HeirPid, HeirData}
]).
```

Monitor ETS memory usage:

```erlang
%% Check table memory consumption
Memory = ets:info(my_table, memory),
io:format("ETS memory: ~p words~n", [Memory]).
```

## Common Mistakes

- Not handling the case where the creating process crashes and table is destroyed
- Using `named_table` without checking if the name is already taken
- Creating ETS tables in supervised children with `temporary` restart type
- Not considering ETS memory overhead for large datasets
- Forgetting that `private` tables can only be accessed by the owning process
- Not cleaning up ETS tables in `terminate/2` callbacks

## Related Pages

- [gen_server call timed out](/languages/erlang/erlang-timeout-error)
- [Application start failed](/languages/erlang/erlang-application-failed)
- [badarg: bad argument in function call](/languages/erlang/badarg)
