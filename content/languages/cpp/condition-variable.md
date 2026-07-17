---
title: "[Solution] C++ std::condition_variable — Condition Variable Fix"
description: "Fix C++ std::condition_variable issues including spurious wakeups, missed notifications, and deadlocks. Learn proper thread synchronization."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::condition_variable — Condition Variable Fix

`std::condition_variable` is used for thread synchronization — one thread waits for a condition while another signals it. Common bugs include spurious wakeups (waking without the condition being true), missed notifications (signaling before anyone is waiting), and deadlocks from holding the mutex during `wait`.

## Why Condition Variable Issues Occur

Common causes include not using a predicate with `wait()` (causing spurious wakeup bugs), signaling without holding the associated mutex, holding the mutex while notifying (reducing concurrency), and using `notify_one` when multiple threads may need to wake.

## Wrong: Not Using Predicate With Wait

```cpp
// WRONG — spurious wakeup causes incorrect behavior
#include <thread>
#include <mutex>
#include <iostream>
#include <vector>

std::mutex mtx;
std::condition_variable cv;
bool ready = false;
int data = 0;

void worker() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock);  // WRONG — may wake spuriously when ready is still false
    std::cout << "Data: " << data << std::endl;
}

int main() {
    std::thread t(worker);

    {
        std::lock_guard<std::mutex> lock(mtx);
        data = 42;
        ready = true;
    }
    cv.notify_one();

    t.join();
    return 0;
}
```

## Correct: Always Use Predicate With Wait

```cpp
// CORRECT — predicate prevents spurious wakeup issues
#include <thread>
#include <mutex>
#include <iostream>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv;
bool ready = false;
int data = 0;

void worker() {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [] { return ready; });  // waits until ready is true
    std::cout << "Data: " << data << std::endl;
}

int main() {
    std::thread t(worker);

    {
        std::lock_guard<std::mutex> lock(mtx);
        data = 42;
        ready = true;
    }
    cv.notify_one();

    t.join();
    return 0;
}
```

## Use Condition Variable With Queue

```cpp
// CORRECT — producer-consumer pattern
#include <thread>
#include <mutex>
#include <iostream>
#include <condition_variable>
#include <queue>

std::mutex mtx;
std::condition_variable cv;
std::queue<int> tasks;
bool done = false;

void producer() {
    for (int i = 0; i < 10; i++) {
        {
            std::lock_guard<std::mutex> lock(mtx);
            tasks.push(i);
        }
        cv.notify_one();
    }
    {
        std::lock_guard<std::mutex> lock(mtx);
        done = true;
    }
    cv.notify_all();
}

void consumer() {
    while (true) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [] { return !tasks.empty() || done; });

        while (!tasks.empty()) {
            int task = tasks.front();
            tasks.pop();
            lock.unlock();
            std::cout << "Processing: " << task << std::endl;
            lock.lock();
        }

        if (done && tasks.empty()) break;
    }
}

int main() {
    std::thread prod(producer);
    std::thread cons(consumer);

    prod.join();
    cons.join();
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Always use predicate with `wait()` | Always — prevents spurious wakeup bugs |
| Hold mutex when modifying shared state | Always when signaling conditions |
| Use `notify_all()` | When multiple threads may need to wake |
| Use `std::unique_lock` with `wait()` | Required for condition variable waits |

## Related Errors

- [std::mutex try_lock]({{< relref "/languages/cpp/mutex-try-lock" >}}) — mutex locking failures.
- [std::atomic load]({{< relref "/languages/cpp/atomic-load" >}}) — atomic operation issues.
- [std::system_error from thread]({{< relref "/languages/cpp/thread-system-error" >}}) — thread creation failures.
