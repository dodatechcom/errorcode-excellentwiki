---
title: "[Solution] C++ consteval Error — How to Fix"
description: "Fix C++ consteval errors including immediate function violations, non-constexpr argument failures, and consteval vs constexpr usage mistakes in C++20."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ consteval Error — How to Fix

C++20 `consteval` creates immediate functions that must be evaluated at compile time, but errors occur when called at runtime, when arguments aren't constexpr-constructible, or when `consteval` is confused with `constexpr`.

## Why It Happens

consteval errors arise when calling a consteval function from runtime code, when arguments passed to consteval functions are runtime values, when consteval functions call non-constexpr functions, when consteval is used on virtual functions, or when the compiler can't evaluate the function at compile time.

## Common Error Messages

1. `error: call to immediate function is not a constant expression`
2. `error: 'constexpr' variable cannot have 'consteval' function type`
3. `error: consteval function cannot be virtual`
4. `error: expression is not a constant expression`

## How to Fix It

### Fix 1: Call consteval Only in Constant Contexts

```cpp
#include <iostream>

// CORRECT — consteval for compile-time only
consteval int square(int x) {
    return x * x;
}

// CORRECT — constexpr works at compile time AND runtime
constexpr int cube(int x) {
    return x * x * x;
}

int main() {
    // consteval works at compile time
    constexpr int sq = square(5);  // OK
    std::cout << sq << "\n";       // 25

    // constexpr works everywhere
    int runtime_val = 3;
    int c = cube(runtime_val);     // OK — runtime
    std::cout << c << "\n";        // 27

    return 0;
}
```

### Fix 2: Ensure Arguments are Constant Expressions

```cpp
#include <iostream>

consteval int compute(int x, int y) {
    return x + y;
}

int main() {
    constexpr int a = 10;
    constexpr int b = 20;

    // CORRECT — arguments are constexpr
    constexpr int result = compute(a, b);
    std::cout << result << "\n";

    // WRONG — runtime value can't be passed to consteval
    // int c = 30;
    // constexpr int bad = compute(a, c);  // error

    return 0;
}
```

### Fix 3: Use consteval for String Processing

```cpp
#include <iostream>
#include <string_view>

// CORRECT — consteval for compile-time string processing
consteval size_t string_length(const char* str) {
    size_t len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

consteval bool is_palindrome(const char* str, size_t len) {
    for (size_t i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) return false;
    }
    return true;
}

int main() {
    constexpr size_t len = string_length("racecar");
    constexpr bool is_pal = is_palindrome("racecar", len);
    static_assert(is_pal);

    std::cout << "Length: " << len << "\n";
    std::cout << "Is palindrome: " << std::boolalpha << is_pal << "\n";

    return 0;
}
```

### Fix 4: Use consteval vs constexpr Correctly

```cpp
#include <iostream>

// consteval — MUST be compile-time
consteval int compile_time_only(int x) { return x + 1; }

// constexpr — CAN be compile-time or runtime
constexpr int flexible(int x) { return x + 1; }

int main() {
    // Both work at compile time
    constexpr int a = compile_time_only(5);
    constexpr int b = flexible(5);

    // Only constexpr works at runtime
    int x = 10;
    int c = flexible(x);        // OK
    // int d = compile_time_only(x);  // error: not constant

    std::cout << a << " " << b << " " << c << "\n";

    return 0;
}
```

## Common Scenarios

- **Runtime calls**: Calling consteval functions with runtime arguments fails.
- **Virtual functions**: `consteval` cannot be applied to virtual member functions.
- **Template instantiation**: consteval functions in templates may fail when instantiated with non-constexpr types.

## Prevent It

1. Use `consteval` only for functions that MUST run at compile time (e.g., static_assert checks).
2. Use `constexpr` for functions that should run at compile time when possible but can run at runtime.
3. Ensure all arguments to consteval functions are compile-time constants.

## Related Errors

- [Constexpr error]({{< relref "/languages/cpp/constexpr-error" >}}) — constexpr evaluation issues.
- [Concept error]({{< relref "/languages/cpp/cpp-concepts-error" >}}) — constraint failures.
- [If constexpr error]({{< relref "/languages/cpp/cpp-if-constexpr-error" >}}) — compile-time branching.
