---
title: "[Solution] C++ std::invalid_argument — Invalid Argument Exception Example"
description: "Example of std::invalid_argument in C++. Learn to validate parameters and handle invalid function arguments properly."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["invalid-argument", "exception", "parameter-validation", "stoi"]
weight: 50
---

# [Solution] C++ std::invalid_argument — Invalid Argument Exception Example

A `std::invalid_argument` exception is thrown when a function receives an argument that is not valid for its expected type or range. This is a subclass of `std::logic_error`, meaning the bug is in the calling code. Common triggers include passing non-numeric strings to `std::stoi()`, creating invalid dates, or passing null pointers where objects are expected.

## Common Causes

- Passing non-numeric strings to `std::stoi()` or `std::stod()`
- Constructing objects with invalid parameters
- Passing enum values that are not in the valid range
- Using invalid bitset or regex patterns

## Example: Throwing std::invalid_argument

```cpp
#include <stdexcept>
#include <string>
#include <cctype>
#include <algorithm>

int parse_age(const std::string& input) {
    if (input.empty()) {
        throw std::invalid_argument("Age string is empty");
    }
    if (!std::all_of(input.begin(), input.end(), [](char c) {
        return std::isdigit(c) || c == '-';
    })) {
        throw std::invalid_argument("Age contains non-numeric characters: " + input);
    }
    int age = std::stoi(input);
    if (age < 0 || age > 150) {
        throw std::invalid_argument("Age out of reasonable range: " + input);
    }
    return age;
}

int main() {
    try {
        int age = parse_age("abc");
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
    }
    return 0;
}
```

## How to Fix: Use Safe Conversion Utilities

```cpp
#include <string>
#include <stdexcept>
#include <optional>
#include <charconv>

std::optional<int> try_parse_int(const std::string& str) {
    int value = 0;
    auto [ptr, ec] = std::from_chars(str.data(), str.data() + str.size(), value);
    if (ec == std::errc{}) {
        return value;
    }
    return std::nullopt;
}

int main() {
    auto age = try_parse_int("42");
    if (age) {
        std::cout << "Age: " << *age << std::endl;
    }

    auto bad = try_parse_int("abc");
    if (!bad) {
        std::cerr << "Invalid input" << std::endl;
    }
    return 0;
}
```

## Constructor Parameter Validation

```cpp
#include <stdexcept>
#include <string>

class EmailAddress {
    std::string value_;
public:
    explicit EmailAddress(const std::string& email) : value_(email) {
        if (email.empty()) {
            throw std::invalid_argument("Email address cannot be empty");
        }
        if (email.find('@') == std::string::npos) {
            throw std::invalid_argument("Invalid email address: " + email);
        }
    }
    const std::string& value() const { return value_; }
};

int main() {
    try {
        EmailAddress email("invalid");
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Validate function parameters at API boundaries | Always for public functions |
| Use `std::from_chars` for safe numeric parsing | When converting strings to numbers |
| Create type-safe wrappers | When types have validation constraints |
| Return `std::optional` for expected failures | When exceptions are too expensive |

## Related Errors

- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — base class for logic errors.
- [std::length_error]({{< relref "/languages/cpp/length-error" >}}) — container size limit exceeded.
- [std::out_of_range]({{< relref "/languages/cpp/out-of-range-example" >}}) — index out of bounds.
