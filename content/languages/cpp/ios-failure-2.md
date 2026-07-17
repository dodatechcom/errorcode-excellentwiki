---
title: "[Solution] C++ std::ios_base::failure — Stream Exception Handling Fix"
description: "Fix C++ std::ios_base::failure when streams throw on badbit or failbit. Learn stream error state management and exception-safe I/O."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::ios_base::failure — Stream Exception Handling Fix

A `std::ios_base::failure` is thrown when a stream I/O operation fails and `exceptions()` has been configured to throw on `badbit` or `failbit`. Streams do not throw by default — they set error flags instead. When you enable exception throwing via `exceptions()`, any stream error triggers this exception.

## Why std::ios_base::failure Occurs

Common causes include reading from a non-existent or already-closed file stream, writing to a read-only stream, formatting errors (e.g., extracting an int from "hello"), calling `exceptions()` with `badbit | failbit` flags, and stream state corruption from bad I/O operations.

## Wrong: Enabling Stream Exceptions Without try-catch

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

## Correct: Catch ios_base::failure When Using Stream Exceptions

```cpp
// CORRECT — catch stream failure with error code
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
// CORRECT — check stream flags instead of throwing
#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("/nonexistent.txt");

    if (!file.is_open()) {
        std::cerr << "Failed to open file" << std::endl;
        return 1;
    }

    int value;
    if (!(file >> value)) {
        if (file.eof()) {
            std::cerr << "End of file reached" << std::endl;
        } else if (file.fail()) {
            std::cerr << "Format error" << std::endl;
        } else if (file.bad()) {
            std::cerr << "I/O error" << std::endl;
        }
        return 1;
    }

    std::cout << "Read: " << value << std::endl;
    return 0;
}
```

## Clear and Retry After Stream Error

```cpp
// CORRECT — clear error state and retry
#include <sstream>
#include <iostream>
#include <string>

int main() {
    std::istringstream stream("hello 42 world");

    int value;
    std::string word;

    if (stream >> value) {
        std::cout << "Integer: " << value << std::endl;
    } else {
        stream.clear();
        stream >> word;
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

- [std::filesystem::filesystem_error]({{< relref "/languages/cpp/filesystemerror" >}}) — filesystem-specific failures.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::system_error]({{< relref "/languages/cpp/systemerror" >}}) — OS-level error codes.
