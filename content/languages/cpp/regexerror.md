---
title: "[Solution] C++ std::regex_error — Invalid Regular Expression Fix"
description: "Fix C++ std::regex_error when constructing or matching invalid regular expressions. Handle malformed patterns and syntax errors."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["regex-error", "std-regex", "regular-expression", "exception"]
weight: 50
---

# [Solution] C++ std::regex_error — Invalid Regular Expression Fix

A `std::regex_error` is thrown when a regular expression is malformed or uses unsupported syntax for the current grammar flag. This occurs during pattern construction or matching when the regex engine encounters invalid syntax such as unmatched parentheses, invalid escape sequences, or misplaced quantifiers.

## Why std::regex_error Occurs

Common causes include unmatched parentheses or brackets, invalid escape sequences, misplaced quantifiers (e.g., `*` at the start), unsupported regex features for the chosen grammar, and empty patterns with quantifiers.

## Wrong: Constructing an Invalid Regex

```cpp
// WRONG — throws std::regex_error (unmatched parenthesis)
#include <regex>
#include <iostream>

int main() {
    std::regex pattern("(\\d+");  // missing closing parenthesis
    return 0;
}
```

## Correct: Validate Regex Patterns Before Use

```cpp
// CORRECT — catch regex_error during construction
#include <regex>
#include <iostream>

int main() {
    try {
        std::regex pattern("(\\d+");  // invalid — will throw
    } catch (const std::regex_error& e) {
        std::cerr << "Regex error: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.code() << std::endl;
        return 1;
    }
    return 0;
}
```

## Using Safe Regex Construction

```cpp
// CORRECT — wrap regex construction in a function
#include <regex>
#include <iostream>
#include <optional>

std::optional<std::regex> make_regex(const std::string& pattern) {
    try {
        return std::regex(pattern);
    } catch (const std::regex_error&) {
        return std::nullopt;
    }
}

int main() {
    auto email_regex = make_regex("([\\w.-]+)@(\\w+\\.\\w+)");
    if (!email_regex) {
        std::cerr << "Invalid email pattern" << std::endl;
        return 1;
    }

    std::string email = "user@example.com";
    if (std::regex_match(email, *email_regex)) {
        std::cout << "Valid email" << std::endl;
    }

    auto bad_regex = make_regex("(unclosed");
    if (!bad_regex) {
        std::cerr << "Bad regex caught safely" << std::endl;
    }

    return 0;
}
```

## Validating Regex at Program Startup

```cpp
// CORRECT — validate all patterns at startup
#include <regex>
#include <iostream>
#include <vector>
#include <string>

struct Pattern {
    std::string name;
    std::string expression;
    std::regex compiled;
};

std::vector<Pattern> load_patterns() {
    std::vector<Pattern> patterns;
    std::vector<std::pair<std::string, std::string>> raw = {
        {"email", "([\\w.-]+)@(\\w+\\.\\w+)"},
        {"phone", "\\d{3}-\\d{4}"},
        {"date", "\\d{4}-\\d{2}-\\d{2}"},
    };

    for (auto& [name, expr] : raw) {
        try {
            patterns.push_back({name, expr, std::regex(expr)});
        } catch (const std::regex_error& e) {
            std::cerr << "Invalid pattern '" << name << "': " << e.what() << std::endl;
        }
    }
    return patterns;
}

int main() {
    auto patterns = load_patterns();
    std::cout << "Loaded " << patterns.size() << " valid patterns" << std::endl;
    return 0;
}
```

## Common Regex Syntax Errors

| Error | Example | Fix |
|---|---|---|
| Unmatched parenthesis | `(\\d+` | `(\\d+)` |
| Unmatched bracket | `[a-z` | `[a-z]` |
| Quantifier without element | `*abc` | `\\w*abc` |
| Invalid escape | `\\p{L}` (basic) | Use ECMAScript grammar |

## Summary

| Fix | When to Use |
|---|---|
| Catch `std::regex_error` during construction | When patterns come from user input |
| Use a safe construction wrapper | When multiple patterns are compiled |
| Validate patterns at startup | When patterns are known at compile time |
| Use raw string literals `R"(...)"` | To avoid C++ escape complexity |

## Related Errors

- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid function arguments.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::logic_error]({{< relref "/languages/cpp/logic-error" >}}) — logical precondition violations.
