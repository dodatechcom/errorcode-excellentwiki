---
title: "[Solution] C++ std::ios_base::failure — Stream I/O Error Fix"
description: "Fix C++ std::ios_base::failure when stream operations fail. Handle badbit, failbit, and stream state errors in I/O operations."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["ios-failure", "iostream", "stream", "file-io"]
weight: 50
---

# [Solution] C++ std::ios_base::failure — Stream I/O Error Fix

A `std::ios_base::failure` (also `std::ios_base::failure`) is thrown when a stream I/O operation fails and `exceptions()` has been set to throw on `badbit` or `failbit`. By default, streams do not throw on errors — they set error state flags instead. But when you enable exception throwing via `exceptions()`, any stream error throws `std::ios_base::failure`.

## Why std::ios_base::failure Occurs

Common causes include reading from an already-exhausted stream, writing to a closed or read-only stream, file I/O errors during stream operations, stream state corruption, and setting `exceptions()` to throw on `badbit` or `failbit`.

## Wrong: Not Handling Stream Errors After Enabling Exceptions

```cpp
// WRONG — exceptions() causes failure to throw
#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("/nonexistent.txt");
    file.exceptions(std::ios::badbit | std::ios::failbit);

    std::string content;
    file >> content;  // throws std::ios_base::failure
    return 0;
}
```

## Correct: Catch ios_base::failure and Inspect Error

```cpp
// CORRECT — catch and inspect stream failure
#include <fstream>
#include <iostream>
#include <ios>

int main() {
    std::ifstream file("/nonexistent.txt");
    file.exceptions(std::ios::badbit | std::ios::failbit);

    try {
        std::string content;
        file >> content;
    } catch (const std::ios_base::failure& e) {
        std::cerr << "Stream failure: " << e.what() << std::endl;
        std::cerr << "Error code: " << e.code().message() << std::endl;
    }
    return 0;
}
```

## Check Stream State Without Exceptions

```cpp
// CORRECT — check state flags instead of throwing
#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("/nonexistent.txt");

    if (!file.is_open()) {
        std::cerr << "Failed to open file" << std::endl;
        return 1;
    }

    std::string content;
    if (!(file >> content)) {
        if (file.eof()) {
            std::cerr << "End of file reached" << std::endl;
        } else if (file.fail()) {
            std::cerr << "Format error" << std::endl;
        } else if (file.bad()) {
            std::cerr << "I/O error" << std::endl;
        }
        return 1;
    }

    std::cout << content << std::endl;
    return 0;
}
```

## Safe Stream Operations with Reset

```cpp
// CORRECT — clear stream state and handle errors
#include <sstream>
#include <iostream>
#include <string>

int main() {
    std::istringstream stream("hello 42 world");

    int value;
    std::string word;

    // Read integer — may fail
    if (stream >> value) {
        std::cout << "Integer: " << value << std::endl;
    } else {
        stream.clear();  // Clear error state
        stream >> word;  // Now read as string
        std::cout << "Word: " << word << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check `is_open()` before reading | When opening files |
| Use `fail()`, `bad()`, `eof()` checks | When not using exceptions |
| Catch `ios_base::failure` | When `exceptions()` is enabled |
| Call `clear()` before retrying | When recovering from stream errors |

## Related Errors

- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::filesystem::filesystem_error]({{< relref "/languages/cpp/filesystemerror" >}}) — filesystem-specific failures.
- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — OS-level error codes.
