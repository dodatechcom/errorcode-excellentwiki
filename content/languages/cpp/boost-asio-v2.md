---
title: "[Solution] Boost.Asio Async Connect Error Fix"
description: "Fix Boost.Asio async connect errors. Handle connection timeouts, resolver failures, and async operation errors."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Boost.Asio Async Connect Error Fix

Fix Boost.Asio async connect errors. Handle connection timeouts, resolver failures, and async operation errors.

## What This Error Means

Boost.Asio async connect errors occur during asynchronous connection establishment:

```
boost::system::system_error: Connection refused
asio.misc: End of file
asio.ssl: SSL
```

## Common Causes

```cpp
// Cause 1: Server not listening
tcp::resolver resolver(io_context);
auto results = resolver.resolve("localhost", "8080");
boost::asio::connect(socket, results); // Connection refused

// Cause 2: DNS resolution failure
// Cause 3: Operation cancelled before completion
// Cause 4: SSL handshake failure
// Cause 5: Timeout not set, connection hangs
```

## How to Fix

### Fix 1: Use async connect with timeout

```cpp
#include <boost/asio.hpp>
#include <iostream>

using boost::asio::ip::tcp;

void async_connect(tcp::socket& socket, tcp::resolver::results_type endpoints) {
    boost::asio::steady_timer timer(socket.get_executor());
    timer.expires_after(std::chrono::seconds(5));

    boost::asio::async_connect(socket, endpoints,
        [&socket](const boost::system::error_code& ec, const tcp::endpoint&) {
            if (!ec) {
                std::cout << "Connected!" << std::endl;
            } else {
                std::cerr << "Connect error: " << ec.message() << std::endl;
            }
        });

    timer.async_wait([&socket](const boost::system::error_code& ec) {
        if (!ec) {
            socket.close(); // Cancel connect
        }
    });
}
```

### Fix 2: Handle error codes in callbacks

```cpp
void handle_connect(const boost::system::error_code& ec, tcp::socket& socket) {
    if (ec == boost::asio::error::operation_aborted) {
        std::cerr << "Connect timed out" << std::endl;
    } else if (ec) {
        std::cerr << "Connect failed: " << ec.message() << std::endl;
    } else {
        std::cout << "Connected successfully" << std::endl;
    }
}
```

### Fix 3: Use coroutines (C++20)

```cpp
#include <boost/asio.hpp>
#include <iostream>

boost::asio::awaitable<void> connect_async() {
    auto executor = co_await boost::asio::this_coro::executor;
    boost::asio::ip::tcp::resolver resolver(executor);
    boost::asio::ip::tcp::socket socket(executor);

    auto results = co_await resolver.async_resolve("localhost", "8080",
        boost::asio::use_awaitable);

    co_await boost::asio::async_connect(socket, results,
        boost::asio::use_awaitable);

    std::cout << "Connected!" << std::endl;
}
```

## Examples

```cpp
#include <boost/asio.hpp>
#include <iostream>
#include <thread>

using boost::asio::ip::tcp;

class TcpClient {
    boost::asio::io_context& io_;
    tcp::socket socket_;
    tcp::resolver resolver_;

public:
    TcpClient(boost::asio::io_context& io)
        : io_(io), socket_(io), resolver_(io) {}

    void connect(const std::string& host, const std::string& port) {
        resolver_.async_resolve(host, port,
            [this](const boost::system::error_code& ec,
                   tcp::resolver::results_type results) {
                if (ec) {
                    std::cerr << "Resolve error: " << ec.message() << std::endl;
                    return;
                }
                boost::asio::async_connect(socket_, results,
                    [this](const boost::system::error_code& ec, const tcp::endpoint&) {
                        if (ec) {
                            std::cerr << "Connect error: " << ec.message() << std::endl;
                            return;
                        }
                        std::cout << "Connected!" << std::endl;
                    });
            });
    }
};

int main() {
    boost::asio::io_context io;
    TcpClient client(io);
    client.connect("127.0.0.1", "8080");
    io.run();
    return 0;
}
```

## Related Errors

- [Boost Beast Error]({{< relref "/languages/cpp/boost-beast-v2" >}}) — Beast WebSocket error
- [Boost JSON Error]({{< relref "/languages/cpp/boost-json-error" >}}) — Boost JSON error
- [System Error]({{< relref "/languages/cpp/system-error" >}}) — system error
