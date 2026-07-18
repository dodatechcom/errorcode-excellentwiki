---
title: "[Solution] C++ System Error Error — How to Fix"
description: "Fix C++ std::system_error errors including missing error codes, incorrect error_category usage, and platform-specific error handling failures."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ System Error Error — How to Fix

`std::system_error` wraps platform-specific error codes into C++ exceptions, but incorrect error category usage, missing error code checks, and platform assumptions lead to cryptic failures and unhandled system errors.

## Why It Happens

System error issues arise when system calls fail without checking `errno` or return values, when `std::error_code` is constructed with the wrong category, when platform-specific errors aren't handled across OS boundaries, or when error codes are compared incorrectly across categories.

## Common Error Messages

1. `std::system_error: generic_category: no such file or directory`
2. `error: 'std::system_error' not caught — unhandled system error`
3. `error: comparing error codes from different categories`
4. `error: system_error thrown with non-portable error code`

## How to Fix It

### Fix 1: Check System Call Return Values

```cpp
#include <system_error>
#include <iostream>
#include <fstream>

int main() {
    // CORRECT — catch system_error from file operations
    try {
        std::ifstream file("/nonexistent/path.txt");
        if (!file.is_open()) {
            throw std::system_error(
                std::error_code(errno, std::system_category()),
                "Failed to open file"
            );
        }
    } catch (const std::system_error& e) {
        std::cout << "Error code: " << e.code().value() << "\n";
        std::cout << "Message: " << e.what() << "\n";
    }
    return 0;
}
```

### Fix 2: Use the Correct Error Category

```cpp
#include <system_error>
#include <iostream>

int main() {
    // CORRECT — use appropriate category for the error type
    std::error_code ec1(2, std::system_category());    // POSIX error
    std::error_code ec2(2, std::generic_category());   // generic C++ error

    std::cout << "system_category[2]: " << ec1.message() << "\n";
    std::cout << "generic_category[2]: " << ec2.message() << "\n";

    // WRONG — comparing codes from different categories
    // if (ec1 == ec2) { ... }  // always false

    // CORRECT — check category before comparing
    if (ec1.category() == std::system_category() &&
        ec1.value() == 2) {
        std::cout << "POSIX error: " << ec1.message() << "\n";
    }
    return 0;
}
```

### Fix 3: Create Custom Error Codes

```cpp
#include <system_error>
#include <iostream>

enum class AppError {
    ok = 0,
    file_not_found = 1,
    permission_denied = 2,
    timeout = 3
};

class app_error_category : public std::error_category {
public:
    const char* name() const noexcept override { return "app_error"; }

    std::string message(int ev) const override {
        switch (static_cast<AppError>(ev)) {
            case AppError::ok: return "Success";
            case AppError::file_not_found: return "File not found";
            case AppError::permission_denied: return "Permission denied";
            case AppError::timeout: return "Timeout";
            default: return "Unknown error";
        }
    }
};

const app_error_category& app_category() {
    static app_error_category cat;
    return cat;
}

std::error_code make_error_code(AppError e) {
    return {static_cast<int>(e), app_category()};
}

int main() {
    std::error_code ec = make_error_code(AppError::timeout);
    std::cout << "Error: " << ec.message() << "\n";
    return 0;
}
```

### Fix 4: Handle Platform-Specific Errors

```cpp
#include <system_error>
#include <iostream>

void platform_operation() {
#ifdef _WIN32
    throw std::system_error(
        std::error_code(ERROR_ACCESS_DENIED, std::system_category()),
        "Windows access denied"
    );
#else
    throw std::system_error(
        std::error_code(EACCES, std::system_category()),
        "Permission denied"
    );
#endif
}

int main() {
    try {
        platform_operation();
    } catch (const std::system_error& e) {
        std::cout << "Platform error: " << e.what() << "\n";
        std::cout << "Code: " << e.code().value() << "\n";
    }
    return 0;
}
```

## Common Scenarios

- **Cross-platform code**: Error code values differ between Windows and POSIX — use category-aware comparisons.
- **Missing error checks**: System calls return error codes that must be checked immediately.
- **Wrong category**: Using `std::generic_category` for POSIX errors produces incorrect messages.

## Prevent It

1. Always check `std::system_error::code().category()` before comparing error codes.
2. Use RAII wrappers (like `std::fstream`) to avoid manual error code checking.
3. Test error handling on all target platforms — error codes are platform-specific.

## Related Errors

- [System error]({{< relref "/languages/cpp/system-error-system" >}}) — system call failures.
- [Stdexcept error]({{< relref "/languages/cpp/cpp-stdexcept-error" >}}) — standard exception issues.
- [Filesystem error]({{< relref "/languages/cpp/filesystemerror" >}}) — filesystem operation failures.
