---
title: "[Solution] C++ std::packaged_task — Packaged Task Error Fix"
description: "Fix C++ std::packaged_task errors including calling without a function, double invocation, and exception propagation. Learn async task patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::packaged_task — Packaged Task Error Fix

A `std::packaged_task` wraps a callable and associates it with a `std::future`. Errors occur when you call the task twice (it can only be invoked once), call it without a stored function, or when the stored callable throws an exception. The exception is propagated through the associated future.

## Why Packaged Task Errors Occurs

Common causes include calling `operator()` on a task that has already been invoked, constructing a task with a move-only callable and moving it, task destruction without invocation (breaks the promise), and the stored callable throwing an exception.

## Wrong: Invoking Packaged Task Twice

```cpp
// WRONG — throws std::future_error
#include <future>
#include <iostream>

int main() {
    std::packaged_task<int()> task([] { return 42; });

    auto fut1 = task.get_future();
    task();  // first invocation — OK

    auto fut2 = task.get_future();  // future already retrieved? No — wrong usage
    task();  // throws — already invoked
    return 0;
}
```

## Correct: Invoke Packaged Task Once

```cpp
// CORRECT — invoke task exactly once
#include <future>
#include <iostream>

int main() {
    std::packaged_task<int()> task([] { return 42; });
    auto fut = task.get_future();

    task();  // invoke once

    std::cout << "Result: " << fut.get() << std::endl;
    return 0;
}
```

## Propagate Exceptions Through Packaged Task

```cpp
// CORRECT — exceptions are forwarded to the future
#include <future>
#include <iostream>
#include <stdexcept>

int main() {
    std::packaged_task<int()> task([]() -> int {
        throw std::runtime_error("Task failed");
    });

    auto fut = task.get_future();
    task();

    try {
        int result = fut.get();
        std::cout << "Result: " << result << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Caught: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use Packaged Task With Thread

```cpp
// CORRECT — run packaged_task on a separate thread
#include <future>
#include <iostream>
#include <thread>

int compute(int a, int b) {
    return a + b;
}

int main() {
    std::packaged_task<int(int, int)> task(compute);
    auto fut = task.get_future();

    std::thread t(std::move(task), 3, 4);
    t.join();

    std::cout << "Result: " << fut.get() << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Invoke `operator()` exactly once | Always — task is single-use |
| Catch exceptions via `future::get()` | When callable may throw |
| Use `std::move(task)` to pass to thread | When running task on another thread |
| Check `valid()` before invoking | When task might not have a callable |

## Related Errors

- [std::future already retrieved]({{< relref "/languages/cpp/future-already-retrieved" >}}) — calling get() twice.
- [std::promise already satisfied]({{< relref "/languages/cpp/promise-already-satisfied" >}}) — setting value twice.
- [std::future_error]({{< relref "/languages/cpp/future-error" >}}) — general future errors.
