---
title: "[Solution] Erlang IO Format Bad Argument Error"
description: "Fix Erlang io:format bad argument error. Resolve format string mismatches and I/O device issues."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The io:format error occurs when the format string and argument list do not match during output operations. This includes bad argument errors from mismatched format specifiers, incorrect argument types, or invalid I/O devices.

## Why It Happens

- Format specifier count does not match argument count: The format string expects more or fewer arguments than provided.
- Wrong format specifier for argument type: Using ~s for an atom when ~p is needed.
- Writing to closed or invalid I/O device: The output device has been closed.
- Unicode characters in non-unicode format string: Special characters cause encoding issues.
- Attempting to format a pid or port incorrectly: Using wrong format specifier for special types.

## How to Fix It

Ensure format specifiers match arguments exactly. Count both specifiers and arguments:

```erlang
%% WRONG: Missing argument
io:format("Name: ~s, Age: ~p~n", [Name]).

%% CORRECT: All arguments provided
io:format("Name: ~s, Age: ~p~n", [Name, Age]).
```

Use correct format specifiers for data types:

```erlang
%% Integer formatting
io:format("Count: ~B (binary), ~#O (octal), ~#X (hex)~n", [255, 255, 255]).

%% Float formatting
io:format("Pi: ~.4f~n", [3.14159]).

%% List formatting
io:format("Items: ~p~n", [[a, b, c]]).

%% Tuple formatting
io:format("Tuple: ~p~n", [{key, value}]).
```

Write to specific devices safely with error handling:

```erlang
case file:open("output.log", [write]) of
    {ok, Device} ->
        io:format(Device, "Log entry: ~p~n", [Data]),
        file:close(Device);
    {error, Reason} ->
        io:format("Failed to open log: ~p~n", [Reason])
end.
```

Use the to_latin1 conversion for safe output of unicode data:

```erlang
SafeOutput = unicode:characters_to_list(Data, latin1),
io:format("~s~n", [SafeOutput]).
```

Use `io_lib:format/2` for safe formatting without output:

```erlang
case io_lib:format("Name: ~s, Age: ~p~n", [Name, Age]) of
    {ok, FormatString} -> io:format(FormatString);
    {error, Reason} -> io:format("Format error: ~p~n", [Reason])
end.
```

## Common Mistakes

- Using ~s for atoms when ~p is appropriate. ~s only works with strings and iolists.
- Forgetting newline at end of format string. Without ~n, output may be buffered.
- Not accounting for optional arguments with control sequences. Some specifiers take additional parameters.
- Mixing up ~p (pretty print) and ~w (write) specifiers. ~p adds indentation, ~w does not.
- Not handling the return value of io:format. It returns ok on success or {error, Reason} on failure.

## Related Pages

- [badarg]({{< relref "/languages/erlang/badarg" >}}) - bad argument error
- [logger-error]({{< relref "/languages/erlang/erlang-logger-error" >}}) - logger handler errors
- [io-error]({{< relref "/languages/erlang/erlang-io-error" >}}) - io operation errors
- [badmatch]({{< relref "/languages/erlang/erlang-badmatch" >}}) - pattern match failure
