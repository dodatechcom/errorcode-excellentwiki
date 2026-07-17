---
title: "[Solution] C++ clang-tidy - lint error"
description: "Fix C++ clang-tidy lint errors. Address modernization and code quality issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# clang-tidy - lint error

clang-tidy is a Clang-based linter that finds common programming errors and suggests modernization improvements.

## Common Causes

```cpp
// Cause 1: Modernize use auto
std::vector<int>::iterator it = vec.begin(); // clang-tidy suggests auto

// Cause 2: Use nullptr instead of NULL
int* p = NULL; // clang-tidy: use nullptr

// Cause 3: Use range-based for
for (int i = 0; i < vec.size(); i++) {
    process(vec[i]); // clang-tidy: use range-based for
}
```

## How to Fix

### Fix 1: Run clang-tidy

```bash
clang-tidy src/*.cpp -- -std=c++17
```

### Fix 2: Apply fixes automatically

```bash
clang-tidy src/*.cpp --fix -- -std=c++17
```

### Fix 3: Fix specific checks

```cpp
// modernize-use-auto
auto it = vec.begin(); // use auto

// modernize-use-nullptr
int* p = nullptr; // use nullptr

// modernize-loop-convert
for (auto& item : vec) {
    process(item);
}
```

## Related Errors

- [cppcheck - static analysis]({{< relref "/languages/cpp/cppcheck-error" >}}) — cppcheck errors.
- [AddressSanitizer]({{< relref "/languages/cpp/sanitizers-address" >}}) — memory errors.
- [Valgrind - memory error]({{< relref "/languages/cpp/valgrind-error" >}}) — memory errors.
