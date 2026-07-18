---
title: "[Solution] C++ Contract Error — How to Fix"
description: "Fix C++ contract errors including precondition/postcondition violations, assertion failures, and std::expected contract handling issues in C++26."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Contract Error — How to Fix

C++26 contracts provide built-in precondition and postcondition checking, but incorrect contract definitions, semantic choices (abort vs. ignore), and violation handler configurations lead to unexpected program termination or silent bugs.

## Why It Happens

Contract errors occur when preconditions are violated at runtime causing program termination, when contract assertions interact poorly with exception handling, when semantic modes (set to `ignore`, `enforce`, or `quick`) are misconfigured, or when postconditions reference modified state after execution.

## Common Error Messages

1. `contract violation: precondition 'value > 0' failed at function entry`
2. `error: postcondition violation — return value constraint failed`
3. `error: contract assertion failed — assert(false)`
4. `warning: side effects in contract expression`

## How to Fix It

### Fix 1: Use Assertions for Invariant Checking

```cpp
#include <cassert>
#include <iostream>

int divide(int a, int b) {
    // CORRECT — assert precondition before use
    assert(b != 0 && "Division by zero");
    return a / b;
}

int main() {
    std::cout << divide(10, 2) << "\n";
    // divide(10, 0);  // assertion failure in debug
    return 0;
}
```

### Fix 2: Validate Parameters Explicitly

```cpp
#include <stdexcept>
#include <iostream>

// CORRECT — explicit precondition check with exception
double safe_sqrt(double value) {
    if (value < 0) {
        throw std::domain_error("sqrt of negative number");
    }
    // approximate sqrt
    double x = value;
    for (int i = 0; i < 10; i++) {
        x = (x + value / x) / 2.0;
    }
    return x;
}

int main() {
    try {
        std::cout << safe_sqrt(25.0) << "\n";
        std::cout << safe_sqrt(-1.0) << "\n";
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << "\n";
    }
    return 0;
}
```

### Fix 3: Use std::expected for Contract-like Returns

```cpp
#include <expected>
#include <iostream>
#include <string>

enum class Error { division_by_zero, overflow };

std::expected<double, Error> divide(int a, int b) {
    if (b == 0) return std::unexpected(Error::division_by_zero);
    if (a == INT32_MIN && b == -1) return std::unexpected(Error::overflow);
    return static_cast<double>(a) / b;
}

int main() {
    auto result1 = divide(10, 2);
    auto result2 = divide(10, 0);

    if (result1) std::cout << "Result: " << *result1 << "\n";
    if (!result2) std::cout << "Error occurred\n";

    return 0;
}
```

### Fix 4: Implement Postcondition Checking

```cpp
#include <iostream>
#include <stdexcept>

class PositiveInt {
    int value_;
public:
    PositiveInt(int v) : value_(v) {
        // POSTCONDITION — value must be positive after construction
        if (v <= 0) throw std::invalid_argument("must be positive");
    }

    int value() const { return value_; }

    PositiveInt& operator++() {
        ++value_;
        // POSTCONDITION — value still positive after increment
        if (value_ <= 0) throw std::overflow_error("value overflowed");
        return *this;
    }
};

int main() {
    PositiveInt p(5);
    ++p;
    std::cout << p.value() << "\n";  // 6
    return 0;
}
```

## Common Scenarios

- **Division by zero**: Preconditions must check divisors before arithmetic operations.
- **Null pointers**: Function contracts should validate pointer parameters aren't null.
- **Range violations**: Array indices and container positions need bounds-checking contracts.

## Prevent It

1. Use `assert()` for internal invariants that should never fail in correct code.
2. Use explicit checks with exceptions or `std::expected` for public API preconditions.
3. Document contract requirements in comments when the language doesn't provide built-in contracts.

## Related Errors

- [Unreachable error]({{< relref "/languages/cpp/cpp-unreachable-error" >}}) — dead code assumptions.
- [Logic error]({{< relref "/languages/cpp/logic-error" >}}) — program logic issues.
- [Invalid argument]({{< relref "/languages/cpp/invalid-argument" >}}) — bad function parameters.
