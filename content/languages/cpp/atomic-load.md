---
title: "[Solution] C++ std::atomic load — Atomic Operation Fix"
description: "Fix C++ std::atomic load issues including data races, memory ordering violations, and incorrect atomic usage patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::atomic load — Atomic Operation Fix

`std::atomic::load()` reads a value atomically from an atomic variable. While atomic operations themselves do not throw exceptions, incorrect usage — such as using non-atomic operations on shared data, using wrong memory ordering, or forgetting to initialize atomics — leads to data races and undefined behavior.

## Why Atomic Issues Occur

Common causes include using non-atomic operations on shared variables (data race), using `memory_order_relaxed` when synchronization is needed, forgetting that `store` and `load` on non-lock-free atomics may involve locks, and using atomics when higher-level synchronization is simpler and safer.

## Wrong: Data Race on Shared Variable

```cpp
// WRONG — data race: undefined behavior
#include <thread>
#include <iostream>

int counter = 0;  // NOT atomic — data race

void increment() {
    for (int i = 0; i < 100000; i++) {
        counter++;  // non-atomic read-modify-write
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);
    t1.join();
    t2.join();
    std::cout << "Counter: " << counter << std::endl;
    return 0;
}
```

## Correct: Use std::atomic for Shared Variables

```cpp
// CORRECT — atomic counter prevents data races
#include <thread>
#include <iostream>
#include <atomic>

std::atomic<int> counter{0};

void increment() {
    for (int i = 0; i < 100000; i++) {
        counter.fetch_add(1, std::memory_order_relaxed);
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);
    t1.join();
    t2.join();
    std::cout << "Counter: " << counter.load() << std::endl;
    return 0;
}
```

## Use Proper Memory Ordering

```cpp
// CORRECT — use appropriate memory ordering
#include <thread>
#include <iostream>
#include <atomic>

std::atomic<bool> data_ready{false};
int shared_data = 0;

void producer() {
    shared_data = 42;
    data_ready.store(true, std::memory_order_release);  // synchronize
}

void consumer() {
    while (!data_ready.load(std::memory_order_acquire)) {
        // spin
    }
    std::cout << "Data: " << shared_data << std::endl;  // guaranteed to see 42
}

int main() {
    std::thread t1(producer);
    std::thread t2(consumer);
    t1.join();
    t2.join();
    return 0;
}
```

## Use std::atomic_flag for Spinlock

```cpp
// CORRECT — atomic_flag-based spinlock
#include <thread>
#include <iostream>
#include <atomic>

class SpinLock {
    std::atomic_flag flag_ = ATOMIC_FLAG_INIT;
public:
    void lock() {
        while (flag_.test_and_set(std::memory_order_acquire)) {
            // spin
        }
    }

    void unlock() {
        flag_.clear(std::memory_order_release);
    }
};

SpinLock spin;
int shared_counter = 0;

void increment() {
    for (int i = 0; i < 100000; i++) {
        spin.lock();
        shared_counter++;
        spin.unlock();
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);
    t1.join();
    t2.join();
    std::cout << "Counter: " << shared_counter << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::atomic<T>` | For simple shared counters and flags |
| Use `memory_order_acquire/release` | For producer-consumer synchronization |
| Use `memory_order_relaxed` | When ordering is not critical |
| Use mutex for complex operations | When multiple variables need atomicity |

## Related Errors

- [std::condition_variable]({{< relref "/languages/cpp/condition-variable" >}}) — condition variable synchronization.
- [std::mutex try_lock]({{< relref "/languages/cpp/mutex-try-lock" >}}) — mutex locking issues.
- [std::system_error from thread]({{< relref "/languages/cpp/thread-system-error" >}}) — thread creation failures.
