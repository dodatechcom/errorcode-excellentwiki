---
title: "[Solution] C++ Barrier Error — How to Fix"
description: "Fix C++ std::barrier errors including wrong phase count, arrived count mismatch, and destructor synchronization failures."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Barrier Error — How to Fix

C++20 `std::barrier` synchronizes threads at a synchronization point with a configurable arrival count. Mismatched arrival counts and phase completion callbacks cause deadlocks and undefined behavior.

## Why It Happens

Barrier errors occur when the number of `arrive()` calls doesn't match the expected arrival count, when `wait()` is called from a thread that hasn't arrived, when the completion function throws, or when the barrier is destroyed while threads are still waiting.

## Common Error Messages

1. `std::system_error: barrier error: operation not permitted`
2. Deadlock — not enough arrivals to complete the phase
3. `error: barrier completion function threw an exception`
4. `std::terminate` — barrier destroyed with waiting threads

## How to Fix It

### Fix 1: Match Arrival Count to Thread Count

```cpp
#include <barrier>
#include <thread>
#include <iostream>
#include <vector>

int main() {
    constexpr int num_threads = 4;
    std::barrier sync_point(num_threads);

    std::vector<std::jthread> threads;
    for (int i = 0; i < num_threads; i++) {
        threads.emplace_back([&sync_point, i] {
            std::cout << "Thread " << i << " phase 1\n";
            sync_point.arrive_and_wait();

            std::cout << "Thread " << i << " phase 2\n";
            sync_point.arrive_and_wait();
        });
    }
    // jthreads join automatically
}
```

### Fix 2: Use arrive_and_drop for Dynamic Participation

```cpp
#include <barrier>
#include <thread>
#include <iostream>

int main() {
    std::barrier sync_point(3);

    std::jthread t1([&sync_point] {
        sync_point.arrive_and_wait();
        std::cout << "T1 done\n";
    });

    std::jthread t2([&sync_point] {
        sync_point.arrive_and_drop();  // leave without waiting
        std::cout << "T2 left\n";
    });

    std::jthread t3([&sync_point] {
        sync_point.arrive_and_wait();
        std::cout << "T3 done\n";
    });
}
```

### Fix 3: Provide a Safe Completion Function

```cpp
#include <barrier>
#include <iostream>

// Completion function runs once per phase, by one thread
void on_phase_complete() noexcept {
    std::cout << "--- Phase complete ---\n";
}

int main() {
    std::barrier sync_point(2, on_phase_complete);

    std::jthread t1([&sync_point] { sync_point.arrive_and_wait(); });
    std::jthread t2([&sync_point] { sync_point.arrive_and_wait(); });
}
```

## Common Scenarios

- **Work distribution**: Barrier phases can distribute work across threads iteratively.
- **Phase callback**: The completion function executes on exactly one thread per phase.
- **Dynamic threads**: `arrive_and_drop` lets threads leave while maintaining the barrier.

## Prevent It

1. Ensure the total `arrive()` + `arrive_and_wait()` count equals the barrier's expected count each phase.
2. Use `std::jthread` with barriers to guarantee all threads complete before barrier destruction.
3. Keep completion functions `noexcept` — throwing terminates the program.

## Related Errors

- [Deadlock]({{< relref "/languages/cpp/deadlock" >}}) — barrier-related deadlocks.
- [Data race]({{< relref "/languages/cpp/data-race" >}}) — unsynchronized phase transitions.
- [Latch error]({{< relref "/languages/cpp/cpp-latch-error" >}}) — similar one-shot synchronization.
