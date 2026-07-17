---
title: "[Solution] std::regex Pattern Compilation Error Fix"
description: "Fix std::regex pattern compilation errors. Handle regex_error from invalid patterns and performance issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["regex", "pattern", "compilation", "std", "search"]
weight: 5
---

# std::regex Pattern Compilation Error

Fix std::regex pattern compilation errors. Handle regex_error from invalid patterns and performance issues.

## What This Error Means

std::regex throws `std::regex_error` when the pattern is invalid:

```
terminate called after throwing an instance of 'std::regex_error'
  what():  regex_error
```

## Common Causes

```cpp
// Cause 1: Unclosed brackets
std::regex re("[a-z"); // Missing ]

// Cause 2: Unescaped special characters
std::regex re("price: $5.00"); // $ is special

// Cause 3: Invalid repetition
std::regex re("a++"); // Double +

// Cause 4: Catastrophic backtracking pattern
std::regex re("(a+)+b"); // Exponential time on "aaa..."
```

## How to Fix

### Fix 1: Escape special characters with std::regex::escape

```cpp
#include <regex>
#include <string>

std::string escape_regex(const std::string& input) {
    std::string result;
    for (char c : input) {
        if (std::ispunct(static_cast<unsigned char>(c))) {
            result += '\\';
        }
        result += c;
    }
    return result;
}

std::regex make_literal_regex(const std::string& literal) {
    return std::regex(escape_regex(literal));
}
```

### Fix 2: Validate pattern before compilation

```cpp
#include <regex>
#include <iostream>

bool is_valid_regex(const std::string& pattern) {
    try {
        std::regex(pattern);
        return true;
    } catch (const std::regex_error&) {
        return false;
    }
}
```

### Fix 3: Use simple regex patterns to avoid backtracking

```cpp
#include <regex>

// Bad: catastrophic backtracking
// std::regex bad("(a+)+b");

// Good: atomic-like grouping
std::regex good("a+b");
```

## Examples

```cpp
#include <regex>
#include <string>
#include <iostream>

std::string replace_pattern(
    const std::string& input,
    const std::string& pattern,
    const std::string& replacement
) {
    try {
        std::regex re(pattern);
        return std::regex_replace(input, re, replacement);
    } catch (const std::regex_error& e) {
        std::cerr << "Invalid regex: " << e.what() << std::endl;
        return input;
    }
}

int main() {
    std::string text = "Hello World 123";

    // Replace digits
    std::string result = replace_pattern(text, "\\d+", "NUM");
    std::cout << result << std::endl;
    // Output: Hello World NUM

    return 0;
}
```

## Related Errors

- [Regex Error Syntax]({{< relref "/languages/cpp/regex-error-syntax" >}}) — regex syntax error
- [Regex Error 2]({{< relref "/languages/cpp/regex-error-2" >}}) — regex error
- [Regex Error]({{< relref "/languages/cpp/regexerror" >}}) — regex error
