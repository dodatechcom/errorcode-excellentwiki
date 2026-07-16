---
title: "[Solution] C++ bind2nd() Deprecated — Replace with Lambda"
description: "Replace std::bind2nd with lambdas in C++11 and later. Migration guide with code examples."
deprecated_function: "std::bind2nd"
replacement_function: "lambda"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["bind2nd", "lambda", "functional", "cpp11", "bind"]
weight: 5
---

# [Solution] C++ bind2nd() Deprecated — Replace with Lambda

`std::bind2nd` was deprecated in C++11 and removed in C++17 because lambdas provide a clearer, more flexible, and more efficient way to bind arguments. `bind2nd` was limited to binding the second argument of a binary function object.

## What You'll See

In C++11/14:

```
warning: 'std::bind2nd' is deprecated: Use lambdas instead
```

In C++17:

```
error: 'bind2nd' is not a member of 'std'
```

## Why Deprecated

`std::bind2nd` was deprecated because:

- **Limited flexibility**: Only binds the second argument of a binary function.
- **Confusing semantics**: The unbound argument becomes the first parameter.
- **Cannot bind by reference**: Lambdas capture variables by reference explicitly.
- **Poor readability**: Harder to understand than equivalent lambdas.
- **Less efficient**: Lambdas are inlined by compilers.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

int divide(int a, int b) {
    return a / b;
}

int main() {
    std::vector<int> nums = {10, 20, 30, 40, 50};

    // Divide each element by 10
    std::transform(nums.begin(), nums.end(), nums.begin(),
                   std::bind2nd(std::ptr_fun(divide), 10));

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

int divide(int a, int b) {
    return a / b;
}

int main() {
    std::vector<int> nums = {10, 20, 30, 40, 50};

    // Divide each element by 10 — clear and efficient
    std::transform(nums.begin(), nums.end(), nums.begin(),
                   [](int x) { return x / 10; });

    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all bind2nd usage**:

```bash
grep -rn "\bbind2nd\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `bind2nd(ptr_fun(f), val)` with `[val](int x) { return f(x, val); }`**.

3. **For member functions**, use lambdas with captures.

4. **Note the argument order** — `bind2nd` binds the second argument, so the lambda parameter is the first argument.

## Related Deprecations

- [bind1st → lambda]({{< relref "/deprecated/cpp/bind1st" >}}) — same pattern, first argument.
- [ptr_fun → std::function]({{< relref "/deprecated/cpp/ptr_fun" >}}) — function wrapper modernization.
- [not1 → lambda]({{< relref "/deprecated/cpp/not1" >}}) — negation modernization.
