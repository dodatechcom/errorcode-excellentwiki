---
title: "[Solution] C++ std::fstream - file stream error"
description: "Fix C++ std::fstream file stream errors. Handle file open, read, and write failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["fstream", "file-stream", "open", "read", "write", "io"]
weight: 5
---

# std::fstream - file stream error

`std::fstream` errors occur when file operations fail. The stream enters a fail state and subsequent operations will fail until cleared.

## Common Causes

```cpp
// Cause 1: File doesn't exist
std::fstream file("missing.txt", std::ios::in);
if (!file.is_open()) { /* error */ }

// Cause 2: Permission denied
std::fstream file("/root/secret.txt", std::ios::out);

// Cause 3: Disk full
std::fstream file("output.txt", std::ios::out);
file << huge_data; // failbit on disk full
```

## How to Fix

### Fix 1: Check open success

```cpp
std::fstream file("data.txt", std::ios::in | std::ios::out);
if (!file.is_open()) {
    std::cerr << "Failed to open file" << std::endl;
    return 1;
}
```

### Fix 2: Check after operations

```cpp
file << data;
if (file.fail()) {
    std::cerr << "Write failed" << std::endl;
}
```

### Fix 3: Use error_code with filesystem

```cpp
#include <filesystem>
std::error_code ec;
auto size = std::filesystem::file_size("data.txt", ec);
if (ec) {
    std::cerr << ec.message() << std::endl;
}
```

## Related Errors

- [std::ifstream - input file error]({{< relref "/languages/cpp/ifstream-error" >}}) — input file error.
- [std::ofstream - output file error]({{< relref "/languages/cpp/ofstream-error" >}}) — output file error.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream exception.
