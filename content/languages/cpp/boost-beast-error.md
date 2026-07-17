---
title: "[Solution] C++ Boost.Beast - HTTP error"
description: "Fix C++ Boost.Beast HTTP errors. Handle HTTP request and response failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Boost.Beast - HTTP error

Boost.Beast HTTP errors occur during HTTP request parsing, response handling, or connection management.

## Common Causes

```cpp
// Cause 1: Invalid HTTP response
http::response<http::string_body> res;
boost::beast::error_code ec;
http::read(stream, buffer, res, ec); // parse error

// Cause 2: Connection lost during request
http::request<http::string_body> req;
http::write(socket, req, ec); // connection error

// Cause 3: Timeout
socket.expires_after(std::chrono::seconds(30));
http::read(socket, buffer, res, ec); // timeout
```

## How to Fix

### Fix 1: Check error codes

```cpp
http::response<http::string_body> res;
boost::beast::error_code ec;
http::read(stream, buffer, res, ec);

if (ec == http::error::end_of_stream) {
    std::cerr << "Connection closed" << std::endl;
} else if (ec) {
    std::cerr << "Read error: " << ec.message() << std::endl;
}
```

### Fix 2: Validate HTTP status

```cpp
if (res.result() == http::status::ok) {
    // success
} else {
    std::cerr << "HTTP " << res.result() << std::endl;
}
```

### Fix 3: Set proper timeouts

```cpp
socket.expires_after(std::chrono::seconds(30));
```

## Related Errors

- [Boost.Asio - async error]({{< relref "/languages/cpp/boost-asio-error" >}}) — async errors.
- [std::system_error]({{< relref "/languages/cpp/system-error-generic" >}}) — system errors.
- [C: Connection timed out]({{< relref "/languages/c/operation-timed-out" >}}) — timeout.
