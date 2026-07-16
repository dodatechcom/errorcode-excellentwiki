---
title: "[Solution] C++ std::future_error — Future Operation Failed Fix"
description: "Fix C++ std::future_error when promise/future operations fail. Handle broken promises, future already retrieved, and shared state errors."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["future-error", "std-future", "promise", "exception"]
weight: 50
---

# [Solution] C++ std::future_error — Future Operation Failed Fix

A `std::future_error` is thrown when an operation on `std::future` or `std::promise` fails due to an invalid state. This includes calling `get()` on a future with no shared state, retrieving a future twice, setting a value on a promise that already has one, or breaking a promise without setting a value.

## Why std::future_error Occurs

Common causes include calling `get()` on a default-constructed `std::future`, calling `get()` on a future that has already been retrieved, setting a value on a promise that already has a value, destroying a promise without setting a value (broken promise), and calling `get()` on a future from `std::async` after it has already returned.

## Wrong: Retrieving a Future Twice

```cpp
// WRONG — throws std::future_error on second get()
#include <future>
#include <iostream>

int main() {
    auto fut = std::async(std::launch::async, [] { return 42; });

    int a = fut.get();  // OK — first get
    int b = fut.get();  // throws std::future_error (error_past)
    return 0;
}
```

## Correct: Check Future State Before Getting

```cpp
// CORRECT — check valid() and use once
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

    // fut is now invalid — do not call get() again
    return 0;
}
```

## Handling Broken Promises

```cpp
// CORRECT — catch broken_promise error
#include <future>
#include <iostream>
#include <thread>

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    // Simulate a broken promise (e.g., producer crashes)
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
// CORRECT — proper promise lifecycle management
#include <future>
#include <iostream>
#include <thread>

void producer(std::promise<int> prom) {
    try {
        // Do work...
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

- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — OS-level error codes.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.
