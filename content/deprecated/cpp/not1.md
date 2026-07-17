---
title: "[Solution] C++ not1() Deprecated — Replace with Lambda"
description: "Replace std::not1 with lambdas in C++11 and later. Migration guide with code examples."
deprecated_function: "std::not1"
replacement_function: "lambda"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C++ not1() Deprecated — Replace with Lambda

`std::not1` was deprecated in C++17 because lambdas provide a clearer way to negate predicates. `not1` wraps a unary function object and negates its result, but the semantics are confusing and the syntax is verbose compared to lambdas.

## What You'll See

In C++17:

```
warning: 'std::not1' is deprecated: Use lambdas instead
```

## Why Deprecated

`std::not1` was deprecated because:

- **Confusing semantics**: `not1(f)(x)` is equivalent to `!f(x)`, but the wrapper obscures this.
- **Requires unary_function base**: The wrapped function must derive from `unary_function`, which is also deprecated.
- **Lambda is clearer**: `[](int x) { return !pred(x); }` is immediately understandable.
- **Less flexible**: Cannot negate predicates with multiple arguments or add conditions.

## Old Code (Deprecated)

```cpp
#include <functional>
#include <algorithm>
#include <vector>
#include <iostream>

struct IsPositive : public std::unary_function<int, bool> {
    bool operator()(int x) const { return x > 0; }
};

int main() {
    std::vector<int> nums = {-3, -1, 0, 2, 5};

    // Count non-positive numbers using not1
    int count = std::count_if(nums.begin(), nums.end(),
                               std::not1(IsPositive()));

    std::cout << "Non-positive: " << count << std::endl;
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

    // Lambda — no class or wrapper needed
    int count = std::count_if(nums.begin(), nums.end(),
                               [](int x) { return x <= 0; });

    std::cout << "Non-positive: " << count << std::endl;
    return 0;
}
```

## New Code — Reusable Predicate

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

// Named predicate — reusable and debuggable
struct IsNonPositive {
    bool operator()(int x) const { return x <= 0; }
};

int main() {
    std::vector<int> nums = {-3, -1, 0, 2, 5};

    int count = std::count_if(nums.begin(), nums.end(), IsNonPositive());

    std::cout << "Non-positive: " << count << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all not1 usage**:

```bash
grep -rn "\bnot1\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `not1(pred)` with `[&pred](auto x) { return !pred(x); }`** or rewrite the predicate directly.

3. **For simple predicates**, invert the logic directly in the lambda: `x > 0` becomes `x <= 0`.

4. **For reusable predicates**, create a named struct with `operator()`.

5. **Remove the `unary_function` base class** from wrapped predicates.

## Related Deprecations

- [not2 → lambda]({{< relref "/deprecated/cpp/not2" >}}) — binary negation wrapper.
- [logical_not → std::negate]({{< relref "/deprecated/cpp/logical_not" >}}) — logical negation.
- [unary_function → std::function]({{< relref "/deprecated/cpp/unary_function" >}}) — base class removal.
