---
title: "[Solution] Erlang Port Is Closed Error"
description: "Fix Erlang port is closed error when communicating with external ports. Handle port lifecycle and IO operations."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `port is closed` error occurs when attempting to send data to or receive data from a port that has already been closed. Ports in Erlang represent OS-level processes or file descriptors, and once closed, all operations on them will fail.

## Why It Happens

- Port process exited or crashed externally: The external program terminated unexpectedly.
- Port closed by timeout or explicit close command: The port was closed intentionally or by a timeout mechanism.
- Attempting to send after port shutdown: Code tries to use the port after it has been closed.
- Race condition between port exit and send operation: The port closes while a send operation is in progress.
- Port driver encountered fatal error: The underlying driver failed and closed the port.

## How to Fix It

Check port status before sending data. Use a try-catch to handle the badarg error that results from sending to a closed port:

```erlang
safe_send(Port, Data) ->
    try erlang:port_command(Port, Data) of
        ok -> {ok, sent}
    catch
        error:badarg -> {error, port_closed}
    end.
```

Monitor port and handle exit signals to detect when the port closes:

```erlang
{Port, MonRef} = erlang:spawn_monitor(fun() ->
    Port = open_port({spawn, Command}, [binary, stream]),
    port_loop(Port)
end),
receive
    {'DOWN', MonRef, process, Port, Reason} ->
        io:format("Port exited: ~p~n", [Reason])
end.
```

Use linked ports with proper error handling. Linking ensures you receive notification when the port exits:

```erlang
Port = open_port({spawn, "my_program"}, [{line, 200}, exit_status]),
link(Port),
receive
    {Port, {data, {eol, Data}}} -> handle_data(Data);
    {Port, {exit_status, Status}} -> handle_exit(Status);
    {'EXIT', Port, Reason} -> handle_port_exit(Reason)
end.
```

Implement reconnection logic for transient failures. This is essential for long-running applications that communicate with external services:

```erlang
send_with_retry(Port, Data, 0) -> {error, max_retries};
send_with_retry(Port, Data, Retries) ->
    case catch erlang:port_command(Port, Data) of
        ok -> ok;
        {'EXIT', _} ->
            timer:sleep(100),
            NewPort = reopen_port(),
            send_with_retry(NewPort, Data, Retries - 1)
    end.
```

Always close ports explicitly when done:

```erlang
port_close(Port),
%% Or use erlang:port_close(Port)
```

## Common Mistakes

- Not monitoring port process for unexpected exits. Without monitoring, you will not know when the port closes.
- Sending data to port without checking if it is still alive. Always verify port status first.
- Forgetting to handle port exit_status messages. These messages indicate how the port process terminated.
- Assuming port remains open across node restarts. Ports are tied to the process that opened them.
- Not closing ports in error paths causing resource leaks. Always close ports in cleanup code.

## Related Pages

- [tcp-error]({{< relref "/languages/erlang/erlang-tcp-error" >}}) - TCP connection errors
- [process-crash]({{< relref "/languages/erlang/erlang-process-crash" >}}) - process crash
- [nodedown]({{< relref "/languages/erlang/erlang-nodedown" >}}) - node down error
- [badarg]({{< relref "/languages/erlang/badarg" >}}) - bad argument error
