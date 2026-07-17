---
title: "[Solution] C++ std::system_error - system category"
description: "Fix C++ std::system_error with system category. Handle Windows-specific error codes."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::system_error - system category

`std::system_error` with the system category wraps platform-specific error codes (Windows error codes on Windows, errno on POSIX).

## Common Causes

```cpp
// Cause 1: Windows API failure
HANDLE h = CreateFile("file.txt", ...); // INVALID_HANDLE_VALUE

// Cause 2: Winsock error
WSAStartup(MAKEWORD(2, 2), &wsaData); // may fail

// Cause 3: POSIX errno
std::error_code ec(errno, std::system_category());
```

## How to Fix

### Fix 1: Check error code

```cpp
try {
    // system call
} catch (const std::system_error& e) {
    if (e.code().category() == std::system_category()) {
        std::cerr << "System error: " << e.code().value() << std::endl;
    }
}
```

### Fix 2: Use platform-specific handling

```cpp
#ifdef _WIN32
DWORD err = GetLastError();
// Handle Windows error
#else
int err = errno;
// Handle POSIX error
#endif
```

### Fix 3: Use std::error_code

```cpp
std::error_code ec;
// ... operation that sets ec ...
if (ec) {
    std::cerr << ec.message() << std::endl;
}
```

## Related Errors

- [std::system_error - generic]({{< relref "/languages/cpp/system-error-generic" >}}) — generic errors.
- [std::filesystem_error]({{< relref "/languages/cpp/filesystem-error" >}}) — filesystem errors.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream errors.
