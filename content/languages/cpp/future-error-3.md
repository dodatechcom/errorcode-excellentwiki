---
title: "[Solution] C++ std::future_error — Broken Promise / Future Already Retrieved Fix"
description: "Fix C++ std::future_error when a promise is broken or a future is retrieved twice. Handle asynchronous result passing correctly."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["future-error", "future_error", "promise", "broken-promise", "future", "async"]
weight: 5
---

# [Solution] C++ std::future_error — Broken Promise / Future Already Retrieved Fix

A `std::future_error` is thrown when operations on `std::future` or `std::promise` are used incorrectly. Common variants include `broken_promise` (the promise was destroyed without setting a value), `future_already_retrieved` (`.get()` or `.share()` was called twice), and `promise_already_satisfied` (setting a value twice on the same promise). The error codes are defined in `<future>`.

## Common Causes

- **Promise destroyed without setting a value** — the promise goes out of scope before `set_value()` is called, resulting in `broken_promise`
- **Calling future.get() twice** — only one retrieval is allowed; the second call throws `future_already_retrieved`
- **Setting promise value twice** — `set_value()` called more than once throws `promise_already_satisfied`
- **Shared future moved improperly** — the shared state is invalidated

## How to Fix

### Fix 1: Always set a value before promise is destroyed

```cpp
#include <iostream>
#include <future>
#include <thread>

int main() {
    std::promise<int> prom;
    std::future<int> fut = prom.get_future();

    std::thread t([&prom]() {
        try {
            prom.set_value(42);
        } catch (const std::future_error& e) {
            std::cerr << "Promise error: " << e.what() << std::endl;
        }
    });

    std::cout << "Result: " << fut.get() << std::endl;
    t.join();
    return 0;
}
```

### Fix 2: Only retrieve the future once

```cpp
#include <iostream>
#include <future>

int main() {
    std::promise<int> prom;
    std::future<int> fut = prom.get_future();
    prom.set_value(10);

    std::cout << "First get: " << fut.get() << std::endl;

    /* WRONG — second get() throws future_already_retrieved */
    // std::cout << fut.get() << std::endl;

    return 0;
}
```

### Fix 3: Set exception on promise instead of value when appropriate

```cpp
#include <iostream>
#include <future>
#include <thread>
#include <stdexcept>

int main() {
    std::promise<int> prom;
    std::future<int> fut = prom.get_future();

    std::thread t([&prom]() {
        try {
            throw std::runtime_error("computation failed");
        } catch (...) {
            prom.set_exception(std::current_exception());
        }
    });

    try {
        int result = fut.get();
        std::cout << "Result: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Got exception: " << e.what() << std::endl;
    }

    t.join();
    return 0;
}
```

### Fix 4: Use shared_future when multiple consumers need the result

```cpp
#include <iostream>
#include <future>
#include <thread>

int main() {
    std::promise<int> prom;
    std::shared_future<int> sf = prom.get_future().share();

    std::thread t1([sf]() { std::cout << "T1: " << sf.get() << std::endl; });
    std::thread t2([sf]() { std::cout << "T2: " << sf.get() << std::endl; });

    prom.set_value(99);

    t1.join();
    t2.join();
    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <future>
#include <stdexcept>

int main() {
    /* Broken promise */
    std::future<int> fut;
    {
        std::promise<int> prom;
        fut = prom.get_future();
        /* promise destroyed here without set_value */
    }
    try {
        std::cout << fut.get() << std::endl;
    } catch (const std::future_error& e) {
        std::cerr << e.what() << std::endl;  // broken_promise
    }

    return 0;
}
```

## Related Errors

- [std::promise_already_satisfied]({{< relref "/languages/cpp/promise-already-satisfied" >}}) — setting value twice
- [std::packaged_task error]({{< relref "/languages/cpp/packaged-task" >}}) — task not invoked before get()
- [std::thread error]({{< relref "/languages/cpp/condition-variable" >}}) — threading synchronization issues
