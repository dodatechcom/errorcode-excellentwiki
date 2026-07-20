---
title: "[Solution] C++ Undefined Reference to Template — Linker Fix"
description: "Fix undefined reference to template function errors with explicit instantiation, header definitions, and proper template export."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-error"]
weight: 903
---

# C++ Undefined Reference to Template — Linker Fix

When the linker reports an undefined reference to a template function or class, it means the compiler generated a call to a template instantiation that was never actually compiled. Templates are instantiated lazily — the definition must be visible at the point of use, or you must explicitly instantiate them.

## Common Causes

```cpp
// Cause 1: Template declared but defined in a .cpp file
// container.h
#pragma once
template <typename T>
class Container;
// Only declaration — no definition visible to includers

// container.cpp
#include "container.h"
template <typename T>
class Container {
    T data_;
public:
    void set(T val) { data_ = val; }
    T get() const { return data_; }
};

// main.cpp
#include "container.h"
int main() {
    Container<int> c;  // undefined reference — definition not in header
    c.set(42);
    return 0;
}
```

```cpp
// Cause 2: Explicit specialization not instantiated
// math.h
#pragma once
template <typename T>
T divide(T a, T b);

// main.cpp
#include "math.h"
int main() {
    double result = divide(10.0, 3.0);  // undefined reference
    return 0;
}
// No definition of divide<double> exists anywhere
```

```cpp
// Cause 3: Template defined only in one translation unit
// utils.h
#pragma once
template <typename T>
T max_val(T a, T b) { return (a > b) ? a : b; }

// utils.cpp
#include "utils.h"
// If main.cpp also includes utils.h, this is fine.
// But if utils.cpp has a separate template not in the header, it won't be visible.
```

```cpp
// Cause 4: Member function template not defined
// myclass.h
#pragma once
class MyClass {
public:
    template <typename T>
    void process(T val);  // declared but not defined
};

// main.cpp
MyClass obj;
obj.process(42);  // undefined reference
```

```cpp
// Cause 5: Using template from a library without linking
// If a template library requires specific instantiation flags
// g++ main.cpp -o main  ← missing library with explicit instantiations
```

## How to Fix

### Fix 1: Put Template Definitions in Headers

```cpp
// math.h
#pragma once

// Full definition in the header
template <typename T>
T divide(T a, T b) {
    if (b == T{}) throw std::runtime_error("division by zero");
    return a / b;
}

// main.cpp
#include "math.h"
#include <iostream>
int main() {
    std::cout << divide(10.0, 3.0) << std::endl;  // works
    return 0;
}
```

### Fix 2: Explicit Template Instantiation

```cpp
// math.h
#pragma once
template <typename T>
T divide(T a, T b);

// math.cpp
#include "math.h"
template <typename T>
T divide(T a, T b) {
    if (b == T{}) throw std::runtime_error("division by zero");
    return a / b;
}

// Explicit instantiations for the types we need
template int divide<int>(int, int);
template double divide<double>(double, double);

// main.cpp
#include "math.h"
#include <iostream>
int main() {
    std::cout << divide(10, 3) << std::endl;       // uses explicit instantiation
    std::cout << divide(10.0, 3.0) << std::endl;   // uses explicit instantiation
    return 0;
}
// Build: g++ main.cpp math.cpp -o main
```

### Fix 3: Use export in C++20 Modules (or Include-What-You-Use)

```cpp
// C++20 modules approach
// math.cppm
module;
#include <stdexcept>
export module math;

export template <typename T>
T divide(T a, T b) {
    if (b == T{}) throw std::runtime_error("division by zero");
    return a / b;
}

// main.cpp
import math;
#include <iostream>
int main() {
    std::cout << divide(10.0, 3.0) << std::endl;
    return 0;
}
```

### Fix 4: Separate Class Template Declaration and Inline Definition

```cpp
// myclass.h
#pragma once

class MyClass {
public:
    template <typename T>
    void process(T val) {
        // Definition inline in the header
        std::cout << "Processing: " << val << std::endl;
    }
};

// Or define outside the class but still in the header:
// template <typename T>
// void MyClass::process(T val) {
//     std::cout << "Processing: " << val << std::endl;
// }
```

### Fix 5: Explicit Instantiation for Complex Templates

```cpp
// serializer.h
#pragma once
#include <string>
#include <vector>

template <typename T>
class Serializer {
public:
    std::string serialize(const T& val);
};

// serializer.cpp
#include "serializer.h"
#include <sstream>

template <typename T>
std::string Serializer<T>::serialize(const T& val) {
    std::ostringstream oss;
    oss << val;
    return oss.str();
}

// Explicit instantiations
template class Serializer<int>;
template class Serializer<double>;
template class Serializer<std::string>;
```

## Examples

```cpp
// Real-world: header-only template library pattern
// sort_utils.h
#pragma once
#include <vector>
#include <algorithm>

template <typename RandomIt>
void bubble_sort(RandomIt begin, RandomIt end) {
    for (auto i = begin; i != end; ++i) {
        for (auto j = begin; j != i; ++j) {
            if (*j > *i) std::iter_swap(i, j);
        }
    }
}

// main.cpp
#include "sort_utils.h"
#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {5, 3, 1, 4, 2};
    bubble_sort(v.begin(), v.end());
    for (int x : v) std::cout << x << " ";
    return 0;
}
```

## Related Errors

- [Undefined reference]({{< relref "/languages/cpp/linker-undefined-reference-cpp" >}}) — non-template symbol not found.
- [Multiple definition]({{< relref "/languages/cpp/linker-multiple-definition-cpp" >}}) — template instantiated in multiple TUs.
- [ABI incompatible]({{< relref "/languages/cpp/linker-abi-incompatible" >}}) — ABI mismatch between translation units.
