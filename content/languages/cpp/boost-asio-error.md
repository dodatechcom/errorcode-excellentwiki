---
title: "[Solution] C++ Boost.Asio - async operation error"
description: "Fix C++ Boost.Asio async operation errors. Handle asynchronous I/O failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Boost.Asio - async operation error

Boost.Asio errors occur during asynchronous operations like socket connect, read, write, or timer operations.

## Common Causes

```cpp
// Cause 1: Connection refused
tcp::socket socket(io_context);
socket.async_connect(endpoint, [](const boost::system::error_code& ec) {
    if (ec) {
        // ECONNREFUSED
    }
});

// Cause 2: Operation cancelled
boost::asio::steady_timer timer(io_context);
timer.async_wait([](const boost::system::error_code& ec) {
    if (ec == boost::asio::error::operation_aborted) {
        // timer was cancelled
    }
});

// Cause 3: End of file
socket.async_read(buffer, [](const boost::system::error_code& ec, size_t n) {
    if (ec == boost::asio::error::eof) {
        // connection closed
    }
});
```

## How to Fix

### Fix 1: Check error code in handlers

```cpp
socket.async_connect(endpoint, [](const boost::system::error_code& ec) {
    if (ec) {
        std::cerr << "Connect failed: " << ec.message() << std::endl;
        return;
    }
    // success
});
```

### Fix 2: Use error_code overloads

```cpp
boost::system::error_code ec;
socket.connect(endpoint, ec);
if (ec) {
    std::cerr << ec.message() << std::endl;
}
```

### Fix 3: Handle specific errors

```cpp
if (ec == boost::asio::error::connection_refused) {
    // server not running
} else if (ec == boost::asio::error::eof) {
    // connection closed by peer
} else if (ec == boost::asio::error::timed_out) {
    // operation timed out
}
```

## Related Errors

- [Boost.Beast - HTTP error]({{< relref "/languages/cpp/boost-beast-error" >}}) — HTTP errors.
- [std::system_error]({{< relref "/languages/cpp/system-error-generic" >}}) — system errors.
- [C: Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
