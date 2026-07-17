---
title: "[Solution] C++ std::ifstream - input file error"
description: "Fix C++ std::ifstream input file errors. Handle file read failures and missing files."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::ifstream - input file error

`std::ifstream` errors occur when opening or reading from an input file stream fails.

## Common Causes

```cpp
// Cause 1: File doesn't exist
std::ifstream file("missing.txt");
if (!file.is_open()) { /* error */ }

// Cause 2: No read permission
std::ifstream file("/etc/shadow");

// Cause 3: Format mismatch during read
std::ifstream file("data.txt");
int val;
file >> val; // failbit if file contains "hello"
```

## How to Fix

### Fix 1: Check if file opened

```cpp
std::ifstream file("data.txt");
if (!file) {
    std::cerr << "Cannot open file" << std::endl;
    return 1;
}
```

### Fix 2: Read line by line

```cpp
std::ifstream file("data.txt");
std::string line;
while (std::getline(file, line)) {
    // process each line
}
```

### Fix 3: Use exception handling

```cpp
std::ifstream file("data.txt");
file.exceptions(std::ifstream::failbit | std::ifstream::badbit);
try {
    int val;
    file >> val;
} catch (const std::ios_base::failure& e) {
    std::cerr << "Read error: " << e.what() << std::endl;
}
```

## Related Errors

- [std::ofstream - output file error]({{< relref "/languages/cpp/ofstream-error" >}}) — output file error.
- [std::fstream - file stream error]({{< relref "/languages/cpp/fstream-error" >}}) — general fstream error.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream exception.
