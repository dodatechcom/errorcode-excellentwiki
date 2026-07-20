---
title: "[Solution] C++ Undefined Reference — Linker Error Fix"
description: "Fix C++ undefined reference errors by linking all objects, placing template definitions in headers, fixing -l order, and using extern C."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-error"]
weight: 901
---

# C++ Undefined Reference — Linker Error Fix

An undefined reference error occurs when the linker cannot find the definition of a function or variable that has been declared but not compiled into any of the linked object files. This is one of the most common C++ linker errors and typically indicates a missing source file in the build, a missing library, or a declaration/definition mismatch.

## Common Causes

```cpp
// Cause 1: Missing source file in compilation
// math_utils.h
#pragma once
int add(int a, int b);

// math_utils.cpp
#include "math_utils.h"
int add(int a, int b) { return a + b; }

// main.cpp
#include <iostream>
#include "math_utils.h"
int main() {
    std::cout << add(1, 2) << std::endl;  // undefined reference if math_utils.cpp not compiled
    return 0;
}
// g++ main.cpp -o main  ← MISSING: math_utils.cpp
```

```cpp
// Cause 2: Template declaration without definition in translation unit
// header.h
#pragma once
template <typename T>
T maximum(T a, T b);

// main.cpp
#include "header.h"
int main() {
    int x = maximum(3, 5);  // undefined reference — no definition visible
    return 0;
}
```

```cpp
// Cause 3: Wrong library link order
// g++ main.cpp -lmylib  ← WRONG: library must come AFTER objects that use it
// Correct: g++ main.cpp -o main -lmylib
```

```cpp
// Cause 4: extern "C" mismatch
// math.h
#ifdef __cplusplus
extern "C" {
#endif
int c_add(int a, int b);
#ifdef __cplusplus
}
#endif

// main.cpp — missing extern "C" wrapper causes name mangling mismatch
#include "math.h"
int main() {
    return c_add(1, 2);  // undefined reference due to name mangling
}
```

```cpp
// Cause 5: Namespace confusion
// utils.h
namespace mylib {
    void do_something();
}

// main.cpp
#include "utils.h"
int main() {
    do_something();  // undefined reference — forgot namespace
    return 0;
}
```

## How to Fix

### Fix 1: Link All Required Object Files

```cpp
// Compile all translation units together
// math_utils.cpp
#include "math_utils.h"
int add(int a, int b) { return a + b; }

// main.cpp
#include <iostream>
#include "math_utils.h"
int main() {
    std::cout << add(1, 2) << std::endl;
    return 0;
}

// Build: g++ main.cpp math_utils.cpp -o main
// Or compile separately:
// g++ -c main.cpp -o main.o
// g++ -c math_utils.cpp -o math_utils.o
// g++ main.o math_utils.o -o main
```

### Fix 2: Put Template Definitions in Headers

```cpp
// math_utils.h
#pragma once

// Definition must be in the header for templates
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// main.cpp
#include <iostream>
#include "math_utils.h"
int main() {
    std::cout << maximum(3, 5) << std::endl;  // works
    std::cout << maximum(3.0, 5.0) << std::endl;  // works
    return 0;
}
```

### Fix 3: Place -l Flags After Object Files

```bash
# WRONG — library before object files
g++ main.cpp -lmylib -o main

# CORRECT — library after object files
g++ main.cpp -o main -lmylib

# Multiple libraries: order matters (dependencies go left to right)
g++ main.cpp -o main -lmylib -lotherlib
```

### Fix 4: Use extern "C" Consistently

```cpp
// math.h
#pragma once

#ifdef __cplusplus
extern "C" {
#endif

int c_add(int a, int b);

#ifdef __cplusplus
}
#endif
```

```cpp
// main.cpp
#include <iostream>
#include "math.h"

int main() {
    std::cout << c_add(1, 2) << std::endl;  // works
    return 0;
}
```

### Fix 5: Verify Include and Namespace Usage

```cpp
// utils.h
#pragma once
namespace mylib {
    void do_something();
}

// utils.cpp
#include "utils.h"
#include <iostream>
void mylib::do_something() {
    std::cout << "done" << std::endl;
}

// main.cpp
#include "utils.h"
int main() {
    mylib::do_something();  // correct: use namespace
    return 0;
}
// Build: g++ main.cpp utils.cpp -o main
```

## Examples

```cpp
// Real-world: header-only library pattern
// container.h
#pragma once
#include <vector>
#include <stdexcept>

template <typename T>
class SafeVector {
    std::vector<T> data_;
public:
    void push(const T& val) { data_.push_back(val); }
    T& at(size_t i) {
        if (i >= data_.size()) throw std::out_of_range("index");
        return data_.at(i);
    }
    size_t size() const { return data_.size(); }
};

// main.cpp — no extra .cpp needed, everything in header
#include <iostream>
#include "container.h"

int main() {
    SafeVector<int> v;
    v.push(42);
    std::cout << v.at(0) << std::endl;
    return 0;
}
// Build: g++ main.cpp -o main
```

## Related Errors

- [Multiple definition]({{< relref "/languages/cpp/linker-multiple-definition-cpp" >}}) — symbol defined in multiple translation units.
- [Template symbol undefined]({{< relref "/languages/cpp/linker-template-symbol" >}}) — undefined reference to template function.
- [ABI incompatible]({{< relref "/languages/cpp/linker-abi-incompatible" >}}) — C++ ABI mismatch between translation units.
