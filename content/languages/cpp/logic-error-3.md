---
title: "[Solution] C++ std::logic_error — Invariant Violation / Program Bug Fix"
description: "Fix C++ std::logic_error exceptions. Understand the difference between logic_error and runtime_error and how to detect these bugs early."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# [Solution] C++ std::logic_error — Invariant Violation / Program Bug Fix

A `std::logic_error` represents a program bug that could have been prevented by checking preconditions or invariants before the function was called. Unlike `std::runtime_error`, logic errors are theoretically detectable at compile time or through static analysis. They are defined in `<stdexcept>` and include subclasses like `std::invalid_argument`, `std::domain_error`, and `std::out_of_range`.

## Common Causes

- **Invalid function argument** — passing a value that violates the function's contract (e.g., negative size)
- **Violation of object invariant** — calling a method on an object in an invalid state
- **Broken precondition** — the caller did not ensure required conditions before calling
- **Implementation bug** — internal logic error that should never happen if the code is correct

## How to Fix

### Fix 1: Validate preconditions before calling functions

```cpp
#include <iostream>
#include <stdexcept>

double square_root(double x) {
    if (x < 0) {
        throw std::logic_error("square_root requires non-negative argument");
    }
    /* use x safely */
    return x;  // simplified
}

int main() {
    try {
        double result = square_root(-1.0);
        std::cout << result << std::endl;
    } catch (const std::logic_error& e) {
        std::cerr << "Logic error: " << e.what() << std::endl;
    }
    return 0;
}
```

### Fix 2: Maintain object invariants

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class BankAccount {
public:
    BankAccount(double balance) : balance_(balance) {
        if (balance < 0) {
            throw std::logic_error("Initial balance cannot be negative");
        }
    }

    void withdraw(double amount) {
        if (amount > balance_) {
            throw std::logic_error("Insufficient funds");
        }
        if (amount < 0) {
            throw std::logic_error("Withdrawal amount must be positive");
        }
        balance_ -= amount;
    }

    double balance() const { return balance_; }

private:
    double balance_;
};

int main() {
    try {
        BankAccount account(100.0);
        account.withdraw(200.0);  // throws logic_error
    } catch (const std::logic_error& e) {
        std::cerr << e.what() << std::endl;
    }
    return 0;
}
```

### Fix 3: Use assertions for debug-mode invariant checks

```cpp
#include <iostream>
#include <cassert>
#include <vector>

void process(const std::vector<int>& data) {
    assert(!data.empty() && "process requires non-empty data");
    std::cout << "First element: " << data[0] << std::endl;
}

int main() {
    std::vector<int> nums = {10, 20, 30};
    process(nums);  // OK
    // process({}); // assertion failure in debug mode
    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <stdexcept>

class Stack {
public:
    void push(int val) { data_[++top_] = val; }
    int pop() {
        if (top_ < 0) {
            throw std::logic_error("pop from empty stack");
        }
        return data_[top_--];
    }
private:
    int data_[100];
    int top_ = -1;
};

int main() {
    try {
        Stack s;
        s.pop();  // logic_error: pop from empty stack
    } catch (const std::logic_error& e) {
        std::cerr << e.what() << std::endl;
    }
    return 0;
}
```

## Related Errors

- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — subclass of logic_error for bad arguments
- [std::runtime_error]({{< relref "/languages/cpp/runtime-error12" >}}) — errors that occur at runtime, not detectable beforehand
- [std::out_of_range]({{< relref "/languages/cpp/out-of-range-3" >}}) — accessing an index outside valid bounds
