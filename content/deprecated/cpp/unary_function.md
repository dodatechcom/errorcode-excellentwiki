---
title: "[Solution] C++ unary_function Deprecated — Replace with std::function"
description: "Replace std::unary_function with lambdas or std::function in C++11 and later. Migration guide with code examples."
deprecated_function: "std::unary_function"
replacement_function: "std::function"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["unary_function", "std::function", "lambda", "functional", "cpp11"]
weight: 5
---

# [Solution] C++ unary_function Deprecated — Replace with std::function

`std::unary_function` was deprecated in C++11 and removed in C++17 because it was an unnecessary base class for function objects. It provided `argument_type` and `result_type` typedefs that are no longer needed with modern C++ features like lambdas and `std::function`.

## What You'll See

In C++11/14:

```
warning: 'std::unary_function' is deprecated
```

In C++17:

```
error: 'unary_function' is not a member of 'std'
```

## Why Deprecated

`std::unary_function` was deprecated because:

- **Unnecessary base class**: Function objects don't need a common base class.
- **typedefs are obsolete**: `argument_type` and `result_type` are replaced by `decltype` and `std::invoke_result`.
- **Lambdas are simpler**: No class definition needed for simple function objects.
- **Prevents optimization**: Inheriting from a base class can inhibit compiler optimizations.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

struct IsPositive : public std::unary_function<int, bool> {
    bool operator()(int x) const {
        return x > 0;
    }
};

int main() {
    std::vector<int> nums = {-3, -1, 0, 2, 5};

    int count = std::count_if(nums.begin(), nums.end(), IsPositive());

    std::cout << "Positive: " << count << std::endl;
    return 0;
}
```

## New Code — Lambda Replacement

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {-3, -1, 0, 2, 5};

    // Lambda — no class definition needed
    int count = std::count_if(nums.begin(), nums.end(),
                               [](int x) { return x > 0; });

    std::cout << "Positive: " << count << std::endl;
    return 0;
}
```

## New Code — Function Object Without Base Class

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

// Simple function object — no inheritance needed
struct IsPositive {
    bool operator()(int x) const {
        return x > 0;
    }
};

int main() {
    std::vector<int> nums = {-3, -1, 0, 2, 5};

    // Works the same — no base class required
    int count = std::count_if(nums.begin(), nums.end(), IsPositive());

    std::cout << "Positive: " << count << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all unary_function usage**:

```bash
grep -rn "\bunary_function\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Remove the inheritance**: `struct Func : public std::unary_function<T, R>` becomes `struct Func`.

3. **Remove the `argument_type` and `result_type` typedefs** if present.

4. **Replace with lambdas** where the function object is simple and used inline.

5. **Keep as standalone function objects** if they need to be named types or stored in containers.

## Related Deprecations

- [binary_function → std::function]({{< relref "/deprecated/cpp/binary_function" >}}) — binary version.
- [ptr_fun → std::function]({{< relref "/deprecated/cpp/ptr_fun" >}}) — free function wrapper.
- [mem_fun_ref → std::function]({{< relref "/deprecated/cpp/mem_fun_ref" >}}) — member function wrapper.
