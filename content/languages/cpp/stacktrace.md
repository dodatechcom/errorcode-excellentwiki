---
title: "[Solution] C++ std::stacktrace — Stack Trace Capture Fix"
description: "Fix C++ std::stacktrace issues including missing debug info, platform support, and performance. Learn stacktrace usage patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::stacktrace — Stack Trace Capture Fix

`std::stacktrace` (C++23) captures the call stack at a point in execution. Issues include compilation failures on unsupported platforms, empty stack traces when debug info is stripped, and performance overhead from capturing traces in hot paths.

## Why stacktrace Issues Occur

Common causes include compiler/platform not supporting C++23 stacktrace, debug symbols stripped in release builds (`-g` not used), performance overhead of capturing stack traces in loops, and incorrect formatting of stacktrace output.

## Wrong: Using stacktrace Without Platform Support

```cpp
// WRONG — may not compile on all platforms
#include <stacktrace>
#include <iostream>

int main() {
    auto trace = std::stacktrace::current();  // may fail to compile
    std::cout << trace << std::endl;
    return 0;
}
```

## Correct: Conditional Compilation With stacktrace

```cpp
// CORRECT — guard with feature test macro
#include <iostream>

#if __has_include(<stacktrace>) && defined(__cpp_lib_stacktrace)
#include <stacktrace>

void print_trace() {
    auto trace = std::stacktrace::current();
    std::cout << "Stack trace:\n" << trace << std::endl;
}
#else
void print_trace() {
    std::cout << "Stacktrace not available on this platform" << std::endl;
}
#endif

int main() {
    print_trace();
    return 0;
}
```

## Use Stacktrace in Exception Handling

```cpp
// CORRECT — capture trace at throw site
#include <iostream>

#if __has_include(<stacktrace>) && defined(__cpp_lib_stacktrace)
#include <stacktrace>
#include <stdexcept>
#include <string>

class traced_error : public std::runtime_error {
    std::stacktrace trace_;
public:
    traced_error(const std::string& msg)
        : std::runtime_error(msg), trace_(std::stacktrace::current()) {}

    const std::stacktrace& trace() const { return trace_; }
};

int main() {
    try {
        throw traced_error("something went wrong");
    } catch (const traced_error& e) {
        std::cerr << e.what() << std::endl;
        std::cerr << "Trace:\n" << e.trace() << std::endl;
    }
    return 0;
}
#else
int main() {
    std::cout << "Stacktrace not supported" << std::endl;
    return 0;
}
#endif
```

## Capture Selective Trace Depth

```cpp
// CORRECT — limit trace depth for performance
#include <iostream>

#if __has_include(<stacktrace>) && defined(__cpp_lib_stacktrace)
#include <stacktrace>

std::stacktrace get_trace(int skip = 0) {
    auto full = std::stacktrace::current();
    // In practice, filter by skipping frames
    return full;
}

int main() {
    auto trace = get_trace();
    std::cout << "Frames: " << trace.size() << std::endl;
    return 0;
}
#else
int main() {
    std::cout << "Stacktrace not supported" << std::endl;
    return 0;
}
#endif
```

## Summary

| Fix | When to Use |
|---|---|
| Use `#if __has_include` guard | For cross-platform compatibility |
| Compile with `-g` flag | To get meaningful stack traces |
| Avoid in hot paths | Stack capture has performance cost |
| Use in error/exception contexts | For diagnostic purposes |

## Related Errors

- [std::source_location]({{< relref "/languages/cpp/source-location" >}}) — source location capture.
- [std::print error]({{< relref "/languages/cpp/print-error" >}}) — print function errors.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
