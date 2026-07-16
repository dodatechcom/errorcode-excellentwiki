---
title: "[Solution] C++ std::bind Deprecated — Replace with Lambda"
description: "Replace std::bind with lambdas in C++11 and later. Migration guide with code examples."
deprecated_function: "std::bind"
replacement_function: "lambda"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["bind", "lambda", "functional", "cpp11", "std::bind"]
weight: 5
---

# [Solution] C++ std::bind Deprecated — Replace with Lambda

`std::bind` is not formally deprecated in the C++ standard, but it is widely discouraged in modern C++ style guides (C++ Core Guidelines, Google Style Guide) because lambdas are more readable, more efficient, and more flexible. `std::bind` has surprising semantics with nested binds, references, and const-correctness.

## What You'll See

Compiler warnings with `-Wdeprecated` in some implementations, and lint warnings from modern linters:

```
warning: 'std::bind' is discouraged: use lambdas for better readability
```

## Why Discouraged

`std::bind` is discouraged because:

- **Nested bind expressions are confusing**: `bind(f, bind(g, _1))` is hard to read and debug.
- **Reference issues**: `std::bind(f, std::ref(x))` is needed to pass by reference; lambdas capture by reference naturally.
- **Performance**: `std::bind` may not be inlined by compilers, while lambdas are.
- **Const-correctness**: Bound objects are always const, which can cause surprises.
- **Placeholder ambiguity**: `_1`, `_2` from `std::placeholders` are less clear than named lambda captures.

## Old Code (Discouraged)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

void print_with_prefix(int prefix, int value) {
    std::cout << prefix << ": " << value << " ";
}

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    int prefix = 100;

    std::for_each(nums.begin(), nums.end(),
                   std::bind(print_with_prefix, std::ref(prefix),
                             std::placeholders::_1));

    std::cout << std::endl;
    return 0;
}
```

## New Code — Lambda Replacement

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

void print_with_prefix(int prefix, int value) {
    std::cout << prefix << ": " << value << " ";
}

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    int prefix = 100;

    // Lambda — clear, efficient, no std::ref needed
    std::for_each(nums.begin(), nums.end(),
                   [&prefix](int value) {
                       print_with_prefix(prefix, value);
                   });

    std::cout << std::endl;
    return 0;
}
```

## New Code — Lambda for Member Function Binding

```cpp
#include <functional>
#include <vector>
#include <iostream>

class Widget {
    int id;
public:
    explicit Widget(int i) : id(i) {}
    void print() const { std::cout << "Widget(" << id << ") "; }
};

int main() {
    std::vector<Widget> widgets = {Widget(1), Widget(2), Widget(3)};

    // Old: std::for_each(..., std::bind(&Widget::print, std::placeholders::_1));
    // New: range-based for is simplest
    for (const auto& w : widgets) {
        w.print();
    }
    std::cout << std::endl;

    // Or with algorithm
    std::for_each(widgets.begin(), widgets.end(),
                   [](const Widget& w) { w.print(); });

    return 0;
}
```

## Migration Steps

1. **Find all std::bind usage**:

```bash
grep -rn "\bstd::bind\b\|\bbind(" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `std::bind(f, args...)` with `[args...](params...) { return f(params...); }`**.

3. **Replace `std::placeholders::_N` with named lambda parameters**.

4. **Remove `std::ref()` wrappers** — lambdas capture by reference naturally.

5. **For simple cases**, use range-based for loops instead of `std::for_each` with bind.

6. **Keep `std::bind` only** when you need to store a bind expression in a type-erased container (rare).

## Related Deprecations

- [bind1st → lambda]({{< relref "/deprecated/cpp/bind1st" >}}) — C++03 binders.
- [bind2nd → lambda]({{< relref "/deprecated/cpp/bind2nd" >}}) — C++03 binders.
- [not1 → lambda]({{< relref "/deprecated/cpp/not1" >}}) — C++03 negators.
