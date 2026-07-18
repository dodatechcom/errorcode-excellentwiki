---
title: "[Solution] C++ Jthread Error — How to Fix"
description: "Fix C++ std::jthread errors including double join, stop token misuse, and destructor join exceptions in multithreaded code."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Jthread Error — How to Fix

C++20 `std::jthread` is a RAII thread that automatically joins on destruction. Double join attempts, stop token misuse, and destructor exceptions are common issues.

## Why It Happens

Jthread errors occur when explicitly calling `join()` or `join()` on a thread that was already joined by the destructor, when the thread function doesn't check the stop token, or when destruction occurs during exception unwinding causing nested `std::terminate` calls.

## Common Error Messages

1. `std::system_error: Resource temporarily unavailable`
2. `error: attempt to join a stopped jthread`
3. `std::terminate called — double join or join on detached thread`
4. `error: stop_token not used in jthread function`

## How to Fix It

### Fix 1: Don't Manually Join Before Destruction

```cpp
#include <thread>
#include <iostream>

// WRONG — destructor will try to join again
void bad_example() {
    std::jthread t([]{ std::cout << "Running\n"; });
    t.join();   // first join
    // destructor calls join() again — error!
}

// CORRECT — let destructor handle joining
void good_example() {
    std::jthread t([]{ std::cout << "Running\n"; });
    // destructor automatically joins
}
```

### Fix 2: Use Stop Token for Cooperative Cancellation

```cpp
#include <thread>
#include <iostream>
#include <chrono>

int main() {
    std::jthread worker([](std::stop_token stoken) {
        while (!stoken.stop_requested()) {
            std::cout << "Working...\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
        std::cout << "Stopped gracefully\n";
    });

    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    // destructor requests stop and joins
}
```

### Fix 3: Handle Thread Exceptions

```cpp
#include <thread>
#include <iostream>
#include <exception>

int main() {
    try {
        std::jthread t([]{
            throw std::runtime_error("thread error");
        });
        // destructor joins; exception propagates from join
    } catch (const std::exception& e) {
        std::cerr << "Caught: " << e.what() << "\n";
    }
}
```

## Common Scenarios

- **Nested jthreads**: A jthread creating another jthread in its destructor can deadlock.
- **Callback threads**: Libraries that start threads internally may not support jthread's join model.
- **Exception in thread**: Uncaught exceptions in a jthread's function cause `std::terminate`.

## Prevent It

1. Never call `join()` or `detach()` on a jthread — let the destructor handle it.
2. Always accept `std::stop_token` in worker functions for cooperative cancellation.
3. Catch exceptions inside thread functions rather than letting them propagate to `std::terminate`.

## Related Errors

- [Thread error]({{< relref "/languages/cpp/thread-error" >}}) — general threading issues.
- [Deadlock]({{< relref "/languages/cpp/deadlock" >}}) — join-related deadlocks.
- [Data race]({{< relref "/languages/cpp/data-race" >}}) — unsynchronized shared state.
