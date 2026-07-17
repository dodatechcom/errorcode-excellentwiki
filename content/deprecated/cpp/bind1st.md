---
title: "[Solution] C++ bind1st() Deprecated — Replace with Lambda"
description: "Replace std::bind1st with lambdas in C++11 and later. Migration guide with code examples."
deprecated_function: "std::bind1st"
replacement_function: "lambda"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C++ bind1st() Deprecated — Replace with Lambda

`std::bind1st` was deprecated in C++11 and removed in C++17 because lambdas provide a clearer, more flexible, and more efficient way to bind arguments to function objects. `bind1st` was limited to binary function objects and had confusing semantics.

## What You'll See

In C++11/14:

```
warning: 'std::bind1st' is deprecated: Use lambdas instead
```

In C++17:

```
error: 'bind1st' is not a member of 'std'
```

## Why Deprecated

`std::bind1st` was deprecated because:

- **Limited flexibility**: Only binds the first argument of a binary function.
- **Confusing semantics**: The bound object becomes the `this` pointer, which is non-obvious.
- **Cannot bind by reference**: Lambdas capture variables by reference explicitly.
- **Poor readability**: `bind1st(ptr_fun(multiply), 5)` is harder to read than `[](int x) { return 5 * x; }`.
- **Less efficient**: Lambdas are inlined by compilers, while binders may not be.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

int multiply(int a, int b) {
    return a * b;
}

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};

    // Multiply each element by 5
    std::transform(nums.begin(), nums.end(), nums.begin(),
                   std::bind1st(std::ptr_fun(multiply), 5));

    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## New Code — Lambda Replacement

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int multiply(int a, int b) {
    return a * b;
}

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};

    // Multiply each element by 5 — clear and efficient
    std::transform(nums.begin(), nums.end(), nums.begin(),
                   [](int x) { return 5 * x; });

    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all bind1st usage**:

```bash
grep -rn "\bbind1st\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `bind1st(ptr_fun(f), val)` with `[val](int x) { return f(val, x); }`**.

3. **For member functions**, use lambdas with captures or `std::bind` with placeholders.

4. **Simplify complex bind chains** — lambdas are usually more readable.

## Related Deprecations

- [bind2nd → lambda]({{< relref "/deprecated/cpp/bind2nd" >}}) — same pattern, second argument.
- [ptr_fun → std::function]({{< relref "/deprecated/cpp/ptr_fun" >}}) — function wrapper modernization.
- [mem_fun → std::function]({{< relref "/deprecated/cpp/mem_fun" >}}) — member function wrapper modernization.
