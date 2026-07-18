---
title: "[Solution] Erlang HTTPC Request Failed Error"
description: "Fix Erlang httpc request failed error. Handle HTTP client timeouts, connection errors, and response parsing."
languages: ["erlang"]
error-types: ["network-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The httpc request failed error occurs when the built-in Erlang HTTP client cannot complete an HTTP request. This covers connection failures, timeouts, SSL errors, and malformed responses from the server.

## Why It Happens

- Target server is unreachable or DNS fails: The hostname cannot be resolved or the server is down.
- Connection timeout before request completes: The server takes too long to respond.
- SSL certificate validation failure on HTTPS: The server certificate is invalid or untrusted.
- Response body too large for memory: The server returns a very large response.
- Invalid URL format or missing required headers: The URL is malformed or headers are incorrect.

## How to Fix It

Start the httpc application and configure timeouts properly:

```erlang
inets:start(),
ssl:start(),
Options = [
    {timeout, 15000},
    {connect_timeout, 5000},
    {ssl, [{verify, verify_peer}]}
],
case httpc:request(get, {"https://api.example.com/data", []}, Options, []) of
    {ok, {{_, 200, _}, _Headers, Body}} -> {ok, Body};
    {ok, {{_, StatusCode, _}, _Headers, Body}} -> 
        {error, {http_error, StatusCode, Body}};
    {error, Reason} -> {error, Reason}
end.
```

Use streaming for large responses to avoid memory issues:

```erlang
Options = [
    {sync, false},
    {stream, {self, once}},
    {timeout, 30000}
],
{ok, RequestId} = httpc:request(get, {Url, Headers}, Options, []),
receive_response(RequestId).
```

Handle redirects manually since httpc does not follow them by default:

```erlang
follow_redirects(Url, Headers, 0) -> {error, too_many_redirects};
follow_redirects(Url, Headers, MaxRedirects) ->
    case httpc:request(get, {Url, Headers}, [{timeout, 10000}], []) of
        {ok, {{_, 301, _}, RespHeaders, _Body}} ->
            NewUrl = proplists:get_value("location", RespHeaders),
            follow_redirects(NewUrl, Headers, MaxRedirects - 1);
        {ok, Response} -> {ok, Response};
        {error, Reason} -> {error, Reason}
    end.
```

Set proper user agent and headers for the request:

```erlang
Headers = [
    {"User-Agent", "MyApp/1.0"},
    {"Accept", "application/json"}
],
httpc:request(get, {Url, Headers}, Options, []).
```

Handle HTTP status codes appropriately:

```erlang
handle_response({ok, {{_, 200, _}, _, Body}}) -> {ok, Body};
handle_response({ok, {{_, 404, _}, _, _}}) -> {error, not_found};
handle_response({ok, {{_, 500, _}, _, _}}) -> {error, server_error};
handle_response({ok, {{_, Code, _}, _, Body}}) -> {error, {http, Code, Body}};
handle_response({error, Reason}) -> {error, Reason}.
```

## Common Mistakes

- Forgetting to start inets and ssl applications. Without these, httpc will not work.
- Not setting connect_timeout causing indefinite hangs on unreachable hosts.
- Ignoring SSL certificate verification in production. Always use verify_peer.
- Not handling non-200 HTTP status codes. Check the status code before processing the body.
- Using httpc on the main process for synchronous requests. This blocks the process until the response arrives.

## Related Pages

- [tcp-error]({{< relref "/languages/erlang/erlang-tcp-error" >}}) - TCP connection errors
- [ssl-error]({{< relref "/languages/erlang/erlang-ssl-error" >}}) - SSL handshake failures
- [timeout-error]({{< relref "/languages/erlang/erlang-timeout-error" >}}) - timeout errors
- [nodedown]({{< relref "/languages/erlang/erlang-nodedown" >}}) - node down error
