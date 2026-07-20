---
title: "[Solution] C++ Exception in Destructor — Fix"
description: "Fix exceptions thrown from destructors by using noexcept destructors, catching inside destructors, and logging errors safely."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 922
---

# C++ Exception in Destructor — Fix

An exception escaping a destructor is extremely dangerous. Since C++11, destructors are implicitly `noexcept`, so an uncaught exception in a destructor calls `std::terminate`. Even before C++11, exceptions during stack unwinding from another exception cause double-fault termination.

## Common Causes

```cpp
// Cause 1: File close operation that throws
#include <fstream>
#include <stdexcept>

class Logger {
    std::ofstream file_;
public:
    Logger(const std::string& path) : file_(path) {}
    ~Logger() {
        file_.close();  // may throw on some implementations
        if (file_.bad()) throw std::runtime_error("close failed");  // std::terminate
    }
};
```

```cpp
// Cause 2: Container destructor with throwing element destructors
#include <vector>

struct ThrowOnDestroy {
    ~ThrowOnDestroy() { throw std::runtime_error("destroy error"); }
};

int main() {
    std::vector<ThrowOnDestroy> v(3);
    v.clear();  // std::terminate — exception from element destructor
    return 0;
}
```

```cpp
// Cause 3: Smart pointer deleter that throws
#include <memory>
#include <stdexcept>

struct BadDeleter {
    void operator()(int* p) const {
        delete p;
        throw std::runtime_error("deleter error");  // std::terminate
    }
};

int main() {
    std::unique_ptr<int, BadDeleter> ptr(new int(42));
    return 0;  // std::terminate when ptr is destroyed
}
```

```cpp
// Cause 4: Lock guard with throwing unlock
#include <mutex>

class BadLock {
    std::mutex mtx_;
public:
    ~BadLock() {
        // If unlock throws (hypothetical), std::terminate
        mtx_.unlock();
    }
};
```

```cpp
// Cause 5: Exception during stack unwinding
#include <stdexcept>

struct ThrowInDestructor {
    ~ThrowInDestructor() noexcept(false) {
        throw std::runtime_error("second exception");
    }
};

void function_that_throws() {
    ThrowInDestructor obj;
    throw std::runtime_error("first exception");
    // Stack unwinding destroys obj → second exception → std::terminate
}
```

## How to Fix

### Fix 1: Catch All Exceptions Inside Destructors

```cpp
#include <fstream>
#include <iostream>

class Logger {
    std::ofstream file_;
public:
    Logger(const std::string& path) : file_(path) {}

    ~Logger() {
        try {
            file_.close();
        } catch (const std::exception& e) {
            std::cerr << "Error closing log: " << e.what() << std::endl;
        } catch (...) {
            std::cerr << "Unknown error closing log" << std::endl;
        }
    }
};
```

### Fix 2: Use noexcept Destructors Explicitly

```cpp
#include <cstdio>

class FileHandle {
    FILE* file_;
public:
    FileHandle(const char* name) : file_(fopen(name, "r")) {}

    // Explicitly noexcept — promise no exceptions
    ~FileHandle() noexcept {
        if (file_) fclose(file_);
    }

    // Move-only
    FileHandle(FileHandle&& other) noexcept : file_(other.file_) {
        other.file_ = nullptr;
    }
};
```

### Fix 3: Separate Cleanup from Destruction

```cpp
#include <fstream>
#include <iostream>
#include <stdexcept>

class DatabaseConnection {
    std::ofstream log_file_;
    bool connected_ = false;

public:
    DatabaseConnection(const std::string& log_path)
        : log_file_(log_path), connected_(true) {}

    // Explicit cleanup method — can throw
    void disconnect() {
        if (!connected_) return;
        log_file_.flush();
        if (log_file_.bad()) throw std::runtime_error("flush failed");
        connected_ = false;
    }

    // Destructor — must not throw
    ~DatabaseConnection() {
        try {
            disconnect();
        } catch (...) {
            // Log and swallow — can't throw from destructor
        }
    }
};
```

### Fix 4: Use ScopeGuard for Safe Cleanup

```cpp
#include <functional>
#include <iostream>

class ScopeGuard {
    std::function<void()> on_exit_;
public:
    explicit ScopeGuard(std::function<void()> f) : on_exit_(std::move(f)) {}
    ~ScopeGuard() noexcept {
        try {
            on_exit_();
        } catch (...) {
            // Swallow — destructor must not throw
        }
    }
    ScopeGuard(const ScopeGuard&) = delete;
    ScopeGuard& operator=(const ScopeGuard&) = delete;
};

void risky_operation() {
    int* resource = new int[100];
    ScopeGuard cleanup([&]() {
        delete[] resource;
        std::cout << "Cleaned up" << std::endl;
    });

    // Use resource...
    throw std::runtime_error("error");
    // cleanup runs safely during stack unwinding
}
```

### Fix 5: Log Errors Without Throwing

```cpp
#include <iostream>
#include <fstream>
#include <string>

class TracedObject {
    std::string name_;
    static std::ofstream log_;

public:
    TracedObject(std::string name) : name_(std::move(name)) {
        log() << "Created: " << name_ << std::endl;
    }

    ~TracedObject() noexcept {
        try {
            log() << "Destroyed: " << name_ << std::endl;
        } catch (...) {
            // Last resort: write to stderr
            std::cerr << "Failed to log destruction of " << name_ << std::endl;
        }
    }

    static std::ofstream& log() {
        if (!log_.is_open()) {
            log_.open("trace.log", std::ios::app);
        }
        return log_;
    }
};
```

## Examples

```cpp
// Real-world: RAII resource manager with safe destructor
#include <string>
#include <iostream>
#include <vector>
#include <memory>

class ConnectionPool {
    struct Connection {
        int id;
        bool in_use = false;
    };

    std::vector<Connection> connections_;
    std::string host_;

public:
    ConnectionPool(std::string host, size_t size)
        : host_(std::move(host)) {
        for (size_t i = 0; i < size; ++i) {
            connections_.push_back({static_cast<int>(i)});
        }
    }

    ~ConnectionPool() noexcept {
        // Close all connections safely
        for (auto& conn : connections_) {
            try {
                if (conn.in_use) {
                    std::cerr << "Warning: connection " << conn.id
                              << " still in use at shutdown" << std::endl;
                }
                // Simulate close
            } catch (...) {
                std::cerr << "Error closing connection " << conn.id << std::endl;
            }
        }
    }
};
```

## Related Errors

- [noexcept violation]({{< relref "/languages/cpp/noexcept-violation" >}}) — exception from noexcept function.
- [Stack unwinding error]({{< relref "/languages/cpp/stack-unwinding-error" >}}) — cleanup during propagation.
- [Exception safety guarantees]({{< relref "/languages/cpp/exception-safety-guarantees" >}}) — guarantee violations.
