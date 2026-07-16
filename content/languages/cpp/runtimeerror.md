---
title: "[Solution] C++ std::runtime_error — Runtime Error Exception Fix"
description: "Fix C++ std::runtime_error when runtime conditions prevent normal execution. Handle unexpected runtime failures and error conditions."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["runtime-error", "exception", "error-handling"]
weight: 50
---

# [Solution] C++ std::runtime_error — Runtime Error Exception Fix

A `std::runtime_error` is the base class for C++ standard library exceptions caused by conditions external to the program. Unlike `std::logic_error` (which indicates bugs in the code), `std::runtime_error` represents errors that depend on runtime conditions — such as network failures, file I/O errors, resource exhaustion, or invalid user input at runtime.

## Why std::runtime_error Occurs

Common causes include file I/O failures, network connectivity issues, invalid runtime input from users, resource exhaustion (memory, file handles), external service failures, and data parsing errors.

## Wrong: Throwing Without Useful Information

```cpp
// WRONG — unhelpful error message
#include <stdexcept>
#include <string>

void process(const std::string& data) {
    if (data.empty()) {
        throw std::runtime_error("error");  // What error? Why?
    }
}

int main() {
    try {
        process("");
    } catch (const std::runtime_error& e) {
        // e.what() just says "error"
    }
    return 0;
}
```

## Correct: Throw With Descriptive Messages

```cpp
// CORRECT — descriptive error messages
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

## Creating Custom Exception Hierarchy

```cpp
// CORRECT — derive from std::runtime_error for domain-specific errors
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

void connect_to_db(const std::string& host, int port) {
    // Simulated failure
    throw ConnectionError(host, port);
}

int main() {
    try {
        connect_to_db("localhost", 5432);
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

## File I/O Error Handling

```cpp
// CORRECT — handle file operations with runtime_error
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

std::string read_file(const std::string& path) {
    std::ifstream file(path);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file: " + path);
    }

    std::string content((std::istreambuf_iterator<char>(file)),
                         std::istreambuf_iterator<char>());

    if (file.bad()) {
        throw std::runtime_error("I/O error while reading file: " + path);
    }

    return content;
}

int main() {
    try {
        std::string data = read_file("/tmp/config.txt");
        std::cout << "File content: " << data << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
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
