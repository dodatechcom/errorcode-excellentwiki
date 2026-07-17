---
title: "[Solution] C++ std::invalid_argument — Invalid Function Argument Fix"
description: "Fix C++ std::invalid_argument when functions receive invalid parameters. Learn input validation and parameter checking patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::invalid_argument — Invalid Function Argument Fix

A `std::invalid_argument` is thrown when a function receives an argument that is invalid for the operation. This includes passing a non-numeric string to `std::stoi`, passing a negative value where only positive is allowed, and providing null pointers where non-null is expected. It inherits from `std::logic_error`.

## Why std::invalid_argument Occurs

Common causes include calling `std::stoi` or `std::stod` with non-numeric strings, passing invalid bit patterns to `std::bitset` constructors, constructing iterators with invalid ranges, and providing null pointers to functions that require valid objects.

## Wrong: Not Validating Function Arguments

```cpp
// WRONG — may throw std::invalid_argument
#include <string>
#include <iostream>

int main() {
    int val = std::stoi("not_a_number");  // throws std::invalid_argument
    std::cout << val << std::endl;
    return 0;
}
```

## Correct: Validate Before Calling Functions

```cpp
// CORRECT — validate input before conversion
#include <string>
#include <iostream>
#include <stdexcept>

int safe_stoi(const std::string& str) {
    try {
        size_t pos;
        int val = std::stoi(str, &pos);
        if (pos != str.size()) {
            throw std::invalid_argument("Trailing characters in: " + str);
        }
        return val;
    } catch (const std::invalid_argument&) {
        throw std::invalid_argument("Cannot convert '" + str + "' to integer");
    }
}

int main() {
    try {
        int val = safe_stoi("abc");
        std::cout << val << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
    }
    return 0;
}
```

## Validate Numeric Ranges

```cpp
// CORRECT — validate numeric arguments
#include <stdexcept>
#include <string>
#include <iostream>

void set_port(int port) {
    if (port < 1 || port > 65535) {
        throw std::invalid_argument("Port must be between 1 and 65535 (got " +
                                     std::to_string(port) + ")");
    }
    std::cout << "Port set to: " << port << std::endl;
}

int main() {
    try {
        set_port(70000);
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Validate Non-Empty Arguments

```cpp
// CORRECT — check for empty or null arguments
#include <stdexcept>
#include <string>
#include <iostream>

class Username {
    std::string name_;
public:
    explicit Username(const std::string& name) : name_(name) {
        if (name.empty()) {
            throw std::invalid_argument("Username must not be empty");
        }
        if (name.size() < 3) {
            throw std::invalid_argument("Username must be at least 3 characters");
        }
    }

    const std::string& name() const { return name_; }
};

int main() {
    try {
        Username u("ab");
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Validate all function parameters | At the API boundary |
| Throw `std::invalid_argument` | For invalid parameter values |
| Use wrapper functions | When converting external input |
| Check for empty containers/strings | When emptiness indicates an error |

## Related Errors

- [std::out_of_range]({{< relref "/languages/cpp/stdout-of-range" >}}) — value outside valid range.
- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — general logic errors.
- [std::domain_error](/languages/cpp/domain-error-example/) — mathematical domain errors.
