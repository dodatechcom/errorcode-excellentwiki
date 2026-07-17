---
title: "[Solution] C++ std::system_error from Thread — Thread Creation Fix"
description: "Fix C++ std::system_error when std::thread operations fail. Handle thread creation, joining, and detachment errors from OS resource limits."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::system_error from Thread — Thread Creation Fix

A `std::system_error` thrown from thread operations indicates an OS-level failure — typically when creating, joining, or detaching a thread. The most common cause is exceeding the system's thread resource limits. The error code provides specific details about what failed.

## Why Thread System Errors Occur

Common causes include exceeding OS thread limits (too many threads), system resource exhaustion (memory, kernel objects), trying to join a thread that has already been joined or detached, calling `join()` or `detach()` on a thread that is not joinable, and thread creation failing due to permission issues.

## Wrong: Creating Too Many Threads Without Handling Errors

```cpp
// WRONG — may throw system_error when resources exhausted
#include <thread>
#include <iostream>
#include <vector>

void worker() {}

int main() {
    std::vector<std::thread> threads;

    for (int i = 0; i < 10000; i++) {
        threads.emplace_back(worker);  // may throw system_error
    }

    for (auto& t : threads) {
        t.join();
    }
    return 0;
}
```

## Correct: Handle Thread Creation Errors

```cpp
// CORRECT — catch system_error from thread creation
#include <thread>
#include <iostream>
#include <system_error>

void worker() {}

int main() {
    try {
        std::thread t(worker);
        t.join();
    } catch (const std::system_error& e) {
        std::cerr << "Thread error: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.code().message() << std::endl;
        if (e.code() == std::errc::resource_unavailable_try_again) {
            std::cerr << "Too many threads — try again later" << std::endl;
        }
        return 1;
    }
    return 0;
}
```

## Check Thread Joinability Before Join

```cpp
// CORRECT — always check joinability
#include <thread>
#include <iostream>

void worker() {}

int main() {
    std::thread t(worker);

    if (t.joinable()) {
        t.join();
    }
    return 0;
}
```

## Use Thread Pool Pattern to Limit Concurrency

```cpp
// CORRECT — limit number of concurrent threads
#include <thread>
#include <iostream>
#include <vector>
#include <queue>
#include <functional>
#include <mutex>
#include <condition_variable>

class ThreadPool {
    std::vector<std::thread> workers_;
    std::queue<std::function<void()>> tasks_;
    std::mutex mutex_;
    std::condition_variable cv_;
    bool stop_ = false;

public:
    explicit ThreadPool(size_t count) {
        for (size_t i = 0; i < count; i++) {
            workers_.emplace_back([this] {
                while (true) {
                    std::function<void()> task;
                    {
                        std::unique_lock lock(mutex_);
                        cv_.wait(lock, [this] { return stop_ || !tasks_.empty(); });
                        if (stop_ && tasks_.empty()) return;
                        task = std::move(tasks_.front());
                        tasks_.pop();
                    }
                    task();
                }
            });
        }
    }

    ~ThreadPool() {
        {
            std::lock_guard lock(mutex_);
            stop_ = true;
        }
        cv_.notify_all();
        for (auto& w : workers_) w.join();
    }

    void enqueue(std::function<void()> task) {
        {
            std::lock_guard lock(mutex_);
            tasks_.push(std::move(task));
        }
        cv_.notify_one();
    }
};

int main() {
    ThreadPool pool(4);
    for (int i = 0; i < 20; i++) {
        pool.enqueue([i] {
            std::cout << "Task " << i << " on thread " << std::this_thread::get_id() << std::endl;
        });
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Catch `std::system_error` from thread ops | When thread resources may be exhausted |
| Check `joinable()` before `join()`/`detach()` | Always before joining or detaching |
| Use thread pool with bounded size | When creating many short-lived tasks |
| Use `std::async` for simpler patterns | When you don't need direct thread control |

## Related Errors

- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — general system errors.
- [std::mutex try_lock]({{< relref "/languages/cpp/mutex-try-lock" >}}) — mutex locking failures.
- [std::condition_variable]({{< relref "/languages/cpp/condition-variable" >}}) — condition variable issues.
