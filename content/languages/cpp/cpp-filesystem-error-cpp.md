---
title: "[Solution] C++ Filesystem Error — How to Fix"
description: "Fix C++ std::filesystem errors including permission denied, path not found, and cross-platform path handling issues."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Filesystem Error — How to Fix

C++17 `std::filesystem` provides portable filesystem operations, but permission errors, path resolution issues, and platform-specific behaviors cause `std::filesystem::filesystem_error` exceptions.

## Why It Happens

Filesystem errors occur when the path doesn't exist, when the process lacks file permissions, when the path exceeds platform limits, when trying to modify files held open by other processes, or when symbolic link targets are unavailable.

## Common Error Messages

1. `filesystem error: No such file or directory`
2. `filesystem error: Permission denied`
3. `filesystem error: File exists` (on rename/mkdir)
4. `filesystem error: Too many levels of symbolic links`

## How to Fix It

### Fix 1: Check Path Existence Before Operations

```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::path p = "/tmp/myfile.txt";

    // WRONG — may throw
    // fs::remove(p);

    // CORRECT — check first
    if (fs::exists(p)) {
        fs::remove(p);
        std::cout << "Removed\n";
    } else {
        std::cout << "File doesn't exist\n";
    }
}
```

### Fix 2: Use error_code Instead of Exceptions

```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    std::error_code ec;
    fs::path p = "/tmp/testdir";

    fs::create_directories(p, ec);
    if (ec) {
        std::cerr << "Error: " << ec.message() << "\n";
    } else {
        std::cout << "Directory created\n";
    }

    fs::remove_all(p, ec);
}
```

### Fix 3: Handle Platform-Specific Paths

```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    // Portable path construction
    fs::path dir = "/tmp";
    fs::path filename = "data.txt";
    fs::path full = dir / filename;

    std::cout << "Full path: " << full << "\n";
    std::cout << "Extension: " << full.extension() << "\n";
    std::cout << "Stem: " << full.stem() << "\n";

    // Canonical path resolves symlinks and relative components
    // fs::path canonical = fs::canonical(full);  // may throw
}
```

## Common Scenarios

- **Concurrent access**: Multiple processes modifying the same file cause race conditions.
- **Symlink following**: Many operations follow symlinks by default — use `std::filesystem::symlink_status` to check.
- **Cross-platform**: Paths work differently on Windows vs. POSIX — use `fs::path` instead of string concatenation.

## Prevent It

1. Always use `std::error_code` overloads for filesystem operations in production code.
2. Use `fs::exists()` or `fs::status()` before destructive operations.
3. Use `fs::path` instead of string manipulation for path construction.

## Related Errors

- [File not found]({{< relref "/languages/cpp/file-not-found" >}}) — missing files.
- [Permission denied]({{< relref "/languages/cpp/permission-denied" >}}) — access control issues.
- [Stream error]({{< relref "/languages/cpp/cpp-stream-error-cpp" >}}) — file stream failures.
