---
title: "[Solution] C++ Source Location Error — How to Fix"
description: "Fix C++ std::source_location errors including missing default arguments, lifetime issues with captured locations, and macro usage."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Source Location Error — How to Fix

C++20 `std::source_location` automatically captures call-site information for logging and diagnostics. Incorrect usage with default arguments, lifetime issues, and macro interactions cause errors.

## Why It Happens

Source location errors occur when `std::source_location::current()` is called explicitly instead of using the default argument pattern, when the location is captured by value in a lambda that outlives the call site, or when macros don't properly forward the location parameter.

## Common Error Messages

1. `error: no matching function for call to 'std::source_location::current()'`
2. `error: 'source_location' is not a type`
3. `error: capture of non-variable 'std::source_location::current()'`
4. `error: default argument must be an initializer`

## How to Fix It

### Fix 1: Use Default Argument Pattern

```cpp
#include <source_location>
#include <iostream>

// CORRECT — default argument captures call site
void log(const char* msg,
         std::source_location loc = std::source_location::current()) {
    std::cout << loc.file_name() << ":" << loc.line()
              << " [" << loc.function_name() << "] " << msg << "\n";
}

int main() {
    log("Hello");  // captures main() as call site
}
```

### Fix 2: Pass Location Through Function Calls

```cpp
#include <source_location>
#include <iostream>

void inner_func(std::source_location loc = std::source_location::current()) {
    std::cout << "Called from: " << loc.function_name() << "\n";
}

void outer_func(std::source_location loc = std::source_location::current()) {
    std::cout << "Outer from: " << loc.function_name() << "\n";
    inner_func(loc);  // forward to preserve original call site
}
```

### Fix 3: Store Location for Deferred Use

```cpp
#include <source_location>
#include <string>

struct LogEntry {
    std::string message;
    std::source_location location;
};

LogEntry create_log(const char* msg,
                    std::source_location loc = std::source_location::current()) {
    return {msg, loc};
}

void process() {
    auto entry = create_log("debug info");
    // entry.location still refers to the process() call site
}
```

## Common Scenarios

- **Macro wrapping**: Source location inside macros may capture the macro definition site, not the call site.
- **Template instantiation**: Source location captures the point of instantiation, which may differ from the point of definition.
- **Compiler support**: Not all compilers fully support `source_location` — check your toolchain version.

## Prevent It

1. Always use `std::source_location::current()` as a default argument, never call it explicitly in logging functions.
2. Forward the location parameter through helper functions to preserve the original call site.
3. Use macros to inject `std::source_location::current()` into constructors where default arguments can't be used.

## Related Errors

- [Assert error]({{< relref "/languages/cpp/assertion-failure" >}}) — debug assertion with location info.
- [Preprocessor error]({{< relref "/languages/cpp/preprocessor-error" >}}) — macro expansion issues.
- [Stacktrace error]({{< relref "/languages/cpp/cpp-stacktrace-error" >}}) — similar diagnostic information.
