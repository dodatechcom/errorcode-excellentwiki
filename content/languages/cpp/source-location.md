---
title: "[Solution] C++ std::source_location — Source Location Fix"
description: "Fix C++ std::source_location issues including incorrect caller information and portability. Learn correct source_location usage."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["source-location", "debugging", "c++20", "diagnostics"]
weight: 5
---

# [Solution] C++ std::source_location — Source Location Fix

`std::source_location` (C++20) captures file, line, column, and function name at the point of construction. Issues arise when the default argument captures the wrong location (e.g., inside a wrapper function), when the implementation doesn't support it, or when used incorrectly across inline boundaries.

## Why source_location Issues Occur

Common causes include using default parameter `std::source_location::current()` in a wrapper function (it captures the wrapper's location, not the caller's), platform differences in `function_name()` output, and using in constexpr context where it's not yet fully supported.

## Wrong: Capturing Location in Wrapper

```cpp
// WRONG — source_location captures wrapper's location
#include <source_location>
#include <iostream>
#include <string>

void log_impl(const std::string& msg, std::source_location loc = std::source_location::current()) {
    std::cout << loc.file_name() << ":" << loc.line() << " " << msg << std::endl;
}

void my_log(const std::string& msg) {
    log_impl(msg);  // loc captures log_impl's line, not my_log's
}

int main() {
    my_log("hello");  // prints my_log's location info, not main's
    return 0;
}
```

## Correct: Pass source_location Explicitly

```cpp
// CORRECT — pass source_location through wrapper
#include <source_location>
#include <iostream>
#include <string>

void log_impl(const std::string& msg, std::source_location loc = std::source_location::current()) {
    std::cout << loc.file_name() << ":" << loc.line()
              << " in " << loc.function_name() << ": " << msg << std::endl;
}

void my_log(const std::string& msg, std::source_location loc = std::source_location::current()) {
    log_impl(msg, loc);  // pass caller's location through
}

int main() {
    my_log("hello");  // correctly shows main's location
    return 0;
}
```

## Use in Error Reporting

```cpp
// CORRECT — use source_location for error context
#include <source_location>
#include <iostream>
#include <stdexcept>
#include <string>

class error : public std::runtime_error {
    std::source_location loc_;
public:
    error(const std::string& msg, std::source_location loc = std::source_location::current())
        : std::runtime_error(msg), loc_(loc) {}

    const char* file() const { return loc_.file_name(); }
    int line() const { return loc_.line(); }
    const char* function() const { return loc_.function_name(); }
};

void process(int value) {
    if (value < 0) {
        throw error("Negative value: " + std::to_string(value));
    }
}

int main() {
    try {
        process(-1);
    } catch (const error& e) {
        std::cerr << e.file() << ":" << e.line()
                  << " in " << e.function() << ": " << e.what() << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Pass source_location explicitly through wrappers | When wrapping logging/assertion functions |
| Use as default parameter at the call site | When you want the immediate caller's location |
| Store in exception classes | For enhanced error diagnostics |
| Use `function_name()` for debugging | When function context is needed |

## Related Errors

- [std::stacktrace]({{< relref "/languages/cpp/stacktrace" >}}) — stack trace capture.
- [std::print error]({{< relref "/languages/cpp/print-error" >}}) — print function errors.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
