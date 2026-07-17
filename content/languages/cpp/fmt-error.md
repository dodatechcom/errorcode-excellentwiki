---
title: "[Solution] C++ fmt - formatting error"
description: "Fix C++ fmt library formatting errors. Resolve fmt::format string issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# fmt - formatting error

The fmt library throws errors when format strings are invalid, arguments don't match placeholders, or types are unsupported.

## Common Causes

```cpp
// Cause 1: Wrong argument count
auto s = fmt::format("Hello, {} and {}!", "Alice"); // too few args

// Cause 2: Invalid format syntax
auto s = fmt::format("Hello, {name!", "Alice"); // missing closing brace

// Cause 3: Wrong type
auto s = fmt::format("{:d}", "not a number"); // wrong format specifier
```

## How to Fix

### Fix 1: Match argument count

```cpp
auto s = fmt::format("Hello, {} and {}!", "Alice", "Bob");
```

### Fix 2: Fix format syntax

```cpp
auto s = fmt::format("Hello, {name}!", fmt::arg("name", "Alice"));
```

### Fix 3: Use correct format specifiers

```cpp
auto s = fmt::format("{:.2f}", 3.14159); // correct for float
auto s = fmt::format("{:d}", 42); // correct for int
```

## Related Errors

- [spdlog - logging error]({{< relref "/languages/cpp/spdlog-error" >}}) — logging errors.
- [fmt format error (detailed)]({{< relref "/languages/cpp/fmt-error" >}}) — detailed fmt errors.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream errors.
