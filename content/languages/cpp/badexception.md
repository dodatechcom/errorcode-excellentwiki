---
title: "[Solution] C++ std::bad_exception — Unexpected Exception Fix"
description: "Fix C++ std::bad_exception when unexpected exceptions are thrown. Handle dynamic exception specifications and unexpected handler."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# [Solution] C++ std::bad_exception — Unexpected Exception Fix

A `std::bad_exception` is thrown when an unexpected exception occurs in a function with a dynamic exception specification (deprecated in C++11, removed in C++20). When a function throws an exception not listed in its `throw()` specification, the runtime calls the unexpected handler, which by default throws `std::bad_exception`. In modern C++ (C++17+), dynamic exception specifications are removed, making this exception mostly historical.

## Why std::bad_exception Occurs

Common causes include using the deprecated `throw(type)` specification with an unlisted exception type, unexpected exceptions propagating through functions with `throw()` specifications, and legacy code that relies on dynamic exception specifications.

## Wrong: Using Dynamic Exception Specifications

```cpp
// WRONG — deprecated throw() specification
// If foo throws something other than std::bad_exception, std::bad_exception is thrown
#include <iostream>
#include <stdexcept>

void foo() throw(std::bad_exception) {
    throw std::runtime_error("unexpected");  // not in throw list
}

int main() {
    try {
        foo();
    } catch (const std::bad_exception& e) {
        std::cerr << "bad_exception: " << e.what() << std::endl;
    }
    return 0;
}
```

## Correct: Use noexcept or No Exception Specification

```cpp
// CORRECT — use noexcept or no specification
#include <iostream>
#include <stdexcept>

void foo() noexcept {
    // If an exception is thrown, std::terminate is called
    // But noexcept is the modern replacement
}

void bar() {
    // No exception specification — any exception can propagate
    throw std::runtime_error("error");
}

int main() {
    try {
        bar();
    } catch (const std::runtime_error& e) {
        std::cerr << "Caught: " << e.what() << std::endl;
    }
    return 0;
}
```

## Using set_unexpected to Handle Legacy Code

```cpp
// CORRECT — set a custom unexpected handler for legacy code
#include <iostream>
#include <exception>

void custom_unexpected() {
    std::cerr << "Unexpected exception caught" << std::endl;
    // Re-throw to get std::bad_exception
    throw;
}

int main() {
    std::set_unexpected(custom_unexpected);

    // Legacy code that might throw unexpected exceptions
    // ... (code using dynamic exception specifications)

    return 0;
}
```

## Modern C++ Exception Handling

```cpp
// CORRECT — modern exception handling without dynamic specifications
#include <iostream>
#include <exception>
#include <string>

class ErrorCode {
    int code_;
    std::string message_;
public:
    ErrorCode(int code, std::string msg) : code_(code), message_(std::move(msg)) {}
    int code() const { return code_; }
    const std::string& message() const { return message_; }
};

void modern_function() {
    throw ErrorCode(42, "something went wrong");
}

int main() {
    try {
        modern_function();
    } catch (const ErrorCode& e) {
        std::cerr << "Error " << e.code() << ": " << e.message() << std::endl;
    } catch (...) {
        std::cerr << "Unknown exception" << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `noexcept` | When a function should not throw |
| Remove dynamic exception specifications | Always in modern C++ (C++17+) |
| Use `catch(...)` as fallback | When you need to catch any exception |
| Set custom unexpected handler | Only for legacy code migration |

## Related Errors

- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — logical precondition violations.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.
