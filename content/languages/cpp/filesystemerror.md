---
title: "[Solution] C++ std::filesystem::filesystem_error — Filesystem Operation Failed Fix"
description: "Fix C++ std::filesystem::filesystem_error when filesystem operations fail. Handle file access errors, missing paths, and permission issues."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["filesystem-error", "std-filesystem", "file-io", "exception"]
weight: 50
---

# [Solution] C++ std::filesystem::filesystem_error — Filesystem Operation Failed Fix

A `std::filesystem::filesystem_error` is thrown when a filesystem operation fails due to an OS-level error. This includes file not found, permission denied, path too long, or disk full conditions. The exception provides both the error code and the path(s) involved in the failed operation.

## Why std::filesystem::filesystem_error Occurs

Common causes include accessing files that do not exist, insufficient permissions to read or write files, invalid file paths, files or directories locked by other processes, and disk full conditions.

## Wrong: Not Catching filesystem_error

```cpp
// WRONG — program crashes on filesystem errors
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::remove("/nonexistent/file.txt");  // throws filesystem_error
    return 0;
}
```

## Correct: Catch filesystem_error and Inspect the Error Code

```cpp
// CORRECT — catch and inspect the error code
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    try {
        fs::remove("/nonexistent/file.txt");
    } catch (const fs::filesystem_error& e) {
        std::cerr << "Filesystem error: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.code() << std::endl;
        std::cerr << "Path: " << e.path1() << std::endl;
        return 1;
    }
    return 0;
}
```

## Using Error Code Overload to Avoid Exceptions

```cpp
// CORRECT — use error_code overload instead of throwing
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    std::error_code ec;
    fs::remove("/nonexistent/file.txt", ec);

    if (ec) {
        std::cerr << "Failed to remove: " << ec.message() << std::endl;
        return 1;
    }

    std::cout << "File removed successfully" << std::endl;
    return 0;
}
```

## Checking File Existence Before Operations

```cpp
// CORRECT — check existence before performing operations
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::path file_path = "/tmp/test.txt";

    if (!fs::exists(file_path)) {
        std::cerr << "File does not exist: " << file_path << std::endl;
        return 1;
    }

    try {
        auto file_size = fs::file_size(file_path);
        std::cout << "File size: " << file_size << " bytes" << std::endl;
    } catch (const fs::filesystem_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```

## Safe Directory Operations

```cpp
// CORRECT — handle directory operations gracefully
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::path dir = "/tmp/myapp/data";

    // Create directories recursively
    std::error_code ec;
    fs::create_directories(dir, ec);
    if (ec) {
        std::cerr << "Failed to create directories: " << ec.message() << std::endl;
        return 1;
    }

    // List directory contents safely
    for (const auto& entry : fs::directory_iterator(dir, ec)) {
        std::cout << entry.path() << std::endl;
    }
    if (ec) {
        std::cerr << "Error reading directory: " << ec.message() << std::endl;
    }

    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `error_code` overload | When you want to avoid exceptions |
| Check `fs::exists()` before operations | When paths may be invalid |
| Catch `filesystem_error` | When you need the full error context |
| Use `create_directories()` | When intermediate directories may not exist |

## Related Errors

- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — OS-level error codes wrapped in exceptions.
- [std::invalid_argument]({{< relref "/languages/cpp/invalid-argument" >}}) — invalid function arguments.
