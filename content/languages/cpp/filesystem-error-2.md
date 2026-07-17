---
title: "[Solution] C++ std::filesystem::filesystem_error — Filesystem Operation Fix"
description: "Fix C++ std::filesystem::filesystem_error when filesystem operations fail. Handle permission denied, file not found, and path errors."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::filesystem::filesystem_error — Filesystem Operation Fix

A `std::filesystem::filesystem_error` is thrown when a filesystem operation fails. It inherits from `std::system_error` and provides additional information about the source and target paths involved in the operation. Common operations that throw include `rename`, `copy`, `remove`, `create_directories`, and `last_write_time`.

## Why std::filesystem::filesystem_error Occurs

Common causes include permission denied when accessing or modifying files, file or directory not found when the path does not exist, file already exists when creating new files, path too long for the filesystem, and cross-device link errors when renaming across mount points.

## Wrong: Calling Filesystem Functions Without Error Handling

```cpp
// WRONG — throws filesystem_error if path doesn't exist
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::copy("source.txt", "dest.txt");  // throws if source doesn't exist
    return 0;
}
```

## Correct: Check Path Exists Before Operations

```cpp
// CORRECT — validate path before operating
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::path src = "source.txt";
    fs::path dst = "dest.txt";

    if (!fs::exists(src)) {
        std::cerr << "Source file does not exist: " << src << std::endl;
        return 1;
    }

    try {
        fs::copy(src, dst);
        std::cout << "Copied successfully" << std::endl;
    } catch (const fs::filesystem_error& e) {
        std::cerr << "Filesystem error: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.code().message() << std::endl;
    }
    return 0;
}
```

## Handle Specific Error Codes

```cpp
// CORRECT — handle specific filesystem error conditions
#include <filesystem>
#include <iostream>
#include <system_error>

namespace fs = std::filesystem;

int main() {
    fs::path dir = "/root/protected";

    try {
        fs::create_directories(dir);
    } catch (const fs::filesystem_error& e) {
        if (e.code() == std::errc::permission_denied) {
            std::cerr << "Permission denied: " << e.what() << std::endl;
        } else if (e.code() == std::errc::file_exists) {
            std::cerr << "Directory already exists" << std::endl;
        } else {
            std::cerr << "Filesystem error: " << e.what() << std::endl;
        }
        return 1;
    }
    return 0;
}
```

## Use std::error_code Overload for Non-Throwing Operations

```cpp
// CORRECT — use error_code overload to avoid exceptions
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    std::error_code ec;
    fs::path src = "source.txt";
    fs::path dst = "dest.txt";

    fs::copy(src, dst, ec);

    if (ec) {
        std::cerr << "Copy failed: " << ec.message() << std::endl;
        return 1;
    }

    std::cout << "Copied successfully" << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check `fs::exists()` before operations | When the file might not exist |
| Use `error_code` overloads | When you want non-throwing error handling |
| Catch `filesystem_error` specifically | When you need path information in errors |
| Check `e.code()` for specific conditions | When different errors need different handling |

## Related Errors

- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — OS-level error codes.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-failure" >}}) — stream I/O errors.
