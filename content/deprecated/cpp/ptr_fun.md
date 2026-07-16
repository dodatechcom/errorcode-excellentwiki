---
title: "[Solution] C++ ptr_fun() Deprecated — Replace with std::function"
description: "Replace std::ptr_fun with std::function or lambdas in C++11 and later. Migration guide with code examples."
deprecated_function: "std::ptr_fun"
replacement_function: "std::function"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["ptr_fun", "std::function", "lambda", "functional", "cpp11"]
weight: 5
---

# [Solution] C++ ptr_fun() Deprecated — Replace with std::function

`std::ptr_fun` was deprecated in C++11 and removed in C++17 because it was unnecessary — function pointers can be used directly, or wrapped in `std::function` when a polymorphic function wrapper is needed. Lambdas have further reduced the need for both.

## What You'll See

In C++11/14:

```
warning: 'std::ptr_fun' is deprecated: Use std::function or lambdas instead
```

In C++17:

```
error: 'ptr_fun' is not a member of 'std'
```

## Why Deprecated

`std::ptr_fun` was deprecated because:

- **Unnecessary wrapper**: Function pointers work directly with most algorithms.
- **Limited functionality**: Only wraps free functions, not member functions or lambdas.
- **Replaced by std::function**: A more general and flexible wrapper.
- **Lambdas are better**: For simple cases, lambdas are more readable and efficient.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

bool is_positive(int x) {
    return x > 0;
}

int main() {
    std::vector<int> nums = {-3, -1, 0, 2, 5};

    // Count positive numbers
    int count = std::count_if(nums.begin(), nums.end(),
                               std::ptr_fun(is_positive));

    std::cout << "Positive: " << count << std::endl;
    return 0;
}
```

## New Code — Function Pointer (Simplest)

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

bool is_positive(int x) {
    return x > 0;
}

int main() {
    std::vector<int> nums = {-3, -1, 0, 2, 5};

    // Function pointer works directly — no wrapper needed
    int count = std::count_if(nums.begin(), nums.end(), is_positive);

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

    // Lambda — more readable and inlineable
    int count = std::count_if(nums.begin(), nums.end(),
                               [](int x) { return x > 0; });

    std::cout << "Positive: " << count << std::endl;
    return 0;
}
```

## New Code — std::function for Polymorphism

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

bool is_positive(int x) {
    return x > 0;
}

int main() {
    std::vector<int> nums = {-3, -1, 0, 2, 5};

    // std::function when you need to store or pass the wrapper
    std::function<bool(int)> predicate = is_positive;

    int count = std::count_if(nums.begin(), nums.end(), predicate);

    std::cout << "Positive: " << count << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all ptr_fun usage**:

```bash
grep -rn "\bptr_fun\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `ptr_fun(f)` with just `f`** — function pointers work directly with algorithms.

3. **Replace with lambdas** when you need inline, readable predicates.

4. **Replace with `std::function`** when you need to store or pass the wrapper polymorphically.

5. **Remove `<functional>` include** if no other binders/function objects are used.

## Related Deprecations

- [mem_fun → std::function]({{< relref "/deprecated/cpp/mem_fun" >}}) — member function wrapper.
- [bind1st → lambda]({{< relref "/deprecated/cpp/bind1st" >}}) — argument binding.
- [bind2nd → lambda]({{< relref "/deprecated/cpp/bind2nd" >}}) — argument binding.
