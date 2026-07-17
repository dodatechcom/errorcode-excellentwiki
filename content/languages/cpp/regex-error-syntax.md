---
title: "[Solution] C++ std::regex_error - regex syntax error"
description: "Fix C++ std::regex_error from invalid regular expression syntax. Validate regex patterns."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::regex_error - regex syntax error

`std::regex_error` is thrown when a regular expression pattern has invalid syntax. This happens at regex construction time.

## Common Causes

```cpp
// Cause 1: Unclosed group
std::regex r("(hello"); // throws regex_error

// Cause 2: Invalid escape
std::regex r("\\"); // throws — invalid escape

// Cause 3: Invalid quantifier
std::regex r("*hello"); // throws — nothing to quantify
```

## How to Fix

### Fix 1: Validate regex syntax

```cpp
std::regex create_regex(const std::string& pattern) {
    try {
        return std::regex(pattern);
    } catch (const std::regex_error& e) {
        std::cerr << "Invalid regex: " << e.what() << std::endl;
        return std::regex(".*"); // fallback
    }
}
```

### Fix 2: Use raw string literals

```cpp
std::regex r(R"(\d+\.\d+)"); // easier to read
```

### Fix 3: Test regex before use

```cpp
std::string pattern = user_input;
try {
    std::regex test(pattern);
    // valid — use it
} catch (const std::regex_error&) {
    std::cerr << "Invalid pattern" << std::endl;
}
```

## Related Errors

- [std::regex_error (detailed)]({{< relref "/languages/cpp/regex-error" >}}) — detailed regex errors.
- [std::regex_error - variant 2]({{< relref "/languages/cpp/regex-error-2" >}}) — regex match errors.
- [std::invalid_argument - stoi]({{< relref "/languages/cpp/invalid-argument-stoi" >}}) — conversion errors.
