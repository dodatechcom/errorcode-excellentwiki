---
title: "[Solution] C++ Stack Unwinding Error — Fix"
description: "Fix stack unwinding failures by checking cleanup order, using smart pointers, and ensuring correct RAII patterns."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 923
---

# C++ Stack Unwinding Error — Fix

Stack unwinding is the process of destroying local objects in a function when an exception causes early exit. Errors occur when cleanup code itself throws, when objects are in inconsistent states during unwinding, or when manual resource management bypasses RAII.

## Common Causes

```cpp
// Cause 1: Raw pointer not cleaned up during unwinding
#include <stdexcept>

void dangerous() {
    int* data = new int[1000];
    throw std::runtime_error("error");  // data is leaked — no cleanup
    delete[] data;  // never reached
}
```

```cpp
// Cause 2: Exception during cleanup of another exception
struct ThrowOnDestroy {
    ~ThrowOnDestroy() noexcept(false) {
        throw std::runtime_error("double fault");
    }
};

void multi_exception() {
    ThrowOnDestroy obj1, obj2;
    throw std::runtime_error("first");
    // Unwinding destroys obj1 (throws) → std::terminate
}
```

```cpp
// Cause 3: File handle not RAII-wrapped
#include <cstdio>
#include <stdexcept>

void process_file() {
    FILE* f = fopen("data.txt", "r");
    if (!f) throw std::runtime_error("cannot open");
    // ... processing ...
    throw std::runtime_error("processing error");  // f is leaked
    fclose(f);  // never reached
}
```

```cpp
// Cause 4: Lock not released during exception
#include <mutex>

class BadDataManager {
    std::mutex mtx_;
    int data_ = 0;
public:
    void update(int val) {
        mtx_.lock();
        if (val < 0) throw std::runtime_error("invalid");  // mutex locked forever
        data_ = val;
        mtx_.unlock();
    }
};
```

```cpp
// Cause 5: Destructor order depends on construction order
class Database {
    std::string name_;
public:
    Database(std::string n) : name_(std::move(n)) {
        std::cout << "Open " << name_ << std::endl;
    }
    ~Database() {
        std::cout << "Close " << name_ << std::endl;
    }
};

void nested() {
    Database db1("primary");
    Database db2("secondary");
    throw std::runtime_error("error");
    // db2 destroyed first, then db1 — order matters
}
```

## How to Fix

### Fix 1: Use Smart Pointers Instead of Raw Pointers

```cpp
#include <memory>
#include <stdexcept>
#include <vector>

void safe_processing() {
    auto data = std::make_unique<int[]>(1000);
    throw std::runtime_error("error");  // data is automatically cleaned up
    // No leak — unique_ptr destructor runs during unwinding
}
```

### Fix 2: Use RAII for All Resources

```cpp
#include <fstream>
#include <stdexcept>
#include <string>

class FileGuard {
    std::ofstream file_;
    std::string name_;
public:
    FileGuard(const std::string& name) : file_(name), name_(name) {
        if (!file_.is_open()) throw std::runtime_error("Cannot open: " + name);
    }

    ~FileGuard() {
        if (file_.is_open()) file_.close();
    }

    std::ofstream& get() { return file_; }
};

void process_file() {
    FileGuard file("output.txt");  // RAII — guaranteed cleanup
    file.get() << "writing data" << std::endl;
    throw std::runtime_error("error");  // file closed automatically
}
```

### Fix 3: Use lock_guard for Mutex Management

```cpp
#include <mutex>
#include <stdexcept>

class DataManager {
    std::mutex mtx_;
    int data_ = 0;
public:
    void update(int val) {
        std::lock_guard<std::mutex> lock(mtx_);  // RAII lock
        if (val < 0) throw std::runtime_error("invalid");
        data_ = val;
        // mutex automatically unlocked, even during exception
    }
};
```

### Fix 4: Ensure Correct Destruction Order

```cpp
#include <string>
#include <iostream>

class Database {
    std::string name_;
public:
    Database(std::string n) : name_(std::move(n)) {
        std::cout << "Open " << name_ << std::endl;
    }
    ~Database() {
        std::cout << "Close " << name_ << std::endl;
    }
};

class ConnectionManager {
    Database secondary_;
    Database primary_;
public:
    // Member init order matches declaration order, not initializer list order
    // primary_ initialized first, secondary_ second
    // Destroyed in reverse: secondary_ first, then primary_
    ConnectionManager()
        : primary_("primary"), secondary_("secondary") {}
};

// Or use pointers for explicit control:
class SafeManager {
    std::unique_ptr<Database> primary_;
    std::unique_ptr<Database> secondary_;
public:
    SafeManager()
        : primary_(std::make_unique<Database>("primary"))
        , secondary_(std::make_unique<Database>("secondary")) {}
};
```

### Fix 5: Use noexcept Destructors Throughout

```cpp
#include <vector>
#include <iostream>

class SafeResource {
    int id_;
public:
    SafeResource(int id) : id_(id) {}
    ~SafeResource() noexcept {  // explicitly noexcept
        try {
            // cleanup that might fail
            std::cout << "Cleaned up resource " << id_ << std::endl;
        } catch (...) {
            // swallow — destructors must not throw
        }
    }
};
```

## Examples

```cpp
// Real-world: RAII database transaction with safe unwinding
#include <string>
#include <iostream>
#include <vector>

class Transaction {
    std::string db_name_;
    bool committed_ = false;
    std::vector<std::string> operations_;

public:
    explicit Transaction(std::string db) : db_name_(std::move(db)) {
        std::cout << "BEGIN transaction on " << db_name_ << std::endl;
    }

    ~Transaction() noexcept {
        if (!committed_) {
            try {
                std::cout << "ROLLBACK " << db_name_ << std::endl;
                // Perform actual rollback
            } catch (...) {
                std::cerr << "Failed to rollback " << db_name_ << std::endl;
            }
        }
    }

    void execute(const std::string& op) {
        if (committed_) throw std::runtime_error("already committed");
        operations_.push_back(op);
        std::cout << "  " << op << std::endl;
    }

    void commit() {
        std::cout << "COMMIT " << db_name_ << std::endl;
        committed_ = true;
    }
};
```

## Related Errors

- [noexcept violation]({{< relref "/languages/cpp/noexcept-violation" >}}) — exception from noexcept function.
- [Exception in destructor]({{< relref "/languages/cpp/exception-destructor" >}}) — exceptions during cleanup.
- [Exception safety guarantees]({{< relref "/languages/cpp/exception-safety-guarantees" >}}) — guarantee violations.
