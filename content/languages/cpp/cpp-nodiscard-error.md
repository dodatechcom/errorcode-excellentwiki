---
title: "[Solution] C++ [[nodiscard]] Error — How to Fix"
description: "Fix C++ [[nodiscard]] attribute errors including ignored return values, incorrect attribute placement, and compilation warnings in C++17 code."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ [[nodiscard]] Error — How to Fix

`[[nodiscard]]` (C++17) warns when a function's return value is ignored, catching bugs from discarded error codes, moved resources, or expensive computations whose results are needed.

## Why It Happens

nodiscard errors occur when callers intentionally ignore return values without suppression, when `[[nodiscard]]` is placed incorrectly on the declaration, when template functions with nodiscard return types are instantiated but results discarded, or when lambdas return nodiscard types.

## Common Error Messages

1. `warning: ignoring return value of function declared with '[[nodiscard]]'`
2. `error: 'nodiscard' attribute cannot be applied to non-functions`
3. `warning: structured binding discards 'nodiscard' return value`
4. `warning: ignoring 'nodiscard' value of type`

## How to Fix It

### Fix 1: Handle Return Values

```cpp
#include <iostream>
#include <system_error>

// CORRECT — [[nodiscard]] catches discarded results
[[nodiscard]] std::error_code open_file(const char* path) {
    // simulation
    return std::error_code(0, std::system_category());
}

int main() {
    // WRONG — triggers warning
    // open_file("test.txt");

    // CORRECT — check or explicitly discard
    auto ec = open_file("test.txt");
    if (ec) {
        std::cout << "Error: " << ec.message() << "\n";
    }

    return 0;
}
```

### Fix 2: Use [[maybe_unused]] to Suppress Warning

```cpp
#include <iostream>

[[nodiscard]] int compute(int x) { return x * 2; }

int main() {
    // CORRECT — explicitly mark as unused if intentional
    [[maybe_unused]] auto result = compute(42);

    // Or cast to void
    (void)compute(42);

    return 0;
}
```

### Fix 3: Apply [[nodiscard]] to Structs

```cpp
#include <iostream>

// CORRECT — nodiscard on struct warns when returned value ignored
struct [[nodiscard]] Error {
    bool failed;
    const char* message;
};

Error do_work() {
    return {false, "success"};
}

int main() {
    // WRONG — triggers warning
    // do_work();

    // CORRECT — handle the result
    auto result = do_work();
    if (result.failed) {
        std::cout << result.message << "\n";
    }

    return 0;
}
```

### Fix 4: Use [[nodiscard("reason")]] with Messages

```cpp
#include <iostream>

// CORRECT — provide reason string
[[nodiscard("must check allocation result")]]
void* safe_alloc(size_t size) {
    return operator new(size);
}

int main() {
    // Warning will include the reason string
    [[maybe_unused]] void* p = safe_alloc(1024);
    return 0;
}
```

## Common Scenarios

- **Error codes**: Functions returning `std::error_code` or errno should always be checked.
- **Moved resources**: Ignoring `std::move` results can leave sources in valid-but-empty states.
- **Performance**: Ignoring `[[nodiscard]]` on expensive functions wastes computation.

## Prevent It

1. Use `[[nodiscard]]` on functions where ignoring the return value is likely a bug.
2. Use `[[maybe_unused]]` or `(void)` cast when intentionally discarding a nodiscard value.
3. Provide reason strings: `[[nodiscard("check error code")]]` for better diagnostics.

## Related Errors

- [Unreachable error]({{< relref "/languages/cpp/cpp-unreachable-error" >}}) — dead code assumptions.
- [Noexcept error]({{< relref "/languages/cpp/cpp-noexcept-error" >}}) — exception specification issues.
- [Compiler warnings]({{< relref "/languages/cpp/cpp-clang-tidy-error.md" >}}) — static analysis issues.
