---
title: "[Solution] C++20 Concept Error — Concept Constraint Fix"
description: "Fix C++20 concept constraint errors when template arguments don't satisfy required concepts. Learn concept definition and debugging."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++20 Concept Error — Concept Constraint Fix

A concept error occurs when a template argument does not satisfy the requirements of a C++20 concept. The compiler produces a clear error message indicating which constraint was not satisfied. This replaces SFINAE-based error messages with more readable diagnostics.

## Why Concept Errors Occur

Common causes include passing a type that doesn't satisfy the concept's requirements, incorrect concept definition (missing required expressions), constraints that are too strict for the intended use, and using concepts from different language versions.

## Wrong: Passing Wrong Type to Concept-Constrained Template

```cpp
// WRONG — compilation error: constraint not satisfied
#include <concepts>
#include <iostream>

template <std::integral T>
T add(T a, T b) {
    return a + b;
}

int main() {
    auto result = add(3.5, 4.5);  // error — double is not integral
    std::cout << result << std::endl;
    return 0;
}
```

## Correct: Use Correct Types or Define Flexible Concepts

```cpp
// CORRECT — use matching types
#include <concepts>
#include <iostream>

template <std::integral T>
T add(T a, T b) {
    return a + b;
}

template <std::floating_point T>
T add(T a, T b) {
    return a + b;
}

int main() {
    std::cout << add(3, 4) << std::endl;
    std::cout << add(3.5, 4.5) << std::endl;
    return 0;
}
```

## Define Custom Concepts

```cpp
// CORRECT — define concepts for your domain
#include <concepts>
#include <iostream>
#include <string>

template <typename T>
concept Printable = requires(T t, std::ostream& os) {
    { os << t } -> std::convertible_to<std::ostream&>;
};

template <Printable T>
void print(const T& val) {
    std::cout << val << std::endl;
}

struct Point {
    int x, y;
};

std::ostream& operator<<(std::ostream& os, const Point& p) {
    return os << "(" << p.x << ", " << p.y << ")";
}

int main() {
    print(42);
    print("hello");
    print(Point{1, 2});
    return 0;
}
```

## Use Requires Expressions

```cpp
// CORRECT — requires expressions for inline constraints
#include <concepts>
#include <iostream>
#include <vector>

template <typename T>
concept Container = requires(T c) {
    typename T::value_type;
    typename T::iterator;
    { c.begin() } -> std::same_as<typename T::iterator>;
    { c.end() } -> std::same_as<typename T::iterator>;
    { c.size() } -> std::convertible_to<std::size_t>;
};

template <Container C>
void print_all(const C& c) {
    for (const auto& val : c) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> v = {1, 2, 3};
    print_all(v);
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use standard concepts (`std::integral`, etc.) | When they match your requirements |
| Define custom concepts | When domain-specific constraints are needed |
| Use requires expressions | For complex inline constraints |
| Check compiler error messages | Concepts provide clear diagnostics |

## Related Errors

- [template instantiation error]({{< relref "/languages/cpp/template-error" >}}) — template issues.
- [constexpr evaluation]({{< relref "/languages/cpp/constexpr-error" >}}) — constexpr failures.
- [std::ranges error]({{< relref "/languages/cpp/ranges-error" >}}) — ranges algorithm errors.
