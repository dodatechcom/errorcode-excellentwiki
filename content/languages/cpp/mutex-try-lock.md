---
title: "[Solution] C++ std::mutex try_lock — Mutex Lock Failure Fix"
description: "Fix C++ std::mutex try_lock failures and deadlocks. Learn proper mutex usage with lock_guard, unique_lock, and deadlock avoidance."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::mutex try_lock — Mutex Lock Failure Fix

`std::mutex::try_lock()` attempts to lock the mutex without blocking — it returns `false` if the mutex is already locked. While `try_lock` itself does not throw, `std::mutex::lock()` throws `std::system_error` with `resource_deadlock_would_occur` if deadlock is detected, and improper use of try_lock can lead to missed critical sections or livelock.

## Why Mutex Lock Failures Occur

Common causes include recursive locking without `std::recursive_mutex`, deadlock from inconsistent lock ordering across threads, using `try_lock` in a busy-wait loop without backoff, and calling `lock()` on a mutex that the current thread already holds.

## Wrong: Recursive Locking Without recursive_mutex

```cpp
// WRONG — undefined behavior or throws system_error
#include <mutex>
#include <iostream>

std::mutex mtx;

void recursive_func(int n) {
    mtx.lock();  // deadlock on second call
    std::cout << "n = " << n << std::endl;
    if (n > 0) recursive_func(n - 1);
    mtx.unlock();
}

int main() {
    recursive_func(3);
    return 0;
}
```

## Correct: Use lock_guard or unique_lock

```cpp
// CORRECT — use RAII locking
#include <mutex>
#include <iostream>

std::mutex mtx;

void safe_func() {
    std::lock_guard<std::mutex> lock(mtx);
    std::cout << "Thread-safe operation" << std::endl;
}  // mutex automatically unlocked

int main() {
    safe_func();
    return 0;
}
```

## Use try_lock With Proper Handling

```cpp
// CORRECT — use try_lock with non-blocking pattern
#include <mutex>
#include <iostream>
#include <chrono>
#include <thread>

std::mutex mtx;

void try_lock_pattern() {
    if (mtx.try_lock()) {
        std::cout << "Lock acquired" << std::endl;
        mtx.unlock();
    } else {
        std::cout << "Could not acquire lock — try later" << std::endl;
    }
}

int main() {
    std::thread t1(try_lock_pattern);
    std::thread t2(try_lock_pattern);
    t1.join();
    t2.join();
    return 0;
}
```

## Use std::lock for Multiple Mutexes

```cpp
// CORRECT — lock multiple mutexes without deadlock
#include <mutex>
#include <iostream>

std::mutex mtx1;
std::mutex mtx2;

void safe_both() {
    std::lock(mtx1, mtx2);
    std::lock_guard<std::mutex> lock1(mtx1, std::adopt_lock);
    std::lock_guard<std::mutex> lock2(mtx2, std::adopt_lock);
    std::cout << "Both mutexes locked safely" << std::endl;
}

int main() {
    safe_both();
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::lock_guard` | For simple scoped locking |
| Use `std::unique_lock` | When you need deferred or timed locking |
| Use `std::recursive_mutex` | When recursive locking is needed |
| Use `std::lock(m1, m2)` | When locking multiple mutexes |

## Related Errors

- [std::system_error from thread]({{< relref "/languages/cpp/thread-system-error" >}}) — thread creation failures.
- [std::condition_variable]({{< relref "/languages/cpp/condition-variable" >}}) — condition variable issues.
- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — general system errors.
