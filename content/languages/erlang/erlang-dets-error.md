---
title: "[Solution] Erlang DETS Table Corrupted or Full Error"
description: "Fix Erlang DETS table corrupted and table full errors. Repair damaged tables and manage storage limits."
languages: ["erlang"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

DETS errors occur when the disk-based ETS table becomes corrupted or reaches its maximum size limit. DETS stores data on disk but has fixed constraints: a maximum file size of 2GB and a maximum of 1M entries.

## Why It Happens

- Table file corrupted due to unclean shutdown: The process crashed while writing to the table.
- Table exceeds 2GB file size limit: The table has accumulated too much data.
- Too many unique objects exceed 1M entry limit: The table has too many distinct keys.
- File system permissions changed after table creation: The file system is now read-only.
- Table opened concurrently by different processes: DETS does not support concurrent access from multiple processes.

## How to Fix It

Open DETS tables with repair option to handle corruption:

```erlang
case dets:open_file(my_table, [{file, "my_table.dets"}, {type, set}]) of
    {ok, Ref} -> {ok, Ref};
    {error, {need_repair, Ref}} ->
        dets:repair_continuation(Ref, 
            dets:traverse(Ref, fun(X) -> {ok, X} end)),
        dets:open_file(my_table, [{file, "my_table.dets"}]);
    {error, Reason} -> {error, Reason}
end.
```

Monitor table size and clean up old entries to prevent reaching limits:

```erlang
check_table_size(Ref) ->
    {_, Size, _} = dets:info(Ref, size),
    case Size > 900000 of
        true -> cleanup_old_entries(Ref, 10000);
        false -> ok
    end.
```

Use safe write with error handling to catch full table conditions:

```erlang
safe_insert(Ref, Record) ->
    case dets:insert(Ref, Record) of
        ok -> ok;
        {error, table_is_full} ->
            cleanup_and_retry(Ref, Record);
        {error, Reason} -> {error, Reason}
    end.
```

Implement backup strategy before large operations. Always backup before bulk imports:

```erlang
backup_table(Ref) ->
    BackupFile = "backup_" ++ 
        integer_to_list(erlang:system_time(second)) ++ ".dets",
    {ok, BackupRef} = dets:open_file(backup, 
        [{file, BackupFile}, {type, set}]),
    dets:traverse(Ref, fun(Record) ->
        dets:insert(BackupRef, Record),
        continue
    end),
    dets:close(BackupRef).
```

Use delete_object for removing specific records:

```erlang
dets:delete_object(Ref, Record).
```

## Common Mistakes

- Not closing DETS tables properly causing corruption. Always close tables in a finally block or after operations complete.
- Storing large binary objects that waste disk space. Consider external storage for large blobs.
- Ignoring table full warnings until operations fail. Monitor table size proactively.
- Not planning for table size growth over time. Implement cleanup strategies for time-series data.
- Opening DETS from multiple processes simultaneously. DETS requires serialized access.

## Related Pages

- [ets-error]({{< relref "/languages/erlang/erlang-ets-error" >}}) - ETS in-memory table errors
- [mnesia-error]({{< relref "/languages/erlang/erlang-mnesia-error" >}}) - Mnesia database errors
- [badarg]({{< relref "/languages/erlang/badarg" >}}) - bad argument error
