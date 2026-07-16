---
title: "[Solution] C++ std::logic_error — Logic Error Exception Fix"
description: "Fix C++ std::logic_error by validating preconditions, using assert(), checking function contracts, and adding runtime parameter validation."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["logic-error", "exception", "precondition", "assert"]
weight: 55
---

# [Solution] C++ std::logic_error — Logic Error Exception Fix

A `std::logic_error` is a C++ standard library exception indicating a violation of logical preconditions or invariants in the program. Unlike errors caused by external conditions (network, memory), a `std::logic_error` means there is a bug in the code itself — the program received invalid arguments or is in an impossible state. The standard library throws derived types like `std::invalid_argument`, `std::out_of_range`, and `std::domain_error`, all of which inherit from `std::logic_error`.

## Why std::logic_error Occurs

Common causes include passing invalid arguments to functions, violating class invariants, using an object in an invalid state, or failing to check preconditions before operations.

## Wrong: No precondition validation

```cpp
#include <stdexcept>
#include <string>
#include <vector>

double divide(double a, double b) {
    // No check — if b is 0, behavior is undefined (not even std::logic_error)
    return a / b;
}

std::string get_element(const std::vector<int>& vec, size_t index) {
    // No bounds check — undefined behavior if index >= vec.size()
    return "Element: " + std::to_string(vec[index]);
}
```

## Correct: Validate preconditions and throw std::logic_error

```cpp
#include <stdexcept>
#include <string>
#include <vector>

double divide(double a, double b) {
    if (b == 0.0) {
        throw std::logic_error("Division by zero is not allowed");
    }
    return a / b;
}

std::string get_element(const std::vector<int>& vec, size_t index) {
    if (index >= vec.size()) {
        throw std::out_of_range("Index " + std::to_string(index) +
                                " out of range (size: " + std::to_string(vec.size()) + ")");
    }
    return "Element: " + std::to_string(vec[index]);
}

// Usage with try-catch
int main() {
    try {
        double result = divide(10, 0);
    } catch (const std::logic_error& e) {
        std::cerr << "Logic error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Using assert() for Debug-Only Checks

```cpp
#include <cassert>
#include <vector>
#include <algorithm>

// assert() is removed in release builds (-DNDEBUG), use only for internal invariants
void process_sorted(const std::vector<int>& data) {
    assert(std::is_sorted(data.begin(), data.end()) && "Data must be sorted");
    assert(!data.empty() && "Data must not be empty");

    // Process the sorted data...
    for (int val : data) {
        std::cout << val << " ";
    }
}
```

## Validating Class Invariants

```cpp
#include <stdexcept>
#include <string>

class BankAccount {
    double balance_;
    bool closed_ = false;

public:
    explicit BankAccount(double initial) : balance_(initial) {
        if (initial < 0) {
            throw std::logic_error("Initial balance cannot be negative");
        }
    }

    void deposit(double amount) {
        if (closed_) {
            throw std::logic_error("Cannot deposit to a closed account");
        }
        if (amount <= 0) {
            throw std::logic_error("Deposit amount must be positive");
        }
        balance_ += amount;
    }

    void withdraw(double amount) {
        if (closed_) {
            throw std::logic_error("Cannot withdraw from a closed account");
        }
        if (amount <= 0) {
            throw std::logic_error("Withdrawal amount must be positive");
        }
        if (amount > balance_) {
            throw std::logic_error("Insufficient funds");
        }
        balance_ -= amount;
    }

    void close() {
        if (closed_) {
            throw std::logic_error("Account is already closed");
        }
        closed_ = true;
    }

    double balance() const { return balance_; }
};
```

## Using Design by Contract Pattern

```cpp
#include <stdexcept>
#include <functional>
#include <iostream>

template <typename T>
class Contract {
public:
    static void requires(T condition, const std::string& message) {
        if (!condition) {
            throw std::logic_error("Precondition violated: " + message);
        }
    }

    static void ensures(T condition, const std::string& message) {
        if (!condition) {
            throw std::logic_error("Postcondition violated: " + message);
        }
    }
};

// Usage
int factorial(int n) {
    Contract<int>::requires(n >= 0, "factorial requires non-negative input");

    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }

    Contract<int>::ensures(result >= 1 || n == 0, "factorial result must be >= 1");
    return result;
}
```

## Exception Hierarchy

| Exception | Meaning | Example |
|---|---|---|
| `std::logic_error` | Logical precondition violated | Generic logic error |
| `std::invalid_argument` | Invalid argument passed to function | `stoi("abc")` |
| `std::out_of_range` | Index or value out of range | Vector access beyond size |
| `std::domain_error` | Mathematical domain error | `sqrt(-1)` |
| `std::length_error` | Exceeds implementation limit | Vector resize too large |
| `std::overflow_error` | Arithmetic overflow | Integer overflow |

## Prevention Tips

- Use `assert()` during development for internal invariants that must never be false.
- Use `std::logic_error` (or derived types) for public API precondition checks that survive in release builds.
- Validate all function parameters at the boundary between subsystems.
- Write unit tests that specifically exercise invalid inputs to verify error handling.
- Use RAII and constructors to ensure objects are always in valid states.

## Related Errors

- [std::invalid_argument](invalid-argument) — specific type of logic error for invalid parameters.
- [std::length_error](length-error) — container size limit exceeded.
- [std::bad_alloc](std-bad-alloc) — memory allocation failure (not a logic error).
