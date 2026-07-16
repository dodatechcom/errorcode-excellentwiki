---
title: "[Solution] C++ std::promise Already Satisfied — Double Set Fix"
description: "Fix C++ std::promise already satisfied error when calling set_value or set_exception twice. Learn proper promise lifecycle management."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["promise", "already-satisfied", "future", "concurrency"]
weight: 5
---

# [Solution] C++ std::promise Already Satisfied — Double Set Fix

A `std::future_error` with `std::errc::promise_already_satisfied` is thrown when you call `set_value()`, `set_exception()`, or `set_value_at_thread_exit()` on a `std::promise` that has already been satisfied. A promise can only be fulfilled once.

## Why Promise Already Satisfied Occurs

Common causes include calling `set_value()` twice on the same promise, calling `set_exception()` after `set_value()` has been called, and multiple code paths attempting to fulfill the same promise.

## Wrong: Setting Value Twice

```cpp
// WRONG — throws future_error: promise_already_satisfied
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

## Correct: Set Value Exactly Once

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

## Use a Flag to Prevent Double Satisfaction

```cpp
// CORRECT — guard against double satisfaction
#include <future>
#include <iostream>
#include <atomic>

class OncePromise {
    std::promise<int> prom_;
    std::atomic<bool> satisfied_{false};

public:
    std::future<int> get_future() { return prom_.get_future(); }

    bool try_set_value(int value) {
        bool expected = false;
        if (satisfied_.compare_exchange_strong(expected, true)) {
            prom_.set_value(value);
            return true;
        }
        return false;
    }
};

int main() {
    OncePromise op;
    auto fut = op.get_future();

    if (op.try_set_value(42)) {
        std::cout << "Set to 42" << std::endl;
    }
    if (!op.try_set_value(100)) {
        std::cout << "Already satisfied" << std::endl;
    }
    std::cout << "Value: " << fut.get() << std::endl;
    return 0;
}
```

## Handle Promise in Exception Path

```cpp
// CORRECT — ensure promise is satisfied exactly once
#include <future>
#include <iostream>
#include <stdexcept>

void compute(std::promise<int> prom) {
    try {
        int result = 42;
        prom.set_value(result);
    } catch (...) {
        try {
            prom.set_exception(std::current_exception());
        } catch (const std::future_error&) {
            // promise already satisfied — ignore
        }
    }
}

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    std::thread t(compute, std::move(prom));
    t.join();

    std::cout << "Result: " << fut.get() << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Set value/exception exactly once | Always with `std::promise` |
| Use atomic flag to guard satisfaction | When multiple paths may set the value |
| Catch `future_error` in cleanup | When exception handling may race with set_value |
| Use `std::async` instead | When promise/future pattern is not needed |

## Related Errors

- [std::future already retrieved]({{< relref "/languages/cpp/future-already-retrieved" >}}) — calling get() twice on future.
- [std::future_error]({{< relref "/languages/cpp/future-error" >}}) — general future errors.
- [std::system_error from thread]({{< relref "/languages/cpp/thread-system-error" >}}) — thread creation failures.
