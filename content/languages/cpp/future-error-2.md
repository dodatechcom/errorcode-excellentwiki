---
title: "[Solution] C++ std::future_error — Promise/Future Error Fix"
description: "Fix C++ std::future_error when using promises, futures, and packaged tasks. Handle broken promises and already-satisfied states."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::future_error — Promise/Future Error Fix

A `std::future_error` is thrown when an operation on a `std::promise`, `std::future`, or `std::shared_future` fails. Common conditions include calling `set_value` on a promise that already has a value, calling `get()` on a future with no shared state, and breaking a promise (destroying it without setting a value).

## Why std::future_error Occurs

Common causes include calling `set_value()` twice on a `std::promise`, calling `get()` on a default-constructed future, destroying a promise without setting a value or exception, and calling `set_exception` after `set_value` has already been called.

## Wrong: Setting Value Twice on a Promise

```cpp
// WRONG — throws std::future_error
#include <future>
#include <iostream>

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    prom.set_value(42);
    prom.set_value(100);  // throws — already satisfied
    std::cout << fut.get() << std::endl;
    return 0;
}
```

## Correct: Set Value Only Once

```cpp
// CORRECT — set value exactly once
#include <future>
#include <iostream>

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    prom.set_value(42);
    std::cout << "Value: " << fut.get() << std::endl;
    return 0;
}
```

## Handle Broken Promise Exception

```cpp
// CORRECT — catch broken_promise when promise is destroyed
#include <future>
#include <iostream>
#include <thread>

void worker(std::promise<int> prom) {
    // Promise destroyed without setting a value
}

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    std::thread t(worker, std::move(prom));
    t.join();

    try {
        std::cout << fut.get() << std::endl;
    } catch (const std::future_error& e) {
        std::cerr << "Future error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use std::async to Avoid Promise/Future Errors

```cpp
// CORRECT — use std::async for simpler async patterns
#include <future>
#include <iostream>
#include <string>

std::string fetch_data(int id) {
    return "data_" + std::to_string(id);
}

int main() {
    auto fut = std::async(std::launch::async, fetch_data, 1);

    try {
        std::string result = fut.get();
        std::cout << "Result: " << result << std::endl;
    } catch (const std::future_error& e) {
        std::cerr << "Future error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Set value/exception exactly once per promise | Always with `std::promise` |
| Use `std::async` instead | When you want simplified async patterns |
| Catch `std::future_error` | When handling promise/future failures |
| Check `valid()` before calling `get()` | When future might not have a shared state |

## Related Errors

- [std::promise already satisfied]({{< relref "/languages/cpp/promise-already-satisfied" >}}) — setting value twice.
- [std::future already retrieved]({{< relref "/languages/cpp/future-already-retrieved" >}}) — calling get twice.
- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — OS-level error codes.
