---
title: "[Solution] C++ Latch Error — How to Fix"
description: "Fix C++ std::latch errors including underflow from extra count_down, wait before zero, and one-shot reuse mistakes."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Latch Error — How to Fix

C++20 `std::latch` is a single-use countdown synchronization primitive. Unlike `std::barrier`, it cannot be reset, and exceeding the count or reusing it causes undefined behavior.

## Why It Happens

Latch errors occur when `count_down()` is called more times than the initial count (causing underflow), when threads call `wait()` on a latch that hasn't reached zero, or when attempting to reuse a latch that has already reached zero.

## Common Error Messages

1. `std::system_error: latch underflow`
2. Deadlock — latch never reaches zero due to missing count_down
3. `std::terminate` — latch value goes negative
4. Undefined behavior — reusing spent latch

## How to Fix It

### Fix 1: Ensure Correct Countdown

```cpp
#include <latch>
#include <thread>
#include <iostream>

int main() {
    constexpr int num_tasks = 3;
    std::latch ready(num_tasks);

    std::jthread t1([&ready] {
        std::cout << "Task 1 ready\n";
        ready.count_down();
    });
    std::jthread t2([&ready] {
        std::cout << "Task 2 ready\n";
        ready.count_down();
    });
    std::jthread t3([&ready] {
        std::cout << "Task 3 ready\n";
        ready.count_down();
    });

    ready.wait();
    std::cout << "All tasks ready\n";
}
```

### Fix 2: Use wait_for with Timeout

```cpp
#include <latch>
#include <thread>
#include <chrono>
#include <iostream>

int main() {
    std::latch task_done(1);

    std::jthread worker([&task_done] {
        std::this_thread::sleep_for(std::chrono::seconds(2));
        task_done.count_down();
    });

    // Wait with timeout
    if (task_done.wait_for(std::chrono::seconds(5))) {
        std::cout << "Task completed\n";
    } else {
        std::cout << "Timed out\n";
    }
}
```

### Fix 3: Use arrive_and_wait for Convenience

```cpp
#include <latch>
#include <thread>
#include <iostream>

int main() {
    std::latch sync(4);

    std::jthread threads[4];
    for (int i = 0; i < 4; i++) {
        threads[i] = std::jthread([&sync, i] {
            std::cout << "Thread " << i << "\n";
            sync.arrive_and_wait();  // count down and wait atomically
        });
    }

    std::cout << "All threads reached sync point\n";
}
```

## Common Scenarios

- **Startup synchronization**: Latches are ideal for waiting until all threads have initialized.
- **One-shot pattern**: Unlike barriers, latches cannot be reused across multiple phases.
- **Count mismatch**: If fewer threads arrive than the initial count, `wait()` blocks forever.

## Prevent It

1. Set the latch count to exactly the number of threads that will call `count_down()`.
2. Use `wait_for()` with a timeout to prevent infinite blocking in production code.
3. Never reuse a latch — create a new one for each synchronization phase.

## Related Errors

- [Barrier error]({{< relref "/languages/cpp/cpp-barrier-error" >}}) — reusable synchronization.
- [Deadlock]({{< relref "/languages/cpp/deadlock" >}}) — latch not reaching zero.
- [Semaphore error]({{< relref "/languages/cpp/cpp-counting-semaphore-error" >}}) — similar resource counting.
