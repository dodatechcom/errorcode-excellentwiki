---
title: "CTAD Deduction Failure - Fix"
description: "Fix Class Template Argument Deduction (CTAG) failures by adding deduction guides, using explicit template args, or fixing constructor matching."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 954
---

# CTAD Deduction Failure - Fix

Class Template Argument Deduction (CTAD, C++17) lets the compiler deduce template arguments from the constructor. Deduction failure occurs when the compiler cannot infer the template parameters, or when deduction is ambiguous.

## Common Causes

```cpp
// No deduction possible: no matching constructor
template <typename T>
struct Box {
    T value;
    Box(T v) : value(v) {}
    Box() = default; // non-deducible
};

int main() {
    Box b; // error: cannot deduce T (no constructor args)
    return 0;
}
```

```cpp
// Ambiguous deduction
template <typename T, typename U>
struct Pair {
    Pair(T first, U second) {}
};

int main() {
    Pair p{1, 2.0}; // OK: deduces Pair<int, double>

    // But if there are two constructors:
    // Pair(T) and Pair(U) -- ambiguous
    return 0;
}
```

```cpp
// Non-deducible template parameters
template <typename T, typename U>
struct Wrapper {
    Wrapper(T val) {}
};

int main() {
    Wrapper w(42); // error: U cannot be deduced
    return 0;
}
```

```cpp
// Initializer list ambiguity
template <typename T>
struct Container {
    Container(std::initializer_list<T> il) {}
};

int main() {
    Container c{1, 2, 3}; // OK: deduces Container<int>
    // But {1, 2.0, 3} fails: can't deduce T
    return 0;
}
```

## How to Fix

### Fix 1: Add a deduction guide

```cpp
template <typename T>
struct Box {
    T value;
    Box(T v) : value(v) {}
    Box() = default;
};

// Deduction guide: if no args, default to int
Box() -> Box<int>;

int main() {
    Box b; // now OK: Box<int>
    Box b2(42); // still OK: Box<int>
    Box b3(3.14); // Box<double>
    return 0;
}
```

### Fix 2: Provide default template arguments

```cpp
template <typename T, typename U = T>
struct Wrapper {
    Wrapper(T val) : value(val) {}
    T value;
    U extra{};
};

int main() {
    Wrapper w(42); // OK: deduces Wrapper<int, int>
    return 0;
}
```

### Fix 3: Use explicit template arguments

```cpp
template <typename T, typename U>
struct Pair {
    Pair(T first, U second) {}
};

int main() {
    Pair<int, double> p{1, 2.0}; // explicit
    return 0;
}
```

### Fix 4: Constrain deduction with concepts

```cpp
#include <concepts>

template <typename T>
struct Number {
    T value;
    Number(std::integral auto v) : value(v) {}
};

int main() {
    Number n{42}; // OK: T = int
    // Number n{3.14}; // error: double doesn't satisfy integral
    return 0;
}
```

## Examples

```cpp
#include <vector>
#include <string>

template <typename Key, typename Value>
struct Dict {
    std::vector<std::pair<Key, Value>> data;
    Dict(std::initializer_list<std::pair<Key, Value>> il) : data(il) {}
};

// Deduction guide handles pairs
template <typename K, typename V>
Dict(std::pair<K, V>) -> Dict<K, V>;

template <typename K, typename V>
Dict(std::initializer_list<std::pair<K, V>>) -> Dict<K, V>;

int main() {
    Dict d = {{"hello", 1}, {"world", 2}}; // Dict<const char*, int>
    return 0;
}
```

## Related Errors

- [constexpr-function-limit]({{< relref "/languages/cpp/constexpr-function-limit" >}})
- [consteval-call-constexpr]({{< relref "/languages/cpp/consteval-call-constexpr" >}})
- [constinit-error]({{< relref "/languages/cpp/constinit-error" >}})
