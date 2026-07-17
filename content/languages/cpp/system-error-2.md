---
title: "[Solution] C++ std::system_error — System Error Code Handling Fix"
description: "Fix C++ std::system_error when OS or library functions fail. Handle error_code exceptions, thread errors, and mutex failures."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::system_error — System Error Code Handling Fix

A `std::system_error` is thrown when a function that uses `std::error_code` encounters a failure. It wraps an error code with a human-readable message and category. Many standard library functions — including `std::thread`, `std::mutex`, and filesystem operations — throw `std::system_error` on failure.

## Why std::system_error Occurs

Common causes include thread creation failures from resource limits, mutex locking failures from deadlock detection, file I/O errors like permission denied or file not found, network socket errors, and failed system calls.

## Wrong: Not Handling Thread or Mutex Errors

```cpp
// WRONG — crashes if thread resources exhausted
#include <thread>
#include <iostream>

void worker() {}

int main() {
    std::thread t(worker);  // may throw system_error
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

## Use error_code Overload to Avoid Exceptions

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

## Handle Mutex Deadlock Errors

```cpp
// CORRECT — handle mutex-specific errors
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
