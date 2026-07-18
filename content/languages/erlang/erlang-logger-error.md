---
title: "[Solution] Erlang Logger Handler Crashed Error"
description: "Fix Erlang logger handler crashed error. Resolve logging configuration, handler crashes, and log formatting issues."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The logger handler crashed error occurs when a configured logging handler fails during log message processing. This can cause log messages to be lost or the system to fall back to default behavior.

## Why It Happens

- Handler module has a bug in log/2 callback: The handler code crashes when processing a log event.
- Handler tries to write to unavailable file or socket: The output destination is not accessible.
- Log message exceeds handler buffer size: A very large message overflows the buffer.
- Handler crashes on specific log levels or metadata: Certain log events trigger unexpected behavior.
- Supervisor restarts handler during high log volume: The handler cannot keep up with the log rate.

## How to Fix It

Add error handling to custom logger handlers to prevent crashes:

```erlang
-module(my_logger_handler).
-export([log/2]).

log(LogEvent, Config) ->
    try format_and_write(LogEvent, Config)
    catch
        error:Reason ->
            io:format(standard_error, "Logger handler error: ~p~n", [Reason])
    end.
```

Configure handler with proper overflow strategy to handle high log volume:

```erlang
logger:add_handler(my_handler, my_logger_handler, #{
    level => info,
    buffer_size => 1000,
    overflow => drop
}).
```

Use the default handler as fallback to ensure logs are always captured:

```erlang
logger:add_handler(default, logger_std_h, #{
    level => info,
    formatter => {logger_formatter, #{
        template => [time, " ", level, " ", msg, "\n"]
    }}
}).
```

Monitor handler health to detect issues early:

```erlang
check_handler_health() ->
    Handlers = logger:get_handler_config(),
    lists:foreach(fun({Id, Config}) ->
        Level = maps:get(level, Config, info),
        io:format("Handler ~p: level ~p~n", [Id, Level])
    end, Handlers).
```

Set up log rotation to prevent disk exhaustion:

```erlog
logger:add_handler(file_handler, logger_disk_log_h, #{
    level => info,
    disk_log => #{
        name => my_log,
        file => "app.log",
        type => halt,
        max_no_bytes => 10485760,  %% 10MB
        max_no_files => 5
    }
}).
```

## Common Mistakes

- Not handling exceptions inside log handler callbacks. A crashing handler causes log loss.
- Using synchronous logging causing performance bottlenecks. Consider async handlers for high-throughput systems.
- Forgetting to set log level causing excessive output. Set appropriate levels for production.
- Not removing old handlers when adding new ones. Duplicate handlers cause duplicate log output.
- Not testing handler behavior under high load. Handlers may fail under stress.

## Related Pages

- [io-error]({{< relref "/languages/erlang/erlang-io-error" >}}) - io:format errors
- [process-crash]({{< relref "/languages/erlang/erlang-process-crash" >}}) - process crash
- [application-failed]({{< relref "/languages/erlang/erlang-application-failed" >}}) - application start failure
- [badarg]({{< relref "/languages/erlang/badarg" >}}) - bad argument error
