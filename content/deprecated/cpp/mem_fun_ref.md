---
title: "[Solution] C++ mem_fun_ref() Deprecated — Replace with std::function"
description: "Replace std::mem_fun_ref with lambdas or std::function in C++11 and later. Migration guide with code examples."
deprecated_function: "std::mem_fun_ref"
replacement_function: "std::function"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C++ mem_fun_ref() Deprecated — Replace with std::function

`std::mem_fun_ref` was deprecated in C++11 and removed in C++17 because lambdas provide a clearer, more flexible way to call member functions through algorithms. `mem_fun_ref` wraps a member function into a unary function object that takes a reference.

## What You'll See

In C++11/14:

```
warning: 'std::mem_fun_ref' is deprecated: Use lambdas or std::function instead
```

In C++17:

```
error: 'mem_fun_ref' is not a member of 'std'
```

## Why Deprecated

`std::mem_fun_ref` was deprecated because:

- **Limited functionality**: Only works with the exact member function signature.
- **Cannot pass arguments**: Cannot bind additional arguments to the member function.
- **Replaced by lambdas**: `[](const auto& obj) { obj.method(); }` is clearer and more flexible.
- **Poor readability**: `std::for_each(v.begin(), v.end(), std::mem_fun_ref(&Widget::print))` vs a simple range-for loop.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

class Widget {
    std::string name;
public:
    explicit Widget(const std::string& n) : name(n) {}
    void print() const { std::cout << name << " "; }
    const std::string& getName() const { return name; }
};

int main() {
    std::vector<Widget> widgets = {
        Widget("A"), Widget("B"), Widget("C")
    };

    // Print each widget using mem_fun_ref
    std::for_each(widgets.begin(), widgets.end(),
                   std::mem_fun_ref(&Widget::print));
    std::cout << std::endl;

    return 0;
}
```

## New Code — Lambda Replacement

```cpp
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

class Widget {
    std::string name;
public:
    explicit Widget(const std::string& n) : name(n) {}
    void print() const { std::cout << name << " "; }
    const std::string& getName() const { return name; }
};

int main() {
    std::vector<Widget> widgets = {
        Widget("A"), Widget("B"), Widget("C")
    };

    // Range-based for — simplest and most readable
    for (const auto& w : widgets) {
        w.print();
    }
    std::cout << std::endl;

    // Or with algorithm and lambda
    std::for_each(widgets.begin(), widgets.end(),
                   [](const Widget& w) { w.print(); });

    return 0;
}
```

## New Code — Lambda with Argument Binding

```cpp
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

class Widget {
    std::string name;
    int value;
public:
    Widget(const std::string& n, int v) : name(n), value(v) {}
    void printWithPrefix(const std::string& prefix) const {
        std::cout << prefix << name << "=" << value << " ";
    }
};

int main() {
    std::vector<Widget> widgets = {
        Widget("x", 1), Widget("y", 2), Widget("z", 3)
    };

    // Lambda with argument binding — mem_fun_ref cannot do this
    std::string prefix = "Widget: ";
    std::for_each(widgets.begin(), widgets.end(),
                   [&prefix](const Widget& w) {
                       w.printWithPrefix(prefix);
                   });
    std::cout << std::endl;

    return 0;
}
```

## Migration Steps

1. **Find all mem_fun_ref usage**:

```bash
grep -rn "\bmem_fun_ref\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace with range-based for loops** for simple iteration.

3. **Replace with lambdas** in algorithms: `[](const T& obj) { obj.method(); }`.

4. **For complex cases**, lambdas can capture variables and pass additional arguments.

5. **Remove `<functional>` include** if no other binders are used.

## Related Deprecations

- [mem_fun → std::function]({{< relref "/deprecated/cpp/mem_fun" >}}) — pointer-based version.
- [ptr_fun → std::function]({{< relref "/deprecated/cpp/ptr_fun" >}}) — free function wrapper.
- [not1 → lambda]({{< relref "/deprecated/cpp/not1" >}}) — negation modernization.
