---
title: "[Solution] C++ std::ofstream - output file error"
description: "Fix C++ std::ofstream output file errors. Handle file write failures and permission issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ofstream", "output-file", "write", "permission", "io"]
weight: 5
---

# std::ofstream - output file error

`std::ofstream` errors occur when opening or writing to an output file stream fails.

## Common Causes

```cpp
// Cause 1: Directory doesn't exist
std::ofstream file("/nonexistent/dir/file.txt");

// Cause 2: Permission denied
std::ofstream file("/root/protected.txt");

// Cause 3: Disk full
std::ofstream file("output.txt");
file << huge_data; // failbit when disk full
```

## How to Fix

### Fix 1: Check open success

```cpp
std::ofstream file("output.txt");
if (!file.is_open()) {
    std::cerr << "Cannot create file" << std::endl;
    return 1;
}
```

### Fix 2: Verify directory exists

```cpp
#include <filesystem>
std::filesystem::create_directories("output/dir");
std::ofstream file("output/dir/data.txt");
```

### Fix 3: Check after write

```cpp
file << data;
if (file.bad()) {
    std::cerr << "Write error (disk full?)" << std::endl;
}
```

## Related Errors

- [std::ifstream - input file error]({{< relref "/languages/cpp/ifstream-error" >}}) — input file error.
- [std::fstream - file stream error]({{< relref "/languages/cpp/fstream-error" >}}) — general fstream error.
- [std::filesystem_error]({{< relref "/languages/cpp/filesystem-error" >}}) — filesystem errors.
