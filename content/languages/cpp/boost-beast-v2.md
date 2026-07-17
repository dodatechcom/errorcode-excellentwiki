---
title: "[Solution] Boost.Beast WebSocket Handshake Error Fix"
description: "Fix Boost.Beast WebSocket handshake errors. Handle HTTP upgrade failures, protocol negotiation, and TLS issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Boost.Beast WebSocket Handshake Error

Fix Boost.Beast WebSocket handshake errors. Handle HTTP upgrade failures, protocol negotiation, and TLS issues.

## What This Error Means

WebSocket handshake errors in Boost.Beast occur when the HTTP upgrade fails:

```
boost::beast::error: HTTP 403 Forbidden
websocket: The WebSocket connection was not accepted
boost::beast::error: bad HTTP version
```

## Common Causes

```cpp
// Cause 1: Server rejects WebSocket upgrade
ws.async_handshake(host, "/", [](beast::error_code ec) {
    // ec == error::upgrade_required
});

// Cause 2: Wrong host header
// Cause 3: TLS version mismatch
// Cause 4: Missing required headers
// Cause 5: Path does not match server expectations
```

## How to Fix

### Fix 1: Set proper WebSocket headers

```cpp
#include <boost/beast/websocket.hpp>
#include <boost/beast/core.hpp>

namespace beast = boost::beast;
namespace websocket = beast::websocket;
namespace http = beast::http;

websocket::stream<beast::tcp_stream> ws(ioc);
beast::get_lowest_layer(ws).connect(results);

ws.set_option(websocket::stream_base::decorator(
    [](websocket::request_type& req) {
        req.set(http::field::user_agent, "MyApp/1.0");
        req.set(http::field::origin, "http://example.com");
    }));

ws.async_handshake(host, "/", [](beast::error_code ec) {
    if (ec) {
        std::cerr << "Handshake failed: " << ec.message() << std::endl;
    }
});
```

### Fix 2: Use correct HTTP version for upgrade

```cpp
ws.set_option(websocket::stream_base::decorator(
    [](websocket::request_type& req) {
        req.version(11); // HTTP/1.1 required for upgrade
    }));
```

### Fix 3: Add TLS configuration for WSS

```cpp
#include <boost/asio/ssl.hpp>

namespace ssl = boost::asio::ssl;
using tcp = boost::asio::ip::tcp;

ssl::context ssl_ctx(ssl::context::tlsv12_client);
ssl_ctx.set_verify_mode(ssl::verify_peer);

websocket::stream<beast::ssl_stream<beast::tcp_stream>> wss(ioc, ssl_ctx);
beast::get_lowest_layer(wss).connect(results);

wss.next_layer().handshake(ssl::stream_base::client);
wss.async_handshake(host, "/", handler);
```

## Examples

```cpp
#include <boost/beast.hpp>
#include <boost/asio.hpp>
#include <iostream>

namespace beast = boost::beast;
namespace websocket = beast::websocket;
namespace net = boost::asio;
using tcp = net::ip::tcp;

int main() {
    try {
        net::io_context ioc;
        tcp::resolver resolver(ioc);
        websocket::stream<beast::tcp_stream> ws(ioc);

        auto const results = resolver.resolve("echo.websocket.org", "80");
        beast::get_lowest_layer(ws).connect(results);

        ws.set_option(websocket::stream_base::decorator(
            [](websocket::request_type& req) {
                req.set(beast::http::field::user_agent, "WebSocket Client");
            }));

        ws.async_handshake("echo.websocket.org", "/",
            [](beast::error_code ec) {
                if (ec) {
                    std::cerr << "Handshake: " << ec.message() << std::endl;
                    return;
                }
                std::cout << "WebSocket connected!" << std::endl;
            });

        ioc.run();
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
    return 0;
}
```

## Related Errors

- [Boost Asio Error]({{< relref "/languages/cpp/boost-asio-v2" >}}) — Boost.Asio error
- [Boost JSON Error]({{< relref "/languages/cpp/boost-json-error" >}}) — Boost JSON error
- [System Error]({{< relref "/languages/cpp/system-error" >}}) — system error
