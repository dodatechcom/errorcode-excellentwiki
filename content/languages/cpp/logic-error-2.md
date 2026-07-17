---
title: "[Solution] C++ std::logic_error — Program Logic Bug Fix"
description: "Fix C++ std::logic_error caused by violated preconditions, invalid arguments, and broken invariants. Learn validation and assertion patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::logic_error — Program Logic Bug Fix

A `std::logic_error` indicates a bug in the program — a violation of logical preconditions or invariants that should never occur if the code is correct. Unlike `std::runtime_error` (caused by external conditions), `std::logic_error` means the code itself is wrong. The standard library throws derived types like `std::invalid_argument`, `std::out_of_range`, and `std::domain_error`.

## Why std::logic_error Occurs

Common causes include passing invalid arguments to functions, violating class invariants, calling methods on objects in invalid states, and failing to check preconditions before operations.

## Wrong: No Precondition Validation

```cpp
// WRONG — no validation, undefined behavior
#include <vector>
#include <string>

std::string get_element(const std::vector<int>& vec, size_t index) {
    return "Element: " + std::to_string(vec[index]);  // UB if index >= size
}

int main() {
    std::vector<int> v = {1, 2, 3};
    std::string s = get_element(v, 10);  // undefined behavior
    return 0;
}
```

## Correct: Validate Preconditions and Throw

```cpp
// CORRECT — validate and throw std::logic_error
#include <vector>
#include <string>
#include <stdexcept>

std::string get_element(const std::vector<int>& vec, size_t index) {
    if (index >= vec.size()) {
        throw std::out_of_range("Index " + std::to_string(index) +
                                " out of range (size: " + std::to_string(vec.size()) + ")");
    }
    return "Element: " + std::to_string(vec[index]);
}

int main() {
    std::vector<int> v = {1, 2, 3};
    try {
        std::string s = get_element(v, 10);
    } catch (const std::out_of_range& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use assert() for Debug-Only Checks

```cpp
// CORRECT — assert for internal invariants
#include <cassert>
#include <vector>
#include <algorithm>
#include <iostream>

void process_sorted(const std::vector<int>& data) {
    assert(std::is_sorted(data.begin(), data.end()) && "Data must be sorted");
    assert(!data.empty() && "Data must not be empty");

    for (int val : data) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main() {
    process_sorted({1, 2, 3, 4, 5});
    return 0;
}
```

## Validate Class Invariants in Constructor

```cpp
// CORRECT — ensure valid state from construction
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

    void withdraw(double amount) {
        if (closed_) throw std::logic_error("Account is closed");
        if (amount <= 0) throw std::logic_error("Amount must be positive");
        if (amount > balance_) throw std::logic_error("Insufficient funds");
        balance_ -= amount;
    }

    double balance() const { return balance_; }
};
```

## Summary

| Fix | When to Use |
|---|---|
| Validate all function parameters | At the API boundary |
| Use `assert()` for internal invariants | During development |
| Throw `std::logic_error` subclasses | For public API precondition checks |
| Ensure valid state in constructors | Always — RAII principle |

## Related Errors

- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — specific type of logic error.
- [std::out_of_range]({{< relref "/languages/cpp/stdout-of-range" >}}) — index out of range.
- [std::length_error]({{< relref "/languages/cpp/length-error" >}}) — size limit exceeded.
