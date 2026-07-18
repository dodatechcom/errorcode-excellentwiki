---
title: "[Solution] C++ Chrono Error — How to Fix"
description: "Fix C++ std::chrono errors including type mismatches in duration arithmetic, clock conversion failures, and time point overflow."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time", "runtime"]
weight: 5
comments: true
---

# [Solution] C++ Chrono Error — How to Fix

C++11/20 `std::chrono` provides type-safe time arithmetic with durations, clocks, and time points. Type mismatches between durations and overflow in time point calculations are common errors.

## Why It Happens

Chrono errors occur when mixing incompatible duration types without explicit conversion, when truncating floating-point durations to integer types, when time points overflow for long-running processes, or when using clock conversions between clocks with different epoch origins.

## Common Error Messages

1. `error: no matching function for call to 'chrono::duration_cast'`
2. `error: cannot convert 'chrono::seconds' to 'chrono::milliseconds'`
3. `error: overflow in duration arithmetic`
4. `error: duration has no member 'count'`

## How to Fix It

### Fix 1: Use Duration Cast for Type Conversion

```cpp
#include <chrono>
#include <iostream>

int main() {
    auto ms = std::chrono::milliseconds(1500);

    // WRONG — implicit conversion may truncate
    // std::chrono::seconds s = ms;  // error

    // CORRECT — explicit duration_cast
    auto s = std::chrono::duration_cast<std::chrono::seconds>(ms);
    std::cout << s.count() << " seconds\n";  // 1

    // Use floor/ceil/round for better control (C++17)
    auto s_floor = std::chrono::floor<std::chrono::seconds>(ms);
    std::cout << s_floor.count() << " seconds (floor)\n";
}
```

### Fix 2: Handle Time Point Arithmetic Safely

```cpp
#include <chrono>
#include <iostream>
#include <limits>

int main() {
    auto now = std::chrono::system_clock::now();

    // CORRECT — use safe arithmetic
    auto later = now + std::chrono::hours(24);

    // Avoid overflow with large durations
    constexpr auto max_hours = std::chrono::hours(
        std::chrono::system_clock::duration::max().count() /
        std::chrono::hours(1).count());

    std::cout << "Hours since epoch: "
              << std::chrono::duration_cast<std::chrono::hours>(
                     now.time_since_epoch()).count() << "\n";
}
```

### Fix 3: Convert Between Clocks Carefully

```cpp
#include <chrono>
#include <iostream>

int main() {
    auto sys_now = std::chrono::system_clock::now();
    auto steady_now = std::chrono::steady_clock::now();

    // Convert system_clock to steady_clock (may not be exact)
    auto sys_dur = sys_now.time_since_epoch();
    auto as_steady = std::chrono::steady_clock::time_point(sys_dur);

    // Better: use time_t for system_clock
    std::time_t tt = std::chrono::system_clock::to_time_t(sys_now);
    std::cout << "Time: " << std::ctime(&tt);
}
```

## Common Scenarios

- **Sleep precision**: `sleep_for` may sleep longer than requested due to OS scheduling.
- **Epoch differences**: `system_clock` and `steady_clock` have different epoch points.
- **Floating durations**: `std::chrono::duration<double>` allows fractional seconds.

## Prevent It

1. Always use `std::chrono::duration_cast` or `floor`/`ceil` for explicit duration conversions.
2. Prefer `steady_clock` for measuring elapsed time; use `system_clock` for wall-clock time.
3. Use `using namespace std::chrono_literals` for convenient duration literals (`1s`, `500ms`).

## Related Errors

- [Overflow error]({{< relref "/languages/cpp/overflow" >}}) — arithmetic overflow in durations.
- [Thread sleep]({{< relref "/languages/cpp/sleep-error" >}}) — timing issues in threading.
- [Format error]({{< relref "/languages/cpp/cpp-format-error" >}}) — chrono formatting with std::format.
