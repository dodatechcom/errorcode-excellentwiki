---
title: "[Solution] C++ std::logic_error — Logic Error Exception Example"
description: "Example of std::logic_error in C++. Learn to identify and fix logical precondition violations with practical examples."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 50
---

# [Solution] C++ std::logic_error — Logic Error Exception Example

A `std::logic_error` indicates a bug in the program's logic — the code violated a precondition or invariant that should never happen if the program is correct. Unlike `std::runtime_error` (external conditions), a `std::logic_error` means the developer made a mistake. Derived types include `std::invalid_argument`, `std::out_of_range`, `std::domain_error`, and `std::length_error`.

## Common Causes

- Passing invalid arguments to functions that require specific ranges or formats
- Violating class invariants by putting objects into invalid states
- Calling methods on objects that are not in the required state
- Failing to check preconditions before performing operations

## Example: Throwing std::logic_error

```cpp
#include <stdexcept>
#include <string>
#include <vector>

void process_data(const std::vector<int>& data) {
    if (data.empty()) {
        throw std::logic_error("process_data(): data must not be empty");
    }
    if (data.size() % 2 != 0) {
        throw std::logic_error("process_data(): data size must be even");
    }
    // Process paired elements...
}

int main() {
    try {
        std::vector<int> data = {1, 2, 3};  // odd size
        process_data(data);
    } catch (const std::logic_error& e) {
        std::cerr << "Logic error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## How to Fix: Validate Preconditions Early

```cpp
#include <stdexcept>
#include <string>

class BankAccount {
    double balance_;
public:
    explicit BankAccount(double initial) : balance_(initial) {
        if (initial < 0) {
            throw std::logic_error("Initial balance cannot be negative");
        }
    }

    void withdraw(double amount) {
        if (amount <= 0) {
            throw std::logic_error("Withdrawal amount must be positive");
        }
        if (amount > balance_) {
            throw std::logic_error("Insufficient funds");
        }
        balance_ -= amount;
    }

    double balance() const { return balance_; }
};

int main() {
    try {
        BankAccount acc(100.0);
        acc.withdraw(200.0);  // throws logic_error
    } catch (const std::logic_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Using assert for Debug-Only Checks

```cpp
#include <cassert>
#include <vector>
#include <algorithm>

// assert() is removed in release builds — use for internal invariants only
void process_sorted(const std::vector<int>& data) {
    assert(std::is_sorted(data.begin(), data.end()) && "Data must be sorted");
    assert(!data.empty() && "Data must not be empty");

    for (int val : data) {
        std::cout << val << " ";
    }
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

## Summary

| Fix | When to Use |
|---|---|
| Validate all preconditions at function entry | Public API boundaries |
| Use `assert()` during development | Internal invariants that must never be false |
| Create custom exception subclasses | When domain-specific errors need extra context |
| Use RAII to enforce valid object states | Always |

## Related Errors

- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — specific type of logic error for invalid parameters.
- [std::length_error]({{< relref "/languages/cpp/length-error" >}}) — container size limit exceeded.
- [std::out_of_range]({{< relref "/languages/cpp/out-of-range-example" >}}) — index out of bounds.
