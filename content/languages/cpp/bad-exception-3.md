---
title: "[Solution] C++ std::bad_exception — Unexpected Exception in Dynamic Exception Specification Fix"
description: "Fix C++ std::bad_exception thrown when an unexpected exception escapes a function with a dynamic exception specification."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-exception", "bad_exception", "dynamic-exception-spec", "unexpected", "noexcept"]
weight: 5
---

# [Solution] C++ std::bad_exception — Unexpected Exception in Dynamic Exception Specification Fix

A `std::bad_exception` is thrown when a function with a dynamic exception specification (e.g., `throw(int)`) throws an exception not listed in its specification. Since C++11, dynamic exception specifications are deprecated and `noexcept` should be used instead. If a `noexcept` function throws, `std::terminate()` is called, but `std::bad_exception` still applies to legacy `throw()` specifications.

## Common Causes

- **Dynamic exception specification violated** — a function declared `throw(int)` throws something other than `int`
- **Legacy exception specifications** — code using pre-C++11 `throw()` specifiers
- **std::unexpected_handler called** — the default handler throws `std::bad_exception`
- **Mismatched exception types across library boundaries**

## How to Fix

### Fix 1: Replace dynamic exception specifications with noexcept

```cpp
#include <iostream>

/* WRONG — legacy dynamic exception specification */
// void func() throw(int) { throw "string"; }  // throws std::bad_exception

/* CORRECT — use noexcept */
void func() noexcept {
    // noexcept functions should not throw
    // If they do, std::terminate() is called
}

/* CORRECT — allow all exceptions (default) */
void func_all() {
    throw std::runtime_error("error");  // fine — no exception spec
}

int main() {
    func_all();
    return 0;
}
```

### Fix 2: Use std::current_exception and std::exception_ptr for deferred handling

```cpp
#include <iostream>
#include <exception>
#include <stdexcept>

void worker(std::exception_ptr& eptr) {
    try {
        throw std::runtime_error("worker failed");
    } catch (...) {
        eptr = std::current_exception();
    }
}

int main() {
    std::exception_ptr eptr;
    worker(eptr);

    try {
        if (eptr) std::rethrow_exception(eptr);
    } catch (const std::exception& e) {
        std::cerr << "Caught: " << e.what() << std::endl;
    }

    return 0;
}
```

### Fix 3: Avoid throwing from noexcept contexts

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void safe_sort(std::vector<int>& v) noexcept {
    /* Use std::sort which may throw, but mark the function noexcept
       only if you're sure the comparison operator doesn't throw */
    try {
        std::sort(v.begin(), v.end());
    } catch (...) {
        /* Swallow or log — don't let exception escape noexcept */
        std::cerr << "Sort failed" << std::endl;
    }
}

int main() {
    std::vector<int> nums = {5, 3, 1, 4, 2};
    safe_sort(nums);
    for (int n : nums) std::cout << n << " ";
    std::cout << std::endl;
    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <exception>
#include <stdexcept>

void legacy_func() throw(int) {
    throw std::runtime_error("not an int");  // triggers std::bad_exception
}

int main() {
    try {
        legacy_func();
    } catch (const std::bad_exception& e) {
        std::cerr << "bad_exception: " << e.what() << std::endl;
    } catch (...) {
        std::cerr << "Caught something else" << std::endl;
    }
    return 0;
}
```

## Related Errors

- [std::runtime_error]({{< relref "/languages/cpp/runtime-error12" >}}) — general runtime exception
- [std::logic_error]({{< relref "/languages/cpp/logic-error-3" >}}) — program logic bugs
- [std::bad_function_call]({{< relref "/languages/cpp/bad-function-call" >}}) — invoking an empty std::function
