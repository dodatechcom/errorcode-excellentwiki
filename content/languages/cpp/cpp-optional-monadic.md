---
title: "[Solution] C++ Optional Monadic Error — How to Fix"
description: "Fix C++23 std::optional monadic operation errors including and_then chain failures, transform type mismatches, and empty value handling."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Optional Monadic Error — How to Fix

C++23 adds monadic operations (`and_then`, `transform`, `or_else`) to `std::optional`, enabling functional-style chaining. Type mismatches and incorrect usage produce compilation errors.

## Why It Happens

Monadic optional errors occur when `and_then` returns a non-optional type, when `transform` returns a type that can't be wrapped in optional, when chaining operations with incompatible intermediate types, or when using these operations with move-only types incorrectly.

## Common Error Messages

1. `error: no matching function for call to 'std::optional::and_then'`
2. `error: cannot convert 'int' to 'std::optional<int>'`
3. `error: no viable conversion from 'optional<string>' to 'optional<int>'`
4. `error: call to deleted constructor of 'std::optional<MoveOnly>'`

## How to Fix It

### Fix 1: Ensure and_then Returns Optional

```cpp
#include <optional>
#include <string>
#include <iostream>

std::optional<int> parse(const std::string& s) {
    try {
        return std::stoi(s);
    } catch (...) {
        return std::nullopt;
    }
}

// CORRECT — and_then lambda must return std::optional
auto result = parse("42")
    .and_then([](int v) -> std::optional<std::string> {
        if (v > 0) return std::to_string(v);
        return std::nullopt;
    });
```

### Fix 2: Use transform for Value Mapping

```cpp
#include <optional>
#include <iostream>

std::optional<int> find_value() { return 42; }

// transform wraps the result in optional automatically
auto result = find_value()
    .transform([](int v) { return v * 2; })
    .transform([](int v) { return std::to_string(v); });

if (result) {
    std::cout << *result << "\n";  // "84"
}
```

### Fix 3: Handle Empty Case with or_else

```cpp
#include <optional>
#include <iostream>

std::optional<int> maybe_value() { return std::nullopt; }

auto result = maybe_value()
    .or_else([]() -> std::optional<int> {
        std::cout << "Value missing, using default\n";
        return 0;
    })
    .transform([](int v) { return v + 10; });

std::cout << result.value_or(-1) << "\n";  // 10
```

## Common Scenarios

- **Nested optionals**: `and_then` flattens nested optionals; `transform` wraps them.
- **Move-only types**: Monadic operations on `optional<MoveOnly>` may require explicit moves.
- **Void transform**: Use `transform` with `void` return type carefully — prefer `and_then` for side effects.

## Prevent It

1. `and_then` lambdas must always return `std::optional<U>` — not raw values.
2. `transform` lambdas can return any type — the result is automatically wrapped in `std::optional`.
3. Use `value_or()` for safe default values instead of dereferencing potentially empty optionals.

## Related Errors

- [Optional bad access]({{< relref "/languages/cpp/bad-optional-access" >}}) — accessing empty optional.
- [std::expected error]({{< relref "/languages/cpp/cpp-expected-error" >}}) — similar monadic pattern.
- [Template deduction error]({{< relref "/languages/cpp/template-error" >}}) — type deduction failures in chains.
