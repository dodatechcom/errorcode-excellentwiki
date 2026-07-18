---
title: "[Solution] C++ stdexcept Error — How to Fix"
description: "Fix C++ stdexcept errors including unhandled standard exceptions, missing exception specifications, and improper catch ordering in exception hierarchies."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ stdexcept Error — How to Fix

Standard library exceptions (`std::runtime_error`, `std::logic_error`, etc.) form the backbone of C++ error handling, but improper catch ordering, missing handlers, and incorrect exception creation lead to uncaught exceptions and program termination.

## Why It Happens

Stdexcept errors occur when catch blocks are ordered incorrectly (catching base before derived), when exceptions are thrown without proper constructors, when standard exceptions aren't caught by reference allowing slicing, or when custom exceptions don't inherit from the appropriate stdexcept base class.

## Common Error Messages

1. `terminate called after throwing an instance of 'std::out_of_range'`
2. `error: catching by value slices exception object`
3. `warning: exception of type 'Derived' will be caught by earlier handler`
4. `error: 'what' function overrides not virtual`

## How to Fix It

### Fix 1: Catch Exceptions by Reference

```cpp
#include <stdexcept>
#include <iostream>

void risky_function() {
    throw std::runtime_error("something went wrong");
}

int main() {
    try {
        risky_function();
    }
    // WRONG — catches by value, slices derived exceptions
    // catch (std::exception e) { std::cout << e.what(); }

    // CORRECT — catch by const reference
    catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << "\n";
    }
    return 0;
}
```

### Fix 2: Order Catch Blocks from Most to Least Derived

```cpp
#include <stdexcept>
#include <iostream>

void process(int value) {
    if (value < 0) throw std::domain_error("negative value");
    if (value > 100) throw std::range_error("value too large");
    throw std::runtime_error("unknown error");
}

int main() {
    try {
        process(200);
    }
    // CORRECT — derived types first
    catch (const std::range_error& e) {
        std::cout << "Range: " << e.what() << "\n";
    }
    catch (const std::domain_error& e) {
        std::cout << "Domain: " << e.what() << "\n";
    }
    catch (const std::runtime_error& e) {
        std::cout << "Runtime: " << e.what() << "\n";
    }
    catch (const std::exception& e) {
        std::cout << "Other: " << e.what() << "\n";
    }
    return 0;
}
```

### Fix 3: Create Custom Exceptions Properly

```cpp
#include <stdexcept>
#include <string>
#include <iostream>

class ValidationError : public std::logic_error {
    std::string field_;
public:
    ValidationError(const std::string& field, const std::string& msg)
        : std::logic_error(msg), field_(field) {}

    const std::string& field() const { return field_; }
};

void validate(int age) {
    if (age < 0) throw ValidationError("age", "Age cannot be negative");
    if (age > 150) throw ValidationError("age", "Age unrealistic");
}

int main() {
    try {
        validate(-5);
    } catch (const ValidationError& e) {
        std::cout << "Field: " << e.field() << ", Error: " << e.what() << "\n";
    }
    return 0;
}
```

### Fix 4: Use noexcept Correctly with Exception Hierarchies

```cpp
#include <stdexcept>
#include <iostream>

class SafeClass {
public:
    // Destructor — must not throw
    ~SafeClass() noexcept {}

    // Move constructor — may throw if allocation fails
    SafeClass(SafeClass&& other) noexcept(false) = default;

    void process() {
        throw std::runtime_error("error in process");
    }
};

int main() {
    try {
        SafeClass sc;
        sc.process();
    } catch (const std::exception& e) {
        std::cout << e.what() << "\n";
    }
    return 0;
}
```

## Common Scenarios

- **Catch by value**: Slicing destroys derived exception information — always catch by `const&`.
- **Wrong order**: Catching `std::exception` before `std::runtime_error` means the derived handler never runs.
- **Missing what()**: Custom exceptions that don't properly pass messages to base constructors show empty error text.

## Prevent It

1. Always catch exceptions by `const std::exception&` to prevent slicing.
2. Order catch blocks from most derived to least derived types.
3. Inherit custom exceptions from `std::runtime_error` or `std::logic_error` and pass messages to the base constructor.

## Related Errors

- [System error]({{< relref "/languages/cpp/system-error-system" >}}) — system call failures.
- [Logic error]({{< relref "/languages/cpp/logic-error" >}}) — program logic issues.
- [Runtime error]({{< relref "/languages/cpp/runtimeerror" >}}) — runtime failures.
