---
title: "[Solution] C++ std::runtime_error — Runtime Error Exception Example"
description: "Example of std::runtime_error in C++. Handle unexpected runtime conditions like file I/O failures and network errors."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runtime-error", "exception", "error-handling", "file-io"]
weight: 50
---

# [Solution] C++ std::runtime_error — Runtime Error Exception Example

A `std::runtime_error` represents errors caused by conditions external to the program — file I/O failures, network issues, resource exhaustion, or invalid runtime input. Unlike `std::logic_error` (bugs in code), `std::runtime_error` depends on runtime conditions that cannot be fully predicted at compile time.

## Common Causes

- File I/O failures (file not found, permission denied, disk full)
- Network connectivity issues and timeouts
- Invalid user input at runtime
- Resource exhaustion (memory, file handles, threads)

## Example: Throwing std::runtime_error

```cpp
#include <stdexcept>
#include <string>
#include <fstream>

std::string read_config(const std::string& path) {
    std::ifstream file(path);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open config file: " + path);
    }
    std::string content((std::istreambuf_iterator<char>(file)),
                         std::istreambuf_iterator<char>());
    return content;
}

int main() {
    try {
        std::string config = read_config("/etc/myapp.conf");
    } catch (const std::runtime_error& e) {
        std::cerr << "Runtime error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## How to Fix: Use Descriptive Error Messages

```cpp
#include <stdexcept>
#include <string>
#include <iostream>

void process(const std::string& data) {
    if (data.empty()) {
        throw std::runtime_error("process(): input data must not be empty");
    }
    if (data.size() > 1024) {
        throw std::runtime_error("process(): input data exceeds 1024 bytes (got " +
                                  std::to_string(data.size()) + ")");
    }
}

int main() {
    try {
        process("");
    } catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Custom Exception Hierarchy

```cpp
#include <stdexcept>
#include <string>
#include <iostream>

class DatabaseError : public std::runtime_error {
    std::string query_;
public:
    DatabaseError(const std::string& msg, const std::string& query)
        : std::runtime_error(msg), query_(query) {}

    const std::string& query() const { return query_; }
};

class ConnectionError : public DatabaseError {
public:
    ConnectionError(const std::string& host, int port)
        : DatabaseError("Failed to connect to " + host + ":" + std::to_string(port), "") {}
};

int main() {
    try {
        throw ConnectionError("localhost", 5432);
    } catch (const ConnectionError& e) {
        std::cerr << "Connection failed: " << e.what() << std::endl;
    } catch (const DatabaseError& e) {
        std::cerr << "Database error: " << e.what() << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Runtime error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Exception Hierarchy

| Exception | Meaning | Example |
|---|---|---|
| `std::runtime_error` | General runtime failure | File I/O error |
| `std::overflow_error` | Arithmetic overflow | Integer overflow |
| `std::underflow_error` | Arithmetic underflow | Floating-point underflow |
| `std::range_error` | Range error in computation | Result out of range |
| `std::filesystem::filesystem_error` | Filesystem operation failed | File not found |
| `std::system_error` | OS-level error | Permission denied |

## Summary

| Fix | When to Use |
|---|---|
| Use descriptive error messages | Always — include context about what failed |
| Create custom exception classes | When building domain-specific error handling |
| Catch by `const&` to avoid slicing | Always when catching exceptions |
| Use exception hierarchy | When multiple error types need different handling |

## Related Errors

- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — logical precondition violations (bugs).
- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — OS-level error codes.
- [std::filesystem::filesystem_error]({{< relref "/languages/cpp/filesystemerror" >}}) — filesystem-specific failures.
