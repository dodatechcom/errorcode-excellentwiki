---
title: "[Solution] C++ mem_fun() Deprecated — Replace with std::function"
description: "Replace std::mem_fun with lambdas or std::function in C++11 and later. Migration guide with code examples."
deprecated_function: "std::mem_fun"
replacement_function: "std::function"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["mem_fun", "std::function", "lambda", "member-function", "cpp11"]
weight: 5
---

# [Solution] C++ mem_fun() Deprecated — Replace with std::function

`std::mem_fun` was deprecated in C++11 and removed in C++17 because it was unnecessary with lambdas and `std::function`. It wrapped a member function pointer into a binary function object that takes a pointer as the first argument.

## What You'll See

In C++11/14:

```
warning: 'std::mem_fun' is deprecated: Use lambdas or std::function instead
```

In C++17:

```
error: 'mem_fun' is not a member of 'std'
```

## Why Deprecated

`std::mem_fun` was deprecated because:

- **Confusing API**: Takes a pointer, not a reference, which is error-prone.
- **Limited functionality**: Only works with pointer containers.
- **Replaced by lambdas**: `[](auto* obj) { obj->method(); }` is clearer.
- **std::function is more general**: Can wrap any callable.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

class Widget {
    int value;
public:
    explicit Widget(int v) : value(v) {}
    int getValue() const { return value; }
};

int main() {
    std::vector<Widget*> widgets = {
        new Widget(1), new Widget(2), new Widget(3)
    };

    // Print each widget's value using mem_fun
    std::for_each(widgets.begin(), widgets.end(),
                   std::bind1st(std::mem_fun(&Widget::getValue), ???));

    for (auto* w : widgets) {
        delete w;
    }
    return 0;
}
```

## New Code — Lambda Replacement

```cpp
#include <algorithm>
#include <vector>
#include <iostream>
#include <memory>

class Widget {
    int value;
public:
    explicit Widget(int v) : value(v) {}
    int getValue() const { return value; }
};

int main() {
    std::vector<std::unique_ptr<Widget>> widgets;
    widgets.push_back(std::make_unique<Widget>(1));
    widgets.push_back(std::make_unique<Widget>(2));
    widgets.push_back(std::make_unique<Widget>(3));

    // Print each widget's value — clear and safe
    for (const auto& w : widgets) {
        std::cout << w->getValue() << " ";
    }
    std::cout << std::endl;

    // Or with algorithms
    std::for_each(widgets.begin(), widgets.end(),
                   [](const std::unique_ptr<Widget>& w) {
                       std::cout << w->getValue() << " ";
                   });

    return 0;
}
```

## Migration Steps

1. **Find all mem_fun usage**:

```bash
grep -rn "\bmem_fun\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace with range-based for loops** when iterating over containers.

3. **Replace with lambdas** when using algorithms: `[](auto* obj) { obj->method(); }`.

4. **Switch to smart pointers** to avoid raw pointer management.

5. **For member function pointers stored in variables**, use `std::function<void(Widget*)>`.

## Related Deprecations

- [mem_fun_ref → std::function]({{< relref "/deprecated/cpp/mem_fun_ref" >}}) — reference-based version.
- [ptr_fun → std::function]({{< relref "/deprecated/cpp/ptr_fun" >}}) — free function wrapper.
- [auto_ptr → unique_ptr]({{< relref "/deprecated/cpp/auto_ptr" >}}) — smart pointer modernization.
