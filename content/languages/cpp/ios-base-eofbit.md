---
title: "[Solution] C++ std::ios_base::eofbit - end of file"
description: "Fix C++ std::ios_base::eofbit end of file. Handle end-of-file conditions in stream operations."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::ios_base::eofbit - end of file

`eofbit` is set when an input operation reaches the end of the file/stream. This is normal behavior at end-of-file but can indicate premature termination.

## Common Causes

```cpp
// Cause 1: Reading past end of file
std::ifstream file("small.txt");
char c;
while (file.get(c)) {
    // eofbit set when file ends
}

// Cause 2: Unexpected EOF
std::ifstream file("corrupted.dat");
int val;
file.read(reinterpret_cast<char*>(&val), sizeof(val));
if (file.eof()) {
    // incomplete read
}

// Cause 3: Pipe closed
std::cin >> val; // eofbit if stdin closed
```

## How to Fix

### Fix 1: Check eof() after operation

```cpp
std::ifstream file("data.txt");
int val;
file >> val;
if (file.eof()) {
    std::cerr << "Unexpected end of file" << std::endl;
} else if (file.fail()) {
    std::cerr << "Format error" << std::endl;
}
```

### Fix 2: Use while(getline) pattern

```cpp
std::string line;
while (std::getline(file, line)) {
    // process line — eof handled automatically
}
```

### Fix 3: Check for complete read

```cpp
file.read(buffer, expected_size);
if (file.gcount() != expected_size) {
    std::cerr << "Incomplete read" << std::endl;
}
```

## Related Errors

- [std::ios_base::failbit]({{< relref "/languages/cpp/ios-base-failbit" >}}) — format error.
- [std::ios_base::badbit]({{< relref "/languages/cpp/ios-base-badbit" >}}) — critical error.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream exception.
