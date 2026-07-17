---
title: "[Solution] C++ std::system_error - generic category"
description: "Fix C++ std::system_error with generic category. Handle system-level errors with error codes."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["system-error", "system_error", "generic", "error-code", "errno"]
weight: 5
---

# std::system_error - generic category

`std::system_error` with the generic category wraps POSIX `errno` values. It provides structured error handling for system calls.

## Common Causes

```cpp
// Cause 1: File open failure
std::ifstream file("/nonexistent"); // sets failbit

// Cause 2: Socket error
int sock = socket(AF_INET, SOCK_STREAM, 0);
// Various system call failures

// Cause 3: Thread creation failure
std::thread t([]{}); // may throw system_error
```

## How to Fix

### Fix 1: Use error_code

```cpp
std::error_code ec;
std::filesystem::file_size("file.txt", ec);
if (ec == std::errc::no_such_file_or_directory) {
    std::cerr << "File not found" << std::endl;
}
```

### Fix 2: Catch and inspect

```cpp
try {
    std::thread t([]{ /* work */ });
    t.detach();
} catch (const std::system_error& e) {
    std::cerr << "Error: " << e.what() << std::endl;
    std::cerr << "Code: " << e.code().value() << std::endl;
}
```

### Fix 3: Use strerror for message

```cpp
try {
    // system call
} catch (const std::system_error& e) {
    std::cerr << strerror(e.code().value()) << std::endl;
}
```

## Related Errors

- [std::system_error - system category]({{< relref "/languages/cpp/system-error-system" >}}) — Windows errors.
- [std::filesystem_error]({{< relref "/languages/cpp/filesystem-error" >}}) — filesystem errors.
- [std::future_error]({{< relref "/languages/cpp/future-error" >}}) — future/promise errors.
