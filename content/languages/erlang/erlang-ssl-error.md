---
title: "[Solution] Erlang SSL Handshake Failed Error"
description: "Fix Erlang SSL handshake failed error. Resolve certificate, protocol version, and cipher suite configuration issues."
languages: ["erlang"]
error-types: ["network-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The SSL handshake failed error occurs when establishing a secure TLS/SSL connection and the handshake process cannot complete successfully. This prevents encrypted communication between client and server.

## Why It Happens

- Certificate verification fails due to invalid or expired cert: The server certificate is not trusted or has expired.
- Protocol version mismatch between client and server: The client and server do not support a common TLS version.
- Cipher suite not supported by either party: No mutually agreeable encryption algorithm can be found.
- CA certificate not in trusted certificate store: The certificate chain cannot be verified.
- Hostname verification mismatch with certificate CN/SAN: The hostname does not match the certificate.

## How to Fix It

Configure SSL options with proper certificate verification for production use:

```erlang
ssl:start(),
Options = [
    {certfile, "client.pem"},
    {keyfile, "client.key"},
    {cacerts, ["ca.pem"]},
    {verify, verify_peer},
    {server_name_indication, "example.com"}
],
case ssl:connect("example.com", 443, Options, 10000) of
    {ok, Socket} -> {ok, Socket};
    {error, {tls_alert, {handshake_failure, _}}} ->
        {error, certificate_validation_failed};
    {error, Reason} -> {error, Reason}
end.
```

Disable verification for development environments only. Never use this in production:

```erlang
%% WARNING: Only for development/testing
Options = [
    {verify, verify_none},
    {server_name_indication, disable}
].
```

Update SSL options for protocol compatibility to support multiple TLS versions:

```erlang
Options = [
    {versions, ['tlsv1.2', 'tlsv1.3']},
    {ciphers, ["ECDHE-RSA-AES256-GCM-SHA384"]},
    {certfile, "cert.pem"}
].
```

Debug SSL handshake with verbose logging:

```erlang
application:set_env(ssl, log_level, debug),
ssl:connect(Host, Port, Options, Timeout).
```

Handle certificate chain verification properly:

```erlang
Options = [
    {verify, verify_peer},
    {depth, 9},
    {cacerts, ["root-ca.pem", "intermediate-ca.pem"]}
].
```

## Common Mistakes

- Using verify_none in production environments. This disables certificate checking and is a security risk.
- Not updating CA certificates when they expire. Certificate rotation is essential for maintaining secure connections.
- Hardcoding cipher suites that server does not support. Check server documentation for supported ciphers.
- Forgetting to start the ssl application before use. Call `ssl:start()` or ensure it is in your application dependencies.
- Not handling hostname verification failures. Ensure the server_name_indication matches the certificate.

## Related Pages

- [tcp-error]({{< relref "/languages/erlang/erlang-tcp-error" >}}) - TCP connection errors
- [httpc-error]({{< relref "/languages/erlang/erlang-httpc-error" >}}) - HTTP client errors
- [nodedown]({{< relref "/languages/erlang/erlang-nodedown" >}}) - node down error
- [port-closed-error]({{< relref "/languages/erlang/erlang-port-closed-error" >}}) - port closed errors
