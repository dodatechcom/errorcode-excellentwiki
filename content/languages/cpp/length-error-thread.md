---
title: "[Solution] C++ std::length_error - thread name too long"
description: "Fix C++ std::length_error when thread name exceeds platform limits."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::length_error - thread name too long

`std::length_error` can occur when setting a thread name that exceeds the platform's maximum allowed length (typically 16 characters on Linux for pthread_setname_np).

## Common Causes

```cpp
// Cause 1: Thread name too long
std::thread t([]{ /* work */ });
pthread_setname_np(t.native_handle(), "this-is-a-very-long-thread-name"); // throws

// Cause 2: Platform limit exceeded
std::string name(100, 'x');
pthread_setname_np(t.native_handle(), name.c_str()); // may fail
```

## How to Fix

### Fix 1: Truncate name

```cpp
std::string name = "very-long-thread-name";
if (name.length() > 15) {
    name = name.substr(0, 15);
}
pthread_setname_np(t.native_handle(), name.c_str());
```

### Fix 2: Use safe wrapper

```cpp
void set_thread_name(std::thread& t, const std::string& name) {
    std::string safe = name.substr(0, 15);
    pthread_setname_np(t.native_handle(), safe.c_str());
}
```

### Fix 3: Use platform-specific limits

```cpp
#ifdef __linux__
constexpr size_t MAX_THREAD_NAME = 15;
#elif defined(__APPLE__)
constexpr size_t MAX_THREAD_NAME = 63;
#endif
```

## Related Errors

- [std::system_error]({{< relref "/languages/cpp/system-error-generic" >}}) — system errors.
- [std::thread creation failure]({{< relref "/languages/cpp/system-error-generic" >}}) — thread errors.
- [std::length_error - string]({{< relref "/languages/cpp/length-error-string" >}}) — string too long.
