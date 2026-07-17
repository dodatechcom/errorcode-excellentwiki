---
title: "[Solution] std::filesystem Directory Iteration Error Fix"
description: "Fix std::filesystem directory iteration errors. Handle permission denied, non-existent paths, and recursive directory errors."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# std::filesystem Directory Iteration Error

Fix std::filesystem directory iteration errors. Handle permission denied, non-existent paths, and recursive directory errors.

## What This Error Means

std::filesystem directory errors occur when iterating or manipulating directories:

```
filesystem error: cannot increment directory iterator
filesystem error: directory not found
filesystem error: permission denied
```

## Common Causes

```cpp
// Cause 1: Directory deleted during iteration
for (auto& entry : std::filesystem::directory_iterator("/tmp")) {
    std::filesystem::remove(entry); // May invalidate iterator
}

// Cause 2: Symlink loop causes infinite iteration
// Cause 3: Permission denied on restricted directory
// Cause 4: Path contains invalid characters
```

## How to Fix

### Fix 1: Use error_code overload for safe iteration

```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

void list_directory(const fs::path& dir) {
    std::error_code ec;
    for (auto& entry : fs::directory_iterator(dir, ec)) {
        std::cout << entry.path() << std::endl;
    }
    if (ec) {
        std::cerr << "Error: " << ec.message() << std::endl;
    }
}
```

### Fix 2: Collect paths first, then modify

```cpp
#include <filesystem>
#include <vector>

namespace fs = std::filesystem;

void remove_old_files(const fs::path& dir, int max_age_days) {
    // Collect first to avoid invalidating iterator
    std::vector<fs::path> to_remove;
    for (auto& entry : fs::directory_iterator(dir)) {
        // Check file age and collect paths
        to_remove.push_back(entry.path());
    }

    for (auto& path : to_remove) {
        fs::remove(path);
    }
}
```

### Fix 3: Use recursive_directory_iterator with max depth

```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

void list_recursive(const fs::path& root) {
    for (auto& entry :
         fs::recursive_directory_iterator(root, fs::directory_options::skip_permission_denied)) {
        std::cout << entry.path() << std::endl;
    }
}
```

## Examples

```cpp
#include <filesystem>
#include <iostream>
#include <vector>

namespace fs = std::filesystem;

std::vector<fs::path> find_files(
    const fs::path& root,
    const std::string& extension
) {
    std::vector<fs::path> results;
    std::error_code ec;

    for (auto& entry : fs::recursive_directory_iterator(root, ec)) {
        if (entry.is_regular_file() && entry.path().extension() == extension) {
            results.push_back(entry.path());
        }
    }

    if (ec) {
        std::cerr << "Warning: " << ec.message() << std::endl;
    }

    return results;
}

int main() {
    auto files = find_files(".", ".cpp");
    for (auto& f : files) {
        std::cout << f << std::endl;
    }
    return 0;
}
```

## Related Errors

- [Filesystem Error 2]({{< relref "/languages/cpp/filesystem-error-2" >}}) — filesystem error
- [FStream Error]({{< relref "/languages/cpp/fstream-error" >}}) — fstream error
- [IFStream Error]({{< relref "/languages/cpp/ifstream-error" >}}) — ifstream error
