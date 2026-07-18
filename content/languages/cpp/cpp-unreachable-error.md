---
title: "[Solution] C++ std::unreachable Error — How to Fix"
description: "Fix C++ std::unreachable errors including incorrect placement, undefined behavior from reaching unreachable code, and compiler optimization issues."
languages: ["cpp"]
severities: ["error"]
error_types: ["undefined-behavior", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ std::unreachable Error — How to Fix

`std::unreachable()` (C++23) marks code paths as never reachable, allowing compiler optimizations. Incorrect placement leads to undefined behavior when the code is actually reached, and can cause silent data corruption.

## Why It Happens

unreachable errors occur when `std::unreachable()` is placed in paths that can actually be executed, when the compiler's flow analysis disagrees with the programmer's assumption, when exception handlers mark unreachable code that exceptions can reach, or when switch-case statements have missing cases after `std::unreachable()`.

## Common Error Messages

1. `warning: 'std::unreachable()' will cause undefined behavior if reached`
2. `runtime error: reached unreachable code`
3. `undefined behavior: execution reached std::unreachable()`
4. `error: unreachable code after return statement`

## How to Fix It

### Fix 1: Only Use unreachable in Verified Dead Code

```cpp
#include <iostream>
#include <utility>

enum class Direction { Up, Down, Left, Right };

const char* direction_name(Direction d) {
    switch (d) {
        case Direction::Up:    return "Up";
        case Direction::Down:  return "Down";
        case Direction::Left:  return "Left";
        case Direction::Right: return "Right";
    }

    // CORRECT — only if enum is fully handled above
    std::unreachable();
}

int main() {
    std::cout << direction_name(Direction::Up) << "\n";
    return 0;
}
```

### Fix 2: Don't Use unreachable with Assertions

```cpp
#include <iostream>
#include <cassert>
#include <utility>

int process(int value) {
    assert(value >= 0 && "value must be non-negative");

    // WRONG — assert is removed in release builds, then code is reachable
    // if (value < 0) std::unreachable();

    // CORRECT — use unreachable only after provable conditions
    if (value < 0) {
        // handle error or throw
        throw std::invalid_argument("negative value");
    }

    return value * 2;
}

int main() {
    std::cout << process(5) << "\n";
    return 0;
}
```

### Fix 3: Use for Compiler Optimization in Hot Loops

```cpp
#include <iostream>
#include <utility>
#include <vector>

void sum_non_negative(const std::vector<int>& values) {
    long total = 0;
    for (int v : values) {
        if (v < 0) continue;

        // If we can prove v >= 0 at this point
        total += v;
    }
    std::cout << "Total: " << total << "\n";
}

int main() {
    sum_non_negative({1, -2, 3, 4, -5, 6});
    return 0;
}
```

### Fix 4: Avoid Unreachable with Complex Control Flow

```cpp
#include <iostream>
#include <optional>
#include <utility>

std::optional<int> find_value(const std::vector<int>& vec, int target) {
    for (int v : vec) {
        if (v == target) return v;
    }
    return std::nullopt;
}

int main() {
    std::vector<int> data = {1, 2, 3, 4, 5};

    auto result = find_value(data, 10);
    if (result) {
        std::cout << "Found: " << *result << "\n";
    } else {
        std::cout << "Not found\n";
        // Don't put std::unreachable() here — result might be empty
    }

    return 0;
}
```

## Common Scenarios

- **Switch on enum**: Adding a new enum value without updating the switch leaves dead code claims false.
- **Debug-only checks**: Using `unreachable()` after assertions that are disabled in release.
- **Optimistic assumptions**: Marking rare-but-possible paths as unreachable to help the optimizer.

## Prevent It

1. Verify that all code paths before `std::unreachable()` provably terminate or throw.
2. Never use `std::unreachable()` after `assert()` — asserts are removed in release mode.
3. Add comments explaining why the path is unreachable and test with sanitizers in debug builds.

## Related Errors

- [UBSan error]({{< relref "/languages/cpp/cpp-ubsan-error" >}}) — undefined behavior detection.
- [Contract error]({{< relref "/languages/cpp/cpp-contract-error" >}}) — assertion and contract issues.
- [Logic error]({{< relref "/languages/cpp/logic-error" >}}) — program logic issues.
