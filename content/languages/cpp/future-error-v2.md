---
title: "[Solution] std::future Promise Already Satisfied Fix"
description: "Fix std::future promise already satisfied errors. Handle duplicate set_value calls and thread synchronization."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# std::future Promise Already Satisfied

Fix std::future promise already satisfied errors. Handle duplicate set_value calls and thread synchronization.

## What This Error Means

`std::promise::set_value()` throws `std::future_error` with `std::future_errc::promise_already_satisfied` if called more than once:

```
terminate called after throwing an instance of 'std::future_error'
  what():  std::future_error: Promise already satisfied
```

## Common Causes

```cpp
// Cause 1: Calling set_value twice
std::promise<int> p;
p.set_value(42);
p.set_value(100); // Throws!

// Cause 2: Multiple threads racing to set the same promise
// Cause 3: Promise captured by value in lambda (copied)
// Cause 4: Forgetting to use std::shared_future for multiple waits
```

## How to Fix

### Fix 1: Use a flag or once_flag to prevent double-set

```cpp
#include <future>
#include <mutex>

class SharedPromise {
    std::promise<int> promise_;
    std::once_flag flag_;
public:
    void set_value(int val) {
        std::call_once(flag_, [&]() {
            promise_.set_value(val);
        });
    }
    std::future<int> get_future() { return promise_.get_future(); }
};
```

### Fix 2: Use shared_future for multiple consumers

```cpp
#include <future>
#include <iostream>

int main() {
    std::promise<int> p;
    auto shared = p.get_future().share(); // shared_future

    std::thread t1([shared]() {
        std::cout << "Thread 1: " << shared.get() << std::endl;
    });

    std::thread t2([shared]() {
        std::cout << "Thread 2: " << shared.get() << std::endl;
    });

    p.set_value(42);
    t1.join();
    t2.join();
    return 0;
}
```

### Fix 3: Use std::optional to track state

```cpp
#include <future>
#include <optional>

int main() {
    std::promise<int> p;
    std::optional<int> result;

    try {
        result = 42;
        p.set_value(*result);
    } catch (const std::future_error&) {
        // Already set, safe to ignore
    }

    std::cout << p.get_future().get() << std::endl;
    return 0;
}
```

## Examples

```cpp
#include <future>
#include <thread>
#include <iostream>
#include <mutex>

class TaskRunner {
    std::promise<std::string> result_promise_;
    std::once_flag done_flag_;
    std::mutex mu_;

public:
    std::future<std::string> get_future() {
        return result_promise_.get_future();
    }

    void complete(const std::string& result) {
        std::call_once(done_flag_, [this, &result]() {
            result_promise_.set_value(result);
        });
    }
};

int main() {
    TaskRunner runner;
    auto future = runner.get_future();

    std::thread worker([&runner]() {
        runner.complete("Task finished");
        runner.complete("Duplicate"); // Ignored safely
    });

    std::cout << future.get() << std::endl;
    worker.join();
    return 0;
}
```

## Related Errors

- [Future Error]({{< relref "/languages/cpp/future-error" >}}) — future error
- [Mutex Try Lock]({{< relref "/languages/cpp/mutex-try-lock" >}}) — mutex error
- [Thread System Error]({{< relref "/languages/cpp/thread-system-error" >}}) — thread error
