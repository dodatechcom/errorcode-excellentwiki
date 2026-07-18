---
title: "[Solution] Fix open_port failed and port creator process died in Erlang"
description: "Resolve Erlang port errors by validating port commands, linking ports to long-lived gen_server processes, and properly managing external process lifecycles."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 7
---

## What This Error Means

A port error occurs when Erlang fails to open a port to communicate with an external OS process, or when the port creator process dies while the port is still active. Ports provide a mechanism for Erlang to exchange data with external programs.

The error appears as:

```erlang
** error: badarg
    in function  open_port/2
    called as open_port({spawn, "my_program"}, [binary])
```

or:

```erlang
=ERROR REPORT==== 12-Jan-2025::14:30:22 ===
    Port creator process for port #Port<0.123> died
```

## Why It Happens

This error occurs due to port management issues:

- External program path is incorrect or program not found
- Port creator process terminates while port is still open
- Invalid port command or options
- Port driver not loaded in the VM
- OS process fails to start due to permissions or missing dependencies
- Too many open ports exceed system limits

## How to Fix It

Verify the external program exists and is executable:

```erlang
%% Check program path
case os:find_executable("my_program") of
    false ->
        {error, program_not_found};
    Path ->
        open_port({spawn, Path}, [binary, {line, 4096}])
end.
```

Handle port owner process lifecycle correctly:

```erlang
%% WRONG: Opening port in a short-lived process
start_port() ->
    Port = open_port({spawn, "ls"}, [binary]),
    %% Process exits immediately, port gets closed
    ok.

%% CORRECT: Keep port in a long-lived process
init(_) ->
    Port = open_port({spawn, "my_program"}, [binary]),
    {ok, #{port => Port}}.

handle_info({Port, {data, Data}}, #{port := Port} = State) ->
    process_data(Data),
    {noreply, State}.
```

Use try-catch for port opening:

```erlang
safe_open_port(Command) ->
    try
        open_port({spawn, Command}, [binary, eof])
    catch
        error:badarg ->
            {error, {port_open_failed, Command}};
        exit:Reason ->
            {error, {port_exit, Reason}}
    end.
```

Monitor port health:

```erlang
handle_info({'EXIT', Port, Reason}, #{port := Port} = State) ->
    io:format("Port exited: ~p~n", [Reason]),
    %% Restart or handle gracefully
    {stop, {port_died, Reason}, State}.
```

Use `os:cmd/1` for simple commands:

```erlang
%% For simple one-shot commands, use os:cmd
Result = os:cmd("ls -la"),
io:format("Output: ~s~n", [Result]).
```

Check system limits:

```bash
%% Check ulimit for open files/ports
ulimit -n

%% Increase if needed
ulimit -n 65536
```

Use `port_close/1` explicitly when done:

```erlang
%% Clean up port explicitly
port_close(Port),
%% Also unlink if needed
unlink(Port).
```

## Common Mistakes

- Not linking the port to the process that manages it
- Opening ports in supervised children that restart frequently
- Not handling `{'EXIT', Port, Reason}` messages for port lifecycle
- Using `open_port` for simple commands when `os:cmd` is sufficient
- Forgetting that port commands are executed by the shell and may need escaping
- Not accounting for port buffer overflow with high-volume data

## Related Pages

- [Process terminated with reason crash](/languages/erlang/erlang-process-crash)
- [Supervisor terminated children](/languages/erlang/erlang-supervisor-restart)
- [badarg: bad argument in function call](/languages/erlang/badarg)
