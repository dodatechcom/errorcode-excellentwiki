---
title: "[Solution] C++ std::invalid_argument — Invalid Argument Exception Fix"
description: "Fix C++ std::invalid_argument by validating parameters, using proper constructors, range checks, and safe type conversions before passing values."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["invalid-argument", "exception", "parameter-validation", "stoi"]
weight: 58
---

# [Solution] C++ std::invalid_argument — Invalid Argument Exception Fix

A `std::invalid_argument` exception is thrown when a function receives an argument that is not valid for its expected type or range. This is a subclass of `std::logic_error`, meaning the bug is in the calling code. Common triggers include passing non-numeric strings to `std::stoi()`, creating invalid dates, or passing null pointers where objects are expected.

## Common Causes

```cpp
#include <stdexcept>
#include <string>
#include <vector>

// Cause 1: std::stoi with non-numeric string
int num = std::stoi("hello");  // std::invalid_argument

// Cause 2: std::stod with invalid string
double val = std::stod("not-a-number");  // std::invalid_argument

// Cause 3: Constructing an invalid date
// (hypothetical date class that throws on invalid input)

// Cause 4: Null pointer where reference is expected
void process(const std::string& str);
const char* ptr = nullptr;
process(ptr);  // undefined behavior (not std::invalid_argument, but still wrong)

// Cause 5: Invalid bitset constructor
std::bitset<8> bits("invalid_binary_string");  // std::invalid_argument
```

## Solutions

### Fix 1: Validate strings before conversion

```cpp
#include <string>
#include <stdexcept>
#include <cctype>
#include <algorithm>

// Wrong — no validation
int parse_age(const std::string& input) {
    return std::stoi(input);  // throws if input is "abc"
}

// Correct — validate before converting
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
```

### Fix 2: Safe conversion utilities

```cpp
#include <string>
#include <stdexcept>
#include <optional>
#include <charconv>

// Safe string-to-int without exceptions
std::optional<int> try_parse_int(const std::string& str) {
    int value = 0;
    auto [ptr, ec] = std::from_chars(str.data(), str.data() + str.size(), value);
    if (ec == std::errc{}) {
        return value;
    }
    return std::nullopt;
}

// Safe string-to-double
std::optional<double> try_parse_double(const std::string& str) {
    double value = 0.0;
    auto [ptr, ec] = std::from_chars(str.data(), str.data() + str.size(), value);
    if (ec == std::errc{}) {
        return value;
    }
    return std::nullopt;
}

// Usage
void process_input(const std::string& input) {
    auto age = try_parse_int(input);
    if (!age) {
        throw std::invalid_argument("Invalid age: " + input);
    }
    std::cout << "Age: " << *age << std::endl;
}
```

### Fix 3: Validate enum and type conversions

```cpp
#include <stdexcept>
#include <string>

enum class Color { Red, Green, Blue };

Color string_to_color(const std::string& str) {
    if (str == "red")   return Color::Red;
    if (str == "green") return Color::Green;
    if (str == "blue")  return Color::Blue;
    throw std::invalid_argument("Unknown color: " + str);
}

// Usage
int main() {
    try {
        Color c = string_to_color("purple");
    } catch (const std::invalid_argument& e) {
        std::cerr << e.what() << std::endl;  // "Unknown color: purple"
    }
    return 0;
}
```

### Fix 4: Constructor parameter validation

```cpp
#include <stdexcept>
#include <string>

class Rectangle {
    double width_;
    double height_;

public:
    Rectangle(double width, double height) : width_(width), height_(height) {
        if (width <= 0) {
            throw std::invalid_argument("Width must be positive, got: " + std::to_string(width));
        }
        if (height <= 0) {
            throw std::invalid_argument("Height must be positive, got: " + std::to_string(height));
        }
    }

    double area() const { return width_ * height_; }
};

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
        if (email.find('.') == std::string::npos) {
            throw std::invalid_argument("Email address missing domain: " + email);
        }
    }

    const std::string& value() const { return value_; }
};
```

### Fix 5: Validate function arguments at API boundaries

```cpp
#include <stdexcept>
#include <vector>
#include <algorithm>

// Public API — must validate all inputs
template <typename T>
T clamp_value(T value, T min_val, T max_val) {
    if (min_val > max_val) {
        throw std::invalid_argument("min must be <= max");
    }
    return std::max(min_val, std::min(max_val, value));
}

// Public API — validate vector operations
int get_middle_element(const std::vector<int>& vec) {
    if (vec.empty()) {
        throw std::invalid_argument("Cannot get middle element of empty vector");
    }
    return vec[vec.size() / 2];
}

// Usage
int main() {
    try {
        int clamped = clamp_value(150, 0, 100);  // returns 100
        int mid = get_middle_element({1, 2, 3, 4, 5});  // returns 3
        int bad = clamp_value(50, 100, 0);  // throws std::invalid_argument
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
    }
    return 0;
}
```

## Prevention Tips

- Always validate function parameters at public API boundaries.
- Use `std::from_chars` for safe numeric parsing — it does not throw on invalid input.
- Create type-safe wrappers (like `EmailAddress`, `Color`) that validate on construction.
- Prefer returning `std::optional` over throwing for expected failure cases.
- Document precondition assumptions with comments or `Expects()` annotations (C++20 Contracts proposal).

## Related Errors

- [std::logic_error](logic-error) — base class for logic errors.
- [std::length_error](length-error) — container size limit exceeded.
- [std::out_of_range](#) — index out of bounds (derived from std::logic_error).
