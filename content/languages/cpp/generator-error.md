---
title: "[Solution] C++23 Generator Error — Coroutine Generator Fix"
description: "Fix C++23 std::generator errors including premature destruction, invalid coroutine usage, and yield patterns. Learn coroutine generator patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["generator", "coroutine", "c++23", "lazy"]
weight: 5
---

# [Solution] C++23 Generator Error — Coroutine Generator Fix

`std::generator<T>` (C++23) is a lazy coroutine-based generator. Errors occur when the generator is destroyed before iteration completes, when yield is called incorrectly, when the coroutine frame is corrupted, or when using generators in ways that violate their borrowing semantics.

## Why Generator Errors Occur

Common causes include destroying a generator while it is still being iterated, yielding references to local variables (dangling), using generators across thread boundaries, and incorrect coroutine promise types.

## Wrong: Yielding Reference to Local Variable

```cpp
// WRONG — dangling reference from generator
#include <generator>
#include <iostream>

std::generator<int&> bad_gen() {
    int local = 42;
    co_yield local;  // local destroyed when coroutine suspends
}

int main() {
    for (int& val : bad_gen()) {
        std::cout << val << std::endl;  // UB — dangling reference
    }
    return 0;
}
```

## Correct: Yield By Value

```cpp
// CORRECT — yield by value for safe copies
#include <generator>
#include <iostream>

std::generator<int> good_gen() {
    for (int i = 0; i < 5; i++) {
        co_yield i;  // value copy — safe
    }
}

int main() {
    for (int val : good_gen()) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Use Generator With Filtering

```cpp
// CORRECT — generator with lazy evaluation
#include <generator>
#include <iostream>

std::generator<int> fibonacci() {
    int a = 0, b = 1;
    while (true) {
        co_yield a;
        auto temp = a;
        a = b;
        b = temp + b;
    }
}

int main() {
    int count = 0;
    for (int val : fibonacci()) {
        std::cout << val << " ";
        if (++count >= 10) break;
    }
    std::cout << std::endl;
    return 0;
}
```

## Safe Generator Lifecycle

```cpp
// CORRECT — ensure generator is consumed properly
#include <generator>
#include <iostream>
#include <vector>

std::generator<int> range_gen(int start, int end) {
    for (int i = start; i < end; i++) {
        co_yield i;
    }
}

int main() {
    std::vector<int> result;

    for (int val : range_gen(0, 10)) {
        result.push_back(val);
    }

    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Yield by value, not by reference | When local variables might go out of scope |
| Consume generator fully or break early | To avoid resource leaks |
| Use `std::vector` to collect results | When you need the values after iteration |
| Avoid sharing generators across threads | Generators are not thread-safe |

## Related Errors

- [coroutine error]({{< relref "/languages/cpp/coroutine-error" >}}) — general coroutine errors.
- [std::ranges error]({{< relref "/languages/cpp/ranges-error" >}}) — ranges algorithm errors.
- [std::span error]({{< relref "/languages/cpp/span-error" >}}) — span bounds errors.
