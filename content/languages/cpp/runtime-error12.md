---
title: "[Solution] C++ std::runtime_error — Generic Runtime Exception Fix"
description: "Fix C++ std::runtime_error with specific message strings. Understand when runtime_error is thrown and how to handle it properly."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runtime-error", "runtime_error", "exception", "stdexcept", "what"]
weight: 5
---

# [Solution] C++ std::runtime_error — Generic Runtime Exception Fix

A `std::runtime_error` is the most commonly thrown standard C++ exception for conditions that cannot be predicted at compile time. It is defined in `<stdexcept>` and carries a descriptive message accessible via `.what()`. Any function can throw it, and it is frequently used as a base class for more specific exception types.

## Common Causes

- **File I/O failures** — opening, reading, or writing to a file that doesn't exist or is inaccessible
- **Network/OS errors** — system calls returning error codes that are wrapped in runtime_error
- **Invalid runtime state** — an operation attempted when the object is in an invalid state
- **Explicit throw by user code** — `throw std::runtime_error("...")` in application logic

## How to Fix

### Fix 1: Catch runtime_error and handle it

```cpp
#include <iostream>
#include <stdexcept>
#include <fstream>

int main() {
    try {
        std::ifstream file("config.txt");
        if (!file.is_open()) {
            throw std::runtime_error("Cannot open config.txt");
        }
        std::string line;
        std::getline(file, line);
        std::cout << line << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Runtime error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

### Fix 2: Create custom exception classes inheriting from runtime_error

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class DatabaseError : public std::runtime_error {
public:
    DatabaseError(const std::string& query, const std::string& detail)
        : std::runtime_error("DB error: " + detail + " (query: " + query + ")"),
          query_(query), detail_(detail) {}

    const std::string& query() const { return query_; }
    const std::string& detail() const { return detail_; }

private:
    std::string query_;
    std::string detail_;
};

void execute_query(const std::string& q) {
    throw DatabaseError(q, "connection refused");
}

int main() {
    try {
        execute_query("SELECT * FROM users");
    } catch (const DatabaseError& e) {
        std::cerr << e.what() << std::endl;
        std::cerr << "Query: " << e.query() << std::endl;
    }
    return 0;
}
```

### Fix 3: Wrap system errors in runtime_error

```cpp
#include <iostream>
#include <stdexcept>
#include <system_error>

void open_file(const char* path) {
    FILE* f = fopen(path, "r");
    if (!f) {
        throw std::runtime_error(
            std::string("Failed to open ") + path + ": " + strerror(errno)
        );
    }
    fclose(f);
}

int main() {
    try {
        open_file("/nonexistent/file.txt");
    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl;
    }
    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class Config {
public:
    Config(int port) {
        if (port < 1 || port > 65535) {
            throw std::runtime_error("Invalid port: " + std::to_string(port));
        }
        port_ = port;
    }
    int port() const { return port_; }
private:
    int port_;
};

int main() {
    try {
        Config c(0);  // throws std::runtime_error
    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl;  // "Invalid port: 0"
    }
    return 0;
}
```

## Related Errors

- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — errors detectable before runtime
- [std::system_error]({{< relref "/languages/cpp/system-error" >}}) — OS/system call errors with error codes
- [std::bad_alloc]({{< relref "/languages/cpp/bad-alloc-3" >}}) — memory allocation failure
