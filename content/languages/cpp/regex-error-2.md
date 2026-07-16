---
title: "[Solution] C++ std::regex_error — Regular Expression Compilation Fix"
description: "Fix C++ std::regex_error when regex patterns are invalid. Handle syntax errors, escape sequences, and regex compilation failures."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["regex-error", "regex", "pattern-matching", "exception"]
weight: 5
---

# [Solution] C++ std::regex_error — Regular Expression Compilation Fix

A `std::regex_error` is thrown when a regular expression pattern is malformed and cannot be compiled by the `std::regex` constructor. This exception includes an error code that indicates the type of syntax error in the pattern. It inherits from `std::runtime_error`.

## Why std::regex_error Occurs

Common causes include unbalanced parentheses or brackets in the pattern, invalid escape sequences (e.g., `\q`), quantifiers without a preceding element (e.g., `*hello`), and unsupported regex syntax for the selected grammar flag.

## Wrong: Constructing Regex With Invalid Pattern

```cpp
// WRONG — throws std::regex_error
#include <regex>
#include <iostream>

int main() {
    std::regex bad("[a-z");  // unbalanced bracket
    return 0;
}
```

## Correct: Validate Regex Pattern

```cpp
// CORRECT — catch regex_error for invalid patterns
#include <regex>
#include <iostream>

int main() {
    try {
        std::regex pattern("[a-z]+");
        std::cout << "Pattern compiled successfully" << std::endl;
    } catch (const std::regex_error& e) {
        std::cerr << "Regex error: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.code() << std::endl;
    }
    return 0;
}
```

## Handle User-Provided Regex Patterns Safely

```cpp
// CORRECT — safely compile user-provided patterns
#include <regex>
#include <iostream>
#include <string>

std::optional<std::regex> safe_compile(const std::string& pattern) {
    try {
        return std::regex(pattern);
    } catch (const std::regex_error& e) {
        std::cerr << "Invalid regex '" << pattern << "': " << e.what() << std::endl;
        return std::nullopt;
    }
}

int main() {
    auto valid = safe_compile("[a-z]+");
    auto invalid = safe_compile("[a-z");

    if (valid) {
        std::cout << "Valid pattern compiled" << std::endl;
    }
    if (!invalid) {
        std::cerr << "Invalid pattern rejected" << std::endl;
    }
    return 0;
}
```

## Use std::regex_search Without Throwing

```cpp
// CORRECT — use regex_constants::optimize and validate first
#include <regex>
#include <iostream>
#include <string>

bool match_pattern(const std::string& text, const std::string& pattern) {
    try {
        std::regex re(pattern);
        return std::regex_search(text, re);
    } catch (const std::regex_error&) {
        return false;
    }
}

int main() {
    std::string text = "hello123world";

    std::cout << std::boolalpha;
    std::cout << "Alphanumeric: " << match_pattern(text, "[a-z]+[0-9]+") << std::endl;
    std::cout << "Invalid: " << match_pattern(text, "[a-z") << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Catch `std::regex_error` | When compiling user-provided patterns |
| Validate patterns before use | When patterns come from external input |
| Use a safe compile wrapper | When multiple patterns need compilation |
| Use `std::regex_constants::icase` | When case-insensitive matching is needed |

## Related Errors

- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid function arguments.
- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — OS-level error codes.
