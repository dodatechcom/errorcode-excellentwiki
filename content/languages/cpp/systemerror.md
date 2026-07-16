---
title: "[Solution] C++ std::system_error — System Error Code Exception Fix"
description: "Fix C++ std::system_error when OS or library calls fail with error codes. Handle error_code exceptions and system-level failures."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["system-error", "error-code", "errno", "exception"]
weight: 50
---

# [Solution] C++ std::system_error — System Error Code Exception Fix

A `std::system_error` is thrown when a function that uses `std::error_code` encounters a failure. It wraps an error code with a human-readable message and category, making it the standard way to handle OS-level and library-level errors in C++. Many standard library functions (e.g., `std::thread` constructor, `std::mutex::lock`, filesystem operations) throw `std::system_error` on failure.

## Why std::system_error Occurs

Common causes include OS system call failures (file I/O, networking), thread creation failures (resource limits), mutex locking failures (deadlock detection), failed file operations (permission denied, file not found), and network socket errors.

## Wrong: Not Handling Thread Creation Errors

```cpp
// WRONG — program crashes if thread creation fails
#include <thread>
#include <iostream>

void worker() {}

int main() {
    // May throw system_error if thread resources exhausted
    std::thread t(worker);
    t.join();
    return 0;
}
```

## Correct: Catch std::system_error and Inspect Error Code

```cpp
// CORRECT — catch and inspect the error code
#include <thread>
#include <iostream>
#include <system_error>

void worker() {}

int main() {
    try {
        std::thread t(worker);
        t.join();
    } catch (const std::system_error& e) {
        std::cerr << "System error: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.code() << " (" << e.code().message() << ")" << std::endl;
        std::cerr << "Category: " << e.code().category().name() << std::endl;
        return 1;
    }
    return 0;
}
```

## Using error_code Overload to Avoid Exceptions

```cpp
// CORRECT — use error_code overload
#include <thread>
#include <iostream>
#include <system_error>

void worker() {}

int main() {
    std::error_code ec;
    std::thread t(worker, ec);

    if (ec) {
        std::cerr << "Failed to create thread: " << ec.message() << std::endl;
        return 1;
    }

    t.join();
    return 0;
}
```

## Handling Mutex Errors

```cpp
// CORRECT — handle mutex and lock errors
#include <mutex>
#include <iostream>
#include <system_error>

std::mutex mtx;

void safe_lock() {
    try {
        std::lock_guard<std::mutex> lock(mtx);
        // Critical section
    } catch (const std::system_error& e) {
        std::cerr << "Mutex error: " << e.what() << std::endl;
        if (e.code() == std::errc::resource_deadlock_would_occur) {
            std::cerr << "Deadlock detected" << std::endl;
        }
    }
}

int main() {
    safe_lock();
    return 0;
}
```

## Custom Error Codes and Categories

```cpp
// CORRECT — define custom error codes with system_error
#include <system_error>
#include <iostream>

enum class app_errc {
    file_not_found = 1,
    invalid_config = 2,
    network_timeout = 3,
};

struct app_error_category : public std::error_category {
    const char* name() const noexcept override { return "app_error"; }

    std::string message(int ev) const override {
        switch (static_cast<app_errc>(ev)) {
            case app_errc::file_not_found: return "File not found";
            case app_errc::invalid_config: return "Invalid configuration";
            case app_errc::network_timeout: return "Network timeout";
            default: return "Unknown error";
        }
    }
};

const app_error_category& app_category() {
    static app_error_category cat;
    return cat;
}

std::error_code make_error_code(app_errc e) {
    return {static_cast<int>(e), app_category()};
}

int main() {
    try {
        throw std::system_error(make_error_code(app_errc::network_timeout));
    } catch (const std::system_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        std::cerr << "Code: " << e.code().message() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Catch `std::system_error` | When calling OS or library functions that may fail |
| Use `error_code` overload | When you want non-throwing error handling |
| Inspect `e.code().message()` | For human-readable error descriptions |
| Define custom error categories | When building domain-specific error handling |

## Related Errors

- [std::filesystem::filesystem_error]({{< relref "/languages/cpp/filesystemerror" >}}) — filesystem-specific system errors.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.
