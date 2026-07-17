---
title: "[Solution] C++ logical_not Deprecated — Replace with std::negate"
description: "Replace std::logical_not with std::negate in C++11 and later. Migration guide with code examples."
deprecated_function: "std::logical_not"
replacement_function: "std::negate"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C++ logical_not Deprecated — Replace with std::negate

`std::logical_not` was deprecated in C++17 because it operated on `bool` values, while `std::negate` operates on arithmetic types and provides more useful behavior. For logical negation, lambdas are clearer.

## What You'll See

In C++17:

```
warning: 'std::logical_not' is deprecated: Use std::negate or lambdas instead
```

## Why Deprecated

`std::logical_not` was deprecated because:

- **Limited to bool**: Only works with `bool` type, not general predicates.
- **Confusing with negate**: `logical_not` converts to bool first, `negate` operates on the value.
- **Lambda is clearer**: `[](bool x) { return !x; }` is more readable.
- **Misleading name**: For arithmetic types, negation (`-x`) is more useful than logical negation (`!x`).

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<bool> flags = {true, false, true, false, true};

    // Count false values using logical_not
    int count = std::count_if(flags.begin(), flags.end(),
                               std::logical_not<bool>());

    std::cout << "False values: " << count << std::endl;
    return 0;
}
```

## New Code — Lambda Replacement

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<bool> flags = {true, false, true, false, true};

    // Lambda — clear and modern
    int count = std::count_if(flags.begin(), flags.end(),
                               [](bool x) { return !x; });

    std::cout << "False values: " << count << std::endl;
    return 0;
}
```

## New Code — std::negate for Arithmetic

```cpp
#include <functional>
#include <numeric>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {1, -2, 3, -4, 5};

    // Negate each element (arithmetic negation, not logical)
    std::vector<int> negated(nums.size());
    std::transform(nums.begin(), nums.end(), negated.begin(),
                   std::negate<int>());

    for (int n : negated) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all logical_not usage**:

```bash
grep -rn "\blogical_not\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `std::logical_not<T>()` with `[](T x) { return !x; }`**.

3. **For arithmetic negation**, use `std::negate<T>()`.

4. **For complex predicates**, write a named lambda or function for clarity.

## Related Deprecations

- [not1 → lambda]({{< relref "/deprecated/cpp/not1" >}}) — unary negation wrapper.
- [not2 → lambda]({{< relref "/deprecated/cpp/not2" >}}) — binary negation wrapper.
- [unary_function → std::function]({{< relref "/deprecated/cpp/unary_function" >}}) — base class removal.
