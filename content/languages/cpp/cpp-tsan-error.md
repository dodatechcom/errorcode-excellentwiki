---
title: "[Solution] C++ TSan Error — How to Fix"
description: "Fix C++ ThreadSanitizer errors including data races, deadlocks, and incorrect synchronization in multithreaded C++ applications."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ TSan Error — How to Fix

ThreadSanitizer (TSan) detects data races between threads accessing the same memory without synchronization, lock order violations that can cause deadlocks, and incorrectly ordered atomic operations.

## Why It Happens

TSan errors occur when two threads access the same memory location concurrently with at least one write and no synchronization, when mutexes are locked in inconsistent order across threads, when atomic variables are used with incorrect memory ordering, or when thread creation/join is not properly synchronized.

## Common Error Messages

1. `WARNING: ThreadSanitizer: data race`
2. `WARNING: ThreadSanitizer: lock-order-inversion`
3. `WARNING: ThreadSanitizer: thread creation/join deadlock`
4. `WARNING: ThreadSanitizer: atomics uses relaxed memory ordering`

## How to Fix It

### Fix 1: Protect Shared Data with Mutex

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

// WRONG — data race
// int counter = 0;

// CORRECT — protect with mutex
std::mutex mtx;
int counter = 0;

void increment() {
    for (int i = 0; i < 1000; i++) {
        std::lock_guard<std::mutex> lock(mtx);
        counter++;
    }
}

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 4; i++) {
        threads.emplace_back(increment);
    }
    for (auto& t : threads) t.join();

    std::cout << "Counter: " << counter << "\n";  // 4000
    return 0;
}
```

### Fix 2: Fix Lock Order Inversion

```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mutex_a;
std::mutex mutex_b;

// WRONG — potential deadlock
// Thread 1: lock A, then B
// Thread 2: lock B, then A

// CORRECT — always lock in same order
void thread_func() {
    std::lock(mutex_a, mutex_b);  // lock both atomically
    std::lock_guard<std::mutex> lock_a(mutex_a, std::adopt_lock);
    std::lock_guard<std::mutex> lock_b(mutex_b, std::adopt_lock);

    std::cout << "Thread safe\n";
}

int main() {
    std::thread t1(thread_func);
    std::thread t2(thread_func);
    t1.join();
    t2.join();
    return 0;
}
```

### Fix 3: Use Atomics Correctly

```cpp
#include <iostream>
#include <thread>
#include <atomic>
#include <vector>

std::atomic<int> atomic_counter{0};

void increment() {
    for (int i = 0; i < 1000; i++) {
        // CORRECT — atomic operations are thread-safe
        atomic_counter.fetch_add(1, std::memory_order_relaxed);
    }
}

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 4; i++) {
        threads.emplace_back(increment);
    }
    for (auto& t : threads) t.join();

    std::cout << "Counter: " << atomic_counter.load() << "\n";
    return 0;
}
```

### Fix 4: Use Thread-Local Storage

```cpp
#include <iostream>
#include <thread>
#include <vector>

// CORRECT — thread_local eliminates data races
thread_local int local_counter = 0;

void increment() {
    for (int i = 0; i < 1000; i++) {
        local_counter++;
    }
    std::cout << "Thread " << std::this_thread::get_id()
              << " counter: " << local_counter << "\n";
}

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 4; i++) {
        threads.emplace_back(increment);
    }
    for (auto& t : threads) t.join();
    return 0;
}
```

## Common Scenarios

- **Shared counters**: Multiple threads incrementing the same variable without locks.
- **Container access**: Reading/writing to `std::vector` from multiple threads without synchronization.
- **Lock ordering**: Different threads acquiring locks in different orders.

## Prevent It

1. Run TSan on all multithreaded code: `g++ -fsanitize=thread -g -O1`.
2. Use `std::mutex` or `std::shared_mutex` for all shared mutable state.
3. Prefer thread-local storage for data that doesn't need to be shared.

## Related Errors

- [OpenMP error]({{< relref "/languages/cpp/cpp-openmp-error.md" >}}) — parallel programming issues.
- [Condition variable]({{< relref "/languages/cpp/condition-variable" >}}) — synchronization issues.
- [Mutex try lock]({{< relref "/languages/cpp/mutex-try-lock" >}}) — mutex operation issues.
