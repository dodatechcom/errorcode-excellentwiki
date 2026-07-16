---
title: "[Solution] C++ std::future_error — Future Operation Failed Fix"
description: "Fix C++ std::future_error when promise/future operations fail. Handle broken promises, future already retrieved, and shared state errors."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["future-error", "std-future", "promise", "exception"]
weight: 50
---

# [Solution] C++ std::future_error — Future Operation Failed Fix

A `std::future_error` is thrown when an operation on `std::future` or `std::promise` fails due to an invalid state. This includes calling `get()` on a future with no shared state, retrieving a future twice, setting a value on a promise that already has one, or breaking a promise without setting a value.

## Common Causes

- Calling `get()` on a default-constructed `std::future`
- Calling `get()` on a future that has already been retrieved
- Setting a value on a promise that already has a value
- Destroying a promise without setting a value (broken promise)

## Example: Throwing std::future_error

```cpp
#include <future>
#include <iostream>

int main() {
    auto fut = std::async(std::launch::async, [] { return 42; });

    int a = fut.get();  // OK
    int b = fut.get();  // throws std::future_error
    return 0;
}
```

## How to Fix: Check Future State Before Getting

```cpp
#include <future>
#include <iostream>

int main() {
    auto fut = std::async(std::launch::async, [] { return 42; });

    if (fut.valid()) {
        int result = fut.get();
        std::cout << "Result: " << result << std::endl;
    } else {
        std::cerr << "Future is not valid" << std::endl;
    }

    return 0;
}
```

## Handling Broken Promises

```cpp
#include <future>
#include <iostream>
#include <thread>

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    prom.set_exception(std::make_exception_ptr(
        std::runtime_error("Producer failed")));

    try {
        int result = fut.get();
    } catch (const std::future_error& e) {
        std::cerr << "Future error: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.code().message() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    return 0;
}
```

## Safe Promise-Future Pattern

```cpp
#include <future>
#include <iostream>
#include <thread>

void producer(std::promise<int> prom) {
    try {
        int result = 42;
        prom.set_value(result);
    } catch (...) {
        prom.set_exception(std::current_exception());
    }
}

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    std::thread t(producer, std::move(prom));
    t.join();

    if (fut.valid()) {
        try {
            int result = fut.get();
            std::cout << "Result: " << result << std::endl;
        } catch (const std::future_error& e) {
            std::cerr << "Future error: " << e.what() << std::endl;
        }
    }
    return 0;
}
```

## Common Future Error Codes

| Error Code | Meaning |
|---|---|
| `future_errc::broken_promise` | Promise destroyed without setting value |
| `future_errc::future_already_retrieved` | `get()` called on already-retrieved future |
| `future_errc::promise_already_satisfied` | Value already set on promise |
| `future_errc::no_state` | Operation on future with no shared state |

## Summary

| Fix | When to Use |
|---|---|
| Check `valid()` before `get()` | Always when future lifecycle is uncertain |
| Use try-catch around `get()` | To handle broken promises and errors |
| Move promise to thread | When producer runs in a separate thread |
| Call `get()` only once | Store result after first retrieval |

## Related Errors

- [std::runtime_error]({{< relref "/languages/cpp/runtime-error-example" >}}) — general runtime failures.
- [std::system_error]({{< relref "/languages/cpp/system-error" >}}) — OS-level error codes.
- [std::bad_alloc]({{< relref "/languages/cpp/bad-allocation" >}}) — memory allocation failure.
