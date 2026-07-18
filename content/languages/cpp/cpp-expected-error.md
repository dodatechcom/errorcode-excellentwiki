---
title: "[Solution] C++ Expected Error — How to Fix"
description: "Fix C++ std::expected errors including type mismatch, unexpected value access, and monadic operation chain failures."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time", "runtime"]
weight: 5
comments: true
---

# [Solution] C++ Expected Error — How to Fix

C++23 `std::expected<T, E>` represents a value or an error, providing a type-safe alternative to exceptions. Misuse leads to access violations, type mismatches, and monadic chain failures.

## Why It Happens

Expected errors occur when accessing the value without checking for an error first, when the error type doesn't match during extraction, when monadic operations return incompatible types, or when moving from an expected that holds an error.

## Common Error Messages

1. `error: std::bad_expected_access: value not available`
2. `error: no member named 'value' in 'std::expected<E, E>'`
3. `error: cannot convert between expected types`
4. `error: use of moved-from expected`

## How to Fix It

### Fix 1: Always Check Before Accessing Value

```cpp
#include <expected>
#include <string>
#include <iostream>

std::expected<int, std::string> parse_int(const std::string& s) {
    try {
        return std::stoi(s);
    } catch (...) {
        return std::unexpected("parse failed");
    }
}

// WRONG — may throw bad_expected_access
// int val = parse_int("abc").value();

// CORRECT — check first
auto result = parse_int("abc");
if (result) {
    std::cout << "Value: " << *result << "\n";
} else {
    std::cout << "Error: " << result.error() << "\n";
}
```

### Fix 2: Use Monadic Operations Safely

```cpp
#include <expected>
#include <string>

std::expected<double, std::string> divide(double a, double b) {
    if (b == 0) return std::unexpected("division by zero");
    return a / b;
}

std::expected<double, std::string> process(double a, double b) {
    return divide(a, b)
        .transform([](double v) { return v * 2.0; })
        .or_else([](std::unexpected<std::string> e) {
            return std::expected<double, std::string>(std::unexpected(e.error()));
        });
}
```

### Fix 3: Handle Unexpected Values in Chains

```cpp
#include <expected>
#include <string>

std::expected<int, std::string> step1() { return 10; }
std::expected<int, std::string> step2(int v) {
    if (v < 0) return std::unexpected("negative");
    return v * 2;
}

// Each step can fail — use and_then
auto result = step1()
    .and_then(step2)
    .transform([](int v) { return std::to_string(v); });

if (result) {
    // result holds the string
}
```

## Common Scenarios

- **Error type conversion**: Unexpected types must match or be implicitly convertible.
- **Move semantics**: `std::expected` is move-aware; moving invalidates the source.
- **Void expected**: `std::expected<void, E>` is useful for operations that either succeed or fail.

## Prevent It

1. Always use `has_value()`, `operator bool()`, or `value_or()` instead of raw `value()`.
2. Prefer monadic chaining (`and_then`, `transform`, `or_else`) over manual branching.
3. Use `std::expected<void, E>` for operations that don't produce a meaningful value.

## Related Errors

- [std::bad_optional_access]({{< relref "/languages/cpp/bad-optional-access" >}}) — empty optional access.
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — type mismatch in std::any.
- [Variant visit error]({{< relref "/languages/cpp/cpp-variant-visit-error" >}}) — wrong variant type.
