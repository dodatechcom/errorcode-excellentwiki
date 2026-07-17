---
title: "[Solution] C++ std::expected Error — Expected Error Fix"
description: "Fix C++ std::expected errors including accessing value without checking, unhandled errors, and misuse patterns. Learn expected usage."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::expected Error — Expected Error Fix

`std::expected<T, E>` (C++23) represents a value that is either a successful result or an error. Errors occur when accessing `value()` without checking, using `error()` on a value-holding expected, or not handling the error case.

## Why std::expected Errors Occur

Common causes include calling `value()` when the expected holds an error (throws `std::bad_expected_access`), calling `error()` when the expected holds a value, not checking `has_value()` before access, and ignoring errors from operations that return expected.

## Wrong: Accessing value() When Holding Error

```cpp
// WRONG — throws std::bad_expected_access
#include <expected>
#include <iostream>
#include <string>

std::expected<int, std::string> parse_int(const std::string& s) {
    try {
        return std::stoi(s);
    } catch (...) {
        return std::unexpected("Parse failed");
    }
}

int main() {
    auto result = parse_int("abc");
    int val = result.value();  // throws — holds error
    std::cout << val << std::endl;
    return 0;
}
```

## Correct: Check has_value() Before Access

```cpp
// CORRECT — check before accessing
#include <expected>
#include <iostream>
#include <string>

std::expected<int, std::string> parse_int(const std::string& s) {
    try {
        return std::stoi(s);
    } catch (...) {
        return std::unexpected("Parse failed");
    }
}

int main() {
    auto result = parse_int("abc");

    if (result.has_value()) {
        std::cout << "Value: " << result.value() << std::endl;
    } else {
        std::cerr << "Error: " << result.error() << std::endl;
    }
    return 0;
}
```

## Use value_or for Defaults

```cpp
// CORRECT — provide default with value_or
#include <expected>
#include <iostream>
#include <string>

std::expected<int, std::string> get_config(const std::string& key) {
    if (key == "timeout") return 30;
    return std::unexpected("Key not found");
}

int main() {
    int timeout = get_config("timeout").value_or(60);
    int retries = get_config("retries").value_or(3);

    std::cout << "Timeout: " << timeout << std::endl;
    std::cout << "Retries: " << retries << std::endl;
    return 0;
}
```

## Chain Operations With transform

```cpp
// CORRECT — use transform for monadic operations
#include <expected>
#include <iostream>
#include <string>
#include <cmath>

std::expected<double, std::string> parse_double(const std::string& s) {
    try {
        return std::stod(s);
    } catch (...) {
        return std::unexpected("Not a number");
    }
}

int main() {
    auto result = parse_double("4.0")
        .transform([](double v) { return std::sqrt(v); });

    if (result) {
        std::cout << "sqrt(4.0) = " << *result << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check `has_value()` before `value()` | When expected might hold error |
| Use `value_or(default)` | When a fallback is acceptable |
| Use `transform` for chained operations | When composing value-producing operations |
| Use `and_then` for monadic binding | When operations return expected |

## Related Errors

- [std::optional error]({{< relref "/languages/cpp/optional-error" >}}) — optional access errors.
- [std::variant error]({{< relref "/languages/cpp/variant-error" >}}) — variant access errors.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
