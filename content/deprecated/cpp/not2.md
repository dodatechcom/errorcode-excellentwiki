---
title: "[Solution] C++ not2() Deprecated — Replace with Lambda"
description: "Replace std::not2 with lambdas in C++11 and later. Migration guide with code examples."
deprecated_function: "std::not2"
replacement_function: "lambda"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C++ not2() Deprecated — Replace with Lambda

`std::not2` was deprecated in C++17 because lambdas provide a clearer way to negate binary predicates. `not2` wraps a binary function object and negates its result, but the semantics are confusing and the syntax is verbose.

## What You'll See

In C++17:

```
warning: 'std::not2' is deprecated: Use lambdas instead
```

## Why Deprecated

`std::not2` was deprecated because:

- **Confusing semantics**: `not2(f)(x, y)` is equivalent to `!f(x, y)`, but the wrapper obscures this.
- **Requires binary_function base**: The wrapped function must derive from `binary_function`, which is also deprecated.
- **Lambda is clearer**: `[](int a, int b) { return !comp(a, b); }` is immediately understandable.
- **Less flexible**: Cannot negate predicates with side conditions.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

struct NotEqual : public std::binary_function<int, int, bool> {
    bool operator()(int a, int b) const { return a != b; }
};

int main() {
    std::vector<int> nums = {1, 2, 2, 3, 3, 3};

    // Count equal adjacent pairs using not2(NotEqual)
    int count = std::count_if(nums.begin(), nums.end() - 1,
                               std::not2(NotEqual()));

    // Actually this counts where nums[i] == nums[i+1]
    // not2(NotEqual) means "not not equal" = "equal"

    // Correct approach with adjacent_find
    auto it = nums.begin();
    int equal_count = 0;
    while ((it = std::adjacent_find(it, nums.end())) != nums.end()) {
        equal_count++;
        ++it;
    }

    std::cout << "Equal adjacent pairs: " << equal_count << std::endl;
    return 0;
}
```

## New Code — Lambda Replacement

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {1, 2, 2, 3, 3, 3};

    // Lambda with std::equal — clear intent
    int count = 0;
    for (size_t i = 0; i + 1 < nums.size(); i++) {
        if (nums[i] == nums[i + 1]) {
            count++;
        }
    }

    std::cout << "Equal adjacent pairs: " << count << std::endl;
    return 0;
}
```

## New Code — Lambda with std::count_if

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {1, 2, 2, 3, 3, 3};

    // Lambda negation of a comparison
    std::vector<int> sorted_nums = nums;
    std::sort(sorted_nums.begin(), sorted_nums.end());

    // Count elements not in sorted position
    int count = 0;
    for (size_t i = 0; i < nums.size(); i++) {
        if (nums[i] != sorted_nums[i]) {
            count++;
        }
    }

    std::cout << "Out of place: " << count << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all not2 usage**:

```bash
grep -rn "\bnot2\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `not2(pred)` with a lambda that inverts the predicate**: `[](auto a, auto b) { return !pred(a, b); }`.

3. **Or invert the logic directly**: if `pred(a, b)` was `a != b`, use `a == b` in the lambda.

4. **Remove the `binary_function` base class** from wrapped predicates.

5. **For complex cases**, write a named function or struct with clear documentation.

## Related Deprecations

- [not1 → lambda]({{< relref "/deprecated/cpp/not1" >}}) — unary negation wrapper.
- [logical_not → std::negate]({{< relref "/deprecated/cpp/logical_not" >}}) — logical negation.
- [binary_function → std::function]({{< relref "/deprecated/cpp/binary_function" >}}) — base class removal.
