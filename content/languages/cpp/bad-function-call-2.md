---
title: "[Solution] C++ std::bad_function_call — Empty Callable Invocation Fix"
description: "Fix C++ std::bad_function_call when invoking an empty std::function. Learn safe callable wrapping and null-check patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-function-call", "std-function", "callable", "exception"]
weight: 5
---

# [Solution] C++ std::bad_function_call — Empty Callable Invocation Fix

A `std::bad_function_call` is thrown when you invoke a `std::function` that does not contain a callable target — i.e., it is empty. This typically happens when a `std::function` is default-constructed or reset without assigning a callable.

## Why std::bad_function_call Occurs

Common causes include invoking a default-constructed `std::function`, calling a `std::function` after `reset()` was called on it, storing a null function pointer in `std::function`, and moving from a `std::function` leaving the source empty.

## Wrong: Invoking an Empty std::function

```cpp
// WRONG — throws std::bad_function_call
#include <functional>
#include <iostream>

int main() {
    std::function<int(int, int)> op;  // empty
    int result = op(1, 2);  // throws
    std::cout << result << std::endl;
    return 0;
}
```

## Correct: Check if std::function Has a Target

```cpp
// CORRECT — check before invoking
#include <functional>
#include <iostream>

int main() {
    std::function<int(int, int)> op;

    if (op) {
        int result = op(1, 2);
        std::cout << "Result: " << result << std::endl;
    } else {
        std::cerr << "Function is empty" << std::endl;
    }
    return 0;
}
```

## Assign a Callable Before Use

```cpp
// CORRECT — assign a callable before invoking
#include <functional>
#include <iostream>

int main() {
    std::function<int(int, int)> op;

    op = [](int a, int b) { return a + b; };

    if (op) {
        std::cout << "Result: " << op(3, 4) << std::endl;
    }
    return 0;
}
```

## Use std::function as Optional Callable

```cpp
// CORRECT — wrap optional callbacks safely
#include <functional>
#include <iostream>
#include <string>

class Processor {
    std::function<void(const std::string&)> on_error_;

public:
    void set_error_handler(std::function<void(const std::string&)> handler) {
        on_error_ = std::move(handler);
    }

    void process(const std::string& data) {
        if (data.empty()) {
            if (on_error_) {
                on_error_("Empty data received");
            } else {
                std::cerr << "No error handler set" << std::endl;
            }
            return;
        }
        std::cout << "Processing: " << data << std::endl;
    }
};

int main() {
    Processor p;
    p.set_error_handler([](const std::string& msg) {
        std::cerr << "Error: " << msg << std::endl;
    });
    p.process("");
    p.process("valid data");
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check `operator bool()` before invocation | When `std::function` might be empty |
| Assign a callable before use | Always after default construction |
| Use `reset()` intentionally | When you need to clear a callback |
| Store `nullptr` as fallback behavior | When an optional callback pattern is needed |

## Related Errors

- [std::bad_any_cast]({{< relref "/languages/cpp/badany-cast" >}}) — invalid `std::any` type cast.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.
- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — failed `dynamic_cast`.
