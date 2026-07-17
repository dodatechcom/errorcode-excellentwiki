---
title: "[Solution] C++ std::ios_base::badbit - stream error"
description: "Fix C++ std::ios_base::badbit stream error. Handle critical I/O stream failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ios-base", "badbit", "stream", "critical-error", "io"]
weight: 5
---

# std::ios_base::badbit - stream error

`badbit` is set in an I/O stream when a critical error occurs, such as a loss of integrity of the stream's internal state. This is more severe than `failbit`.

## Common Causes

```cpp
// Cause 1: Physical I/O error
std::ifstream file("device_file");
// Hardware failure during read

// Cause 2: Stream in bad state
std::stringstream ss;
ss.setstate(std::ios::badbit);
int val;
ss >> val; // fails

// Cause 3: File corruption
std::ifstream file("corrupted.dat");
// read fails with badbit
```

## How to Fix

### Fix 1: Check stream state

```cpp
std::ifstream file("data.txt");
if (file.bad()) {
    std::cerr << "Critical I/O error" << std::endl;
    return 1;
}
```

### Fix 2: Use exception mask

```cpp
std::ifstream file("data.txt");
file.exceptions(std::ios::badbit);
try {
    file.read(buffer, size);
} catch (const std::ios_base::failure& e) {
    std::cerr << "Stream error: " << e.what() << std::endl;
}
```

### Fix 3: Clear and retry

```cpp
file.clear(); // clear error state
file.seekg(0); // reposition
file.read(buffer, size); // retry
```

## Related Errors

- [std::ios_base::failbit]({{< relref "/languages/cpp/ios-base-failbit" >}}) — logical I/O error.
- [std::ios_base::eofbit]({{< relref "/languages/cpp/ios-base-eofbit" >}}) — end of file.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream exception.
