---
title: "[Solution] C++ std::function Exceptions — Callable Error Fix"
description: "Fix C++ std::function exceptions including bad_function_call, callable type mismatches, and exception propagation from stored callables."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["std-function", "callable", "exception", "type-erasure"]
weight: 5
---

# [Solution] C++ std::function Exceptions — Callable Error Fix

`std::function` can throw `std::bad_function_call` when invoked while empty, and the stored callable can throw any exception which propagates through `std::function::operator()`. Type erasure overhead and exception safety are common concerns.

## Why std::function Exceptions Occur

Common causes include invoking an empty `std::function`, the stored callable throwing an exception, type mismatch between the stored callable's signature and the call signature, and allocation failure when assigning a large callable.

## Wrong: Invoking Empty std::function

```cpp
// WRONG — throws std::bad_function_call
#include <functional>
#include <iostream>

int main() {
    std::function<int(int)> fn;  // empty
    int result = fn(42);  // throws
    return 0;
}
```

## Correct: Check Before Invoking

```cpp
// CORRECT — check if function has a target
#include <functional>
#include <iostream>

int main() {
    std::function<int(int)> fn;

    if (fn) {
        std::cout << fn(42) << std::endl;
    } else {
        std::cerr << "Function is empty" << std::endl;
    }

    fn = [](int x) { return x * 2; };

    if (fn) {
        std::cout << fn(42) << std::endl;
    }
    return 0;
}
```

## Handle Exceptions From Stored Callables

```cpp
// CORRECT — catch exceptions from stored callables
#include <functional>
#include <iostream>
#include <stdexcept>

int safe_divide(int a, int b) {
    if (b == 0) throw std::runtime_error("Division by zero");
    return a / b;
}

int main() {
    std::function<int(int, int)> fn = safe_divide;

    try {
        std::cout << fn(10, 2) << std::endl;
        fn(10, 0);  // throws
    } catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use Function Ref for Non-Owning Callable

```cpp
// CORRECT — use function_ref pattern to avoid allocation
#include <functional>
#include <iostream>

// For performance-critical code, avoid std::function overhead
void apply(double (*fn)(double), double val) {
    std::cout << "Result: " << fn(val) << std::endl;
}

double square(double x) { return x * x; }

int main() {
    apply(square, 5.0);
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check `operator bool()` before invocation | When function might be empty |
| Catch exceptions from stored callables | When callables may throw |
| Use function pointers for simple cases | To avoid std::function overhead |
| Reset with `nullptr` to clear | When you need to invalidate a callback |

## Related Errors

- [std::bad_function_call]({{< relref "/languages/cpp/bad-function-call" >}}) — invoking empty std::function.
- [std::bad_any_cast]({{< relref "/languages/cpp/badany-cast" >}}) — invalid any cast.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.
