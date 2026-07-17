---
title: "[Solution] C++ std::ios_base::failure - stream error"
description: "Fix C++ std::ios_base::failure stream errors. Handle I/O stream failures and check stream state."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::ios_base::failure - stream error

`std::ios_base::failure` is thrown when an I/O stream operation fails. This includes file errors, format errors, and internal stream failures.

## Common Causes

```cpp
// Cause 1: File not found
std::ifstream file("nonexistent.txt");
file >> value; // may throw ios_base::failure

// Cause 2: Format mismatch
std::stringstream ss("hello");
int val;
ss >> val; // format error

// Cause 3: Permission denied
std::ofstream file("/root/test.txt"); // throws
```

## How to Fix

### Fix 1: Check stream state

```cpp
std::ifstream file("data.txt");
if (!file.is_open()) {
    std::cerr << "Failed to open file" << std::endl;
    return 1;
}
```

### Fix 2: Check after read

```cpp
int val;
if (ss >> val) {
    // success
} else {
    std::cerr << "Format error" << std::endl;
}
```

### Fix 3: Use exception mask

```cpp
std::ifstream file("data.txt");
file.exceptions(std::ifstream::failbit | std::ifstream::badbit);
try {
    file >> value;
} catch (const std::ios_base::failure& e) {
    std::cerr << "Stream error: " << e.what() << std::endl;
}
```

## Related Errors

- [std::fstream - file stream error]({{< relref "/languages/cpp/fstream-error" >}}) — file stream error.
- [std::ifstream - input file error]({{< relref "/languages/cpp/ifstream-error" >}}) — input file error.
- [std::ofstream - output file error]({{< relref "/languages/cpp/ofstream-error" >}}) — output file error.
