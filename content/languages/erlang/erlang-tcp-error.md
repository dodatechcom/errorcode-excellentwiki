---
title: "[Solution] Erlang TCP Connect Send Recv Error"
description: "Fix Erlang TCP errors including connect, send, and recv failures. Handle network timeouts and connection issues."
languages: ["erlang"]
error-types: ["network-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

TCP errors occur when operations on TCP sockets fail during connection, sending, or receiving data. These errors indicate network-level problems, socket configuration issues, or server unavailability.

## Why It Happens

- Target host is unreachable or DNS resolution fails: The hostname cannot be resolved to an IP address.
- Connection refused because no service listening on port: The server is not running on the specified port.
- Socket closed or not connected during send/recv: The connection was dropped before the operation.
- Network timeout exceeded during operation: The operation took longer than the configured timeout.
- Buffer overflow from sending data too fast: The kernel send buffer is full.

## How to Fix It

Handle connection errors with proper timeouts to avoid indefinite blocking:

```erlang
case gen_tcp:connect("localhost", 8080, [binary, {active, false}], 5000) of
    {ok, Socket} -> {ok, Socket};
    {error, timeout} -> {error, connection_timeout};
    {error, econnrefused} -> {error, server_not_running};
    {error, nxdomain} -> {error, dns_failure};
    {error, Reason} -> {error, {connect_failed, Reason}}
end.
```

Implement retry logic for transient failures. Network issues are often temporary:

```erlang
connect_retry(Host, Port, 0) -> {error, max_retries};
connect_retry(Host, Port, Retries) ->
    case gen_tcp:connect(Host, Port, [binary, {active, false}], 3000) of
        {ok, Socket} -> {ok, Socket};
        {error, Reason} ->
            timer:sleep(1000),
            connect_retry(Host, Port, Retries - 1)
    end.
```

Use passive sockets to avoid buffer issues and have explicit control over receiving data:

```erlang
{ok, Socket} = gen_tcp:connect(Host, Port, [binary, {active, false}]),
case gen_tcp:recv(Socket, 0, 5000) of
    {ok, Data} -> {ok, Data};
    {error, timeout} -> {error, receive_timeout};
    {error, closed} -> {error, connection_closed}
end.
```

Send data in manageable chunks to prevent buffer overflow:

```erlang
safe_send(Socket, Data) when byte_size(Data) > 65536 ->
    <<Chunk:65536/binary, Rest/binary>> = Data,
    case gen_tcp:send(Socket, Chunk) of
        ok -> safe_send(Socket, Rest);
        {error, _} = Error -> Error
    end;
safe_send(Socket, Data) ->
    gen_tcp:send(Socket, Data).
```

Handle partial sends properly:

```erlang
send_all(Socket, Data) ->
    case gen_tcp:send(Socket, Data) of
        ok -> ok;
        {ok, Remaining} -> send_all(Socket, Remaining);
        {error, Reason} -> {error, Reason}
    end.
```

## Common Mistakes

- Not setting connect timeout causing indefinite blocking on unreachable hosts.
- Using active mode sockets without proper message handling. Active mode sends messages to the process mailbox.
- Ignoring partial send results from gen_tcp:send. The return value indicates how much data was actually sent.
- Not closing sockets in error paths causing resource leaks. Always close sockets in cleanup code.
- Not handling the `{tcp_closed, Socket}` message in active mode.

## Related Pages

- [ssl-error]({{< relref "/languages/erlang/erlang-ssl-error" >}}) - SSL handshake failures
- [httpc-error]({{< relref "/languages/erlang/erlang-httpc-error" >}}) - HTTP client errors
- [nodedown]({{< relref "/languages/erlang/erlang-nodedown" >}}) - distributed node down
- [port-closed-error]({{< relref "/languages/erlang/erlang-port-closed-error" >}}) - port closed errors
