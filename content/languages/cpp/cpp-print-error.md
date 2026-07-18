---
title: "[Solution] C++ Print Error — How to Fix"
description: "Fix C++ std::print and std::println errors including format string mismatches, stream flush issues, and encoding problems."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time", "runtime"]
weight: 5
comments: true
---

# [Solution] C++ Print Error — How to Fix

C++23 `std::print` and `std::println` provide efficient console output with format string validation. Format mismatches, encoding issues, and file descriptor errors cause failures.

## Why It Happens

Print errors occur when format strings don't match argument types, when output streams are in a bad state, when wide/narrow character encoding conversions fail, or when printing to invalid file descriptors.

## Common Error Messages

1. `error: no matching function for call to 'std::print'`
2. `error: format string is not a constant expression`
3. `error: cannot convert 'const char*' to 'std::string_view' for format argument`
4. `std::format_error: invalid format string`

## How to Fix It

### Fix 1: Use Constant Expression Format Strings

```cpp
#include <print>

// CORRECT — format string as literal (compile-time checked)
std::println("Hello, {}!", "world");

// WRONG — runtime format string not allowed
// const char* fmt = "Hello, {}!";
// std::println(fmt, "world");  // error
```

### Fix 2: Match Argument Types

```cpp
#include <print>

struct Point { int x, y; };

template <>
struct std::formatter<Point> : std::formatter<std::string> {
    auto format(const Point& p, auto& ctx) const {
        return std::format_to(ctx.out(), "({}, {})", p.x, p.y);
    }
};

int main() {
    Point p{10, 20};
    std::println("Position: {}", p);
}
```

### Fix 3: Use std::println for Automatic Newline

```cpp
#include <print>
#include <string>

int main() {
    std::string name = "Alice";
    int age = 30;

    // println adds newline automatically
    std::println("Name: {}, Age: {}", name, age);

    // print does NOT add newline
    std::print("Enter name: ");
}
```

## Common Scenarios

- **Buffer flushing**: `std::println` flushes after each call; use `std::print` for batch output.
- **Encoding conversion**: UTF-8 strings may need conversion on Windows console.
- **File output**: Use `std::print(f, ...)` to print to files.

## Prevent It

1. Always use string literals for format strings — not runtime strings.
2. Provide `std::formatter` specializations for custom types before using `std::print`.
3. Use `std::println` instead of `std::print` with `"\n"` for better performance.

## Related Errors

- [Format error]({{< relref "/languages/cpp/cpp-format-error" >}}) — std::format issues.
- [Stream error]({{< relref "/languages/cpp/cpp-stream-error-cpp" >}}) — iostream state problems.
- [Locale error]({{< relref "/languages/cpp/cpp-locale-error" >}}) — encoding and locale issues.
