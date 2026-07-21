---
title: "Erlang file read write error in io module"
description: "Fix Erlang file:read and file:write errors when performing I/O operations with incorrect modes or permissions."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

File I/O errors occur when the `file` module encounters problems opening, reading, or writing files. The error tuple `{error, Reason}` indicates the specific OS-level failure.

## Common Causes

- File does not exist when opening with `read` mode
- Insufficient file system permissions for write operations
- File is already open by another process with exclusive lock
- Disk is full during write operations
- Path contains invalid characters or exceeds OS limits

## How to Fix

```erlang
%% WRONG: Not checking file existence
{ok, Data} = file:read_file("missing.txt").
%% {error, enoent}

%% CORRECT: Check and handle errors
case file:read_file("data.txt") of
    {ok, Data} -> process(Data);
    {error, enoent} -> {error, file_not_found};
    {error, Reason} -> {error, Reason}
end.
```

```erlang
%% WRONG: Write mode on read-only file system
file:write_file("/proc/data", <<"test">>).
%% {error, eacces}

%% CORRECT: Use appropriate path
file:write_file("output.txt", <<"test">>).
```

## Examples

```erlang
%% Example 1: Read file line by line
{ok, Fd} = file:open("data.txt", [read]),
read_lines(Fd),
file:close(Fd).

read_lines(Fd) ->
    case file:read_line(Fd) of
        {ok, Line} -> io:format("~s", [Line]), read_lines(Fd);
        eof -> ok
    end.

%% Example 2: Write with append mode
file:write_file("log.txt", <<"new entry\n">>, [append]).

%% Example 3: Consult Erlang terms from file
{ok, Terms} = file:consult("config.config").
```

## Related Errors

- [IO error](erl-io-error) -- general I/O problems
- [Disk log error](erl-disk-log) -- disk log specific issues
