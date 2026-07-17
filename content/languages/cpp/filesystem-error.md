---
title: "[Solution] C++ std::filesystem::filesystem_error"
description: "Fix C++ std::filesystem::filesystem_error. Handle filesystem operation failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["filesystem", "filesystem_error", "error-code", "path", "filesystem-library"]
weight: 5
---

# std::filesystem::filesystem_error

`std::filesystem::filesystem_error` is thrown when a filesystem operation fails. The error includes the path and error code.

## Common Causes

```cpp
// Cause 1: File not found
std::filesystem::path p = "/nonexistent/file.txt";
auto size = std::filesystem::file_size(p); // throws

// Cause 2: Permission denied
std::filesystem::remove("/root/protected.txt"); // throws

// Cause 3: Path too long
std::string long_path(10000, 'a');
std::filesystem::create_directories(long_path); // throws
```

## How to Fix

### Fix 1: Use error_code overload

```cpp
std::error_code ec;
auto size = std::filesystem::file_size(p, ec);
if (ec) {
    std::cerr << "Error: " << ec.message() << std::endl;
}
```

### Fix 2: Check existence first

```cpp
if (std::filesystem::exists(p)) {
    std::filesystem::remove(p);
}
```

### Fix 3: Catch and handle

```cpp
try {
    std::filesystem::copy_file(src, dst);
} catch (const std::filesystem::filesystem_error& e) {
    std::cerr << e.what() << std::endl;
    std::cerr << "Path: " << e.path1() << std::endl;
}
```

## Related Errors

- [std::filesystem::filesystem_error (detailed)]({{< relref "/languages/cpp/filesystem-error" >}}) — detailed analysis.
- [C: No such file]({{< relref "/languages/c/no-such-file" >}}) — ENOENT.
- [C: Permission denied]({{< relref "/languages/c/permission-denied-file" >}}) — EACCES.
