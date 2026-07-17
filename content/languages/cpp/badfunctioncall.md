---
title: "[Solution] C++ std::bad_function_call — Empty Callable Invoked Fix"
description: "Fix C++ std::bad_function_call when invoking an empty std::function. Handle null callables and validate function wrappers before invocation."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# [Solution] C++ std::bad_function_call — Empty Callable Invoked Fix

A `std::bad_function_call` exception is thrown when you invoke an empty `std::function` wrapper — one that does not hold any callable target. This typically happens when a `std::function` is default-constructed, reset, or assigned `nullptr`, and then called without checking whether it holds a valid target.

## Why std::bad_function_call Occurs

Common causes include default-constructing a `std::function` and calling it, resetting a `std::function` with `.reset()` then invoking it, moving a `std::function` which leaves the source empty, or assigning `nullptr` to a `std::function`.

## Wrong: Calling an Empty std::function

```cpp
// WRONG — crashes with std::bad_function_call
#include <functional>
#include <iostream>

int main() {
    std::function<int(int, int)> op;
    // op is empty — has no callable target
    int result = op(1, 2);  // throws std::bad_function_call
    std::cout << result << std::endl;
    return 0;
}
```

## Correct: Check if std::function Has a Target Before Calling

```cpp
// CORRECT — verify the function holds a target
#include <functional>
#include <iostream>

int main() {
    std::function<int(int, int)> op;

    if (op) {
        int result = op(1, 2);
        std::cout << result << std::endl;
    } else {
        std::cerr << "Function is not set" << std::endl;
    }
    return 0;
}
```

## Handling Moved std::function Objects

```cpp
// CORRECT — moved-from std::function is empty
#include <functional>
#include <iostream>

int main() {
    std::function<int(int)> square = [](int x) { return x * x; };

    std::function<int(int)> moved = std::move(square);

    // square is now empty
    if (!square) {
        std::cerr << "square is empty after move" << std::endl;
    }

    // moved still works
    if (moved) {
        std::cout << "Result: " << moved(5) << std::endl;
    }
    return 0;
}
```

## Safe Invocation Pattern with Fallback

```cpp
// CORRECT — provide a default callable or fallback
#include <functional>
#include <iostream>
#include <string>

class Pipeline {
    std::function<double(double)> transform_;
public:
    void set_transform(std::function<double(double)> fn) {
        transform_ = std::move(fn);
    }

    double apply(double value) const {
        if (transform_) {
            return transform_(value);
        }
        // Return unmodified value if no transform is set
        return value;
    }
};

int main() {
    Pipeline pipe;
    std::cout << "No transform: " << pipe.apply(42.0) << std::endl;

    pipe.set_transform([](double x) { return x * 2.0; });
    std::cout << "With transform: " << pipe.apply(42.0) << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check `if (func)` before calling | Always when the function may be unset |
| Provide default callable | When a sensible fallback exists |
| Use `std::function::target<T>()` | When you need type information about the stored callable |
| Use `noexcept` callables | When you want to avoid exception propagation |

## Related Errors

- [std::bad_any_cast]({{< relref "/languages/cpp/badany-cast" >}}) — casting with `std::any::cast` fails.
- [std::bad_weak_ptr]({{< relref "/languages/cpp/badweak-ptr" >}}) — locking a `std::weak_ptr` to an expired object.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.
