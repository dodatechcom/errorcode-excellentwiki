---
title: "[Solution] C++ std::filesystem::filesystem_error — File System Operation Failed Fix"
description: "Fix C++ std::filesystem::filesystem_error when file operations fail. Handle permission errors, missing files, and cross-platform path issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["filesystem-error", "filesystem_error", "filesystem", "path", "io-error"]
weight: 5
---

# [Solution] C++ std::filesystem::filesystem_error — File System Operation Failed Fix

A `std::filesystem::filesystem_error` is thrown when a file system operation fails. This exception carries an error code (accessible via `.code()`) and the path(s) involved (via `.path1()` and `.path2()`). It is defined in `<filesystem>` and occurs during operations like `rename`, `remove`, `create_directories`, `copy`, or path queries.

## Common Causes

- **Permission denied** — the process lacks read/write/execute permission on the target path
- **File or directory does not exist** — operating on a non-existent path
- **Cross-platform path issues** — paths using wrong separators or invalid characters
- **File already exists** — `rename` or `create_directory` when the target already exists
- **Symlink loops** — recursive symlink traversal hits a cycle

## How to Fix

### Fix 1: Check for file existence before operations

```cpp
#include <iostream>
#include <filesystem>
#include <fstream>

namespace fs = std::filesystem;

int main() {
    fs::path file = "config.json";

    if (!fs::exists(file)) {
        std::cerr << "File not found: " << file << std::endl;
        return 1;
    }

    try {
        auto size = fs::file_size(file);
        std::cout << "Size: " << size << " bytes" << std::endl;
    } catch (const fs::filesystem_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```

### Fix 2: Handle permission errors gracefully

```cpp
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    fs::path target = "/root/protected_file";

    try {
        fs::remove(target);
    } catch (const fs::filesystem_error& e) {
        if (e.code() == std::errc::permission_denied) {
            std::cerr << "Permission denied: " << e.path1() << std::endl;
            return 1;
        }
        throw;
    }

    return 0;
}
```

### Fix 3: Use error_code overloads to avoid exceptions

```cpp
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    fs::path target = "/tmp/test_dir";
    std::error_code ec;

    fs::create_directories(target, ec);
    if (ec) {
        std::cerr << "Failed to create directory: " << ec.message() << std::endl;
        return 1;
    }

    std::cout << "Directory created successfully" << std::endl;
    return 0;
}
```

### Fix 4: Normalize paths before use

```cpp
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    fs::path raw = "/tmp/../tmp/./test.txt";
    fs::path normalized = fs::weakly_canonical(raw);
    std::cout << "Normalized: " << normalized << std::endl;

    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    /* Rename to existing file */
    try {
        fs::rename("file_a.txt", "file_b.txt");
    } catch (const fs::filesystem_error& e) {
        std::cerr << e.what() << std::endl;
    }

    /* Remove non-existent file */
    try {
        fs::remove("/nonexistent/file");
    } catch (const fs::filesystem_error& e) {
        std::cerr << e.what() << std::endl;
    }

    /* Permission denied */
    try {
        fs::permissions("/etc/shadow", fs::perms::owner_write);
    } catch (const fs::filesystem_error& e) {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}
```

## Related Errors

- [std::runtime_error]({{< relref "/languages/cpp/runtime-error12" >}}) — general runtime errors
- [std::system_error]({{< relref "/languages/cpp/system-error" >}}) — OS-level error codes
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-failure" >}}) — stream I/O failures
