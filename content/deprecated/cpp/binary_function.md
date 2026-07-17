---
title: "[Solution] C++ binary_function Deprecated — Replace with std::function"
description: "Replace std::binary_function with lambdas or std::function in C++11 and later. Migration guide with code examples."
deprecated_function: "std::binary_function"
replacement_function: "std::function"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C++ binary_function Deprecated — Replace with std::function

`std::binary_function` was deprecated in C++11 and removed in C++17 because it was an unnecessary base class for binary function objects. It provided `first_argument_type`, `second_argument_type`, and `result_type` typedefs that are no longer needed with modern C++.

## What You'll See

In C++11/14:

```
warning: 'std::binary_function' is deprecated
```

In C++17:

```
error: 'binary_function' is not a member of 'std'
```

## Why Deprecated

`std::binary_function` was deprecated because:

- **Unnecessary base class**: Function objects don't need a common base class.
- **typedefs are obsolete**: Type traits can deduce argument and result types.
- **Lambdas are simpler**: No class definition needed.
- **Prevents optimization**: Inheritance can inhibit compiler optimizations.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

struct Multiply : public std::binary_function<int, int, int> {
    int operator()(int a, int b) const {
        return a * b;
    }
};

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};

    int product = std::accumulate(nums.begin(), nums.end(), 1, Multiply());

    std::cout << "Product: " << product << std::endl;
    return 0;
}
```

## New Code — Lambda Replacement

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};

    // Lambda — no class definition needed
    int product = std::accumulate(nums.begin(), nums.end(), 1,
                                   [](int a, int b) { return a * b; });

    std::cout << "Product: " << product << std::endl;
    return 0;
}
```

## New Code — Function Object Without Base Class

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

// Simple function object — no inheritance needed
struct Multiply {
    int operator()(int a, int b) const {
        return a * b;
    }
};

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};

    int product = std::accumulate(nums.begin(), nums.end(), 1, Multiply());

    std::cout << "Product: " << product << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all binary_function usage**:

```bash
grep -rn "\bbinary_function\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Remove the inheritance**: `struct Func : public std::binary_function<T1, T2, R>` becomes `struct Func`.

3. **Remove the typedefs** (`first_argument_type`, `second_argument_type`, `result_type`).

4. **Replace with lambdas** where the function object is simple and used inline.

5. **Keep as standalone function objects** if they need to be named types.

## Related Deprecations

- [unary_function → std::function]({{< relref "/deprecated/cpp/unary_function" >}}) — unary version.
- [ptr_fun → std::function]({{< relref "/deprecated/cpp/ptr_fun" >}}) — free function wrapper.
- [bind1st → lambda]({{< relref "/deprecated/cpp/bind1st" >}}) — argument binding modernization.
