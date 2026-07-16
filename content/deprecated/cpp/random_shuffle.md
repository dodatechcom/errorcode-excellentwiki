---
title: "[Solution] C++ random_shuffle() Deprecated — Replace with std::shuffle"
description: "Replace std::random_shuffle with std::shuffle in C++14. Migration guide with code examples."
deprecated_function: "std::random_shuffle"
replacement_function: "std::shuffle"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["random_shuffle", "shuffle", "random", "algorithm", "cpp14"]
weight: 5
---

# [Solution] C++ random_shuffle() Deprecated — Replace with std::shuffle

`std::random_shuffle` was deprecated in C++14 and removed in C++17 because it used implementation-defined random number generation, making results non-reproducible and platform-dependent. `std::shuffle` takes an explicit URBG (UniformRandomBitGenerator), giving you control over the random number source.

## What You'll See

In C++14:

```
warning: 'std::random_shuffle' is deprecated: Use std::shuffle instead
```

In C++17:

```
error: 'random_shuffle' is not a member of 'std'
```

## Why Deprecated

`std::random_shuffle` was deprecated because:

- **Implementation-defined randomness**: Different compilers and platforms produce different shuffles.
- **No reproducibility**: Cannot seed or control the random source for testing.
- **Weak randomness**: Some implementations used `rand()`, which has poor statistical quality.
- **Inconsistent behavior**: `std::random_shuffle(v.begin(), v.end())` produces different results on different systems.
- **Security risk**: Predictable shuffling in security contexts.

## Old Code (Deprecated)

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    std::random_shuffle(nums.begin(), nums.end());  // DEPRECATED

    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## New Code — std::shuffle with mt19937

```cpp
#include <algorithm>
#include <random>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    std::random_device rd;
    std::mt19937 g(rd());

    std::shuffle(nums.begin(), nums.end(), g);

    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## New Code — Reproducible Shuffle for Testing

```cpp
#include <algorithm>
#include <random>
#include <vector>
#include <iostream>
#include <cassert>

std::vector<int> shuffled(const std::vector<int>& input, unsigned seed) {
    std::vector<int> result = input;
    std::mt19937 g(seed);
    std::shuffle(result.begin(), result.end(), g);
    return result;
}

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};

    // Reproducible — same seed gives same shuffle
    auto s1 = shuffled(nums, 42);
    auto s2 = shuffled(nums, 42);
    assert(s1 == s2);

    // Different seed gives different shuffle
    auto s3 = shuffled(nums, 123);
    assert(s1 != s3);

    for (int n : s1) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

## New Code — Partial Shuffle

```cpp
#include <algorithm>
#include <random>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    std::mt19937 g(std::random_device{}());

    // Shuffle only the first 5 elements
    std::shuffle(nums.begin(), nums.begin() + 5, g);

    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Migration Steps

1. **Find all random_shuffle usage**:

```bash
grep -rn "\brandom_shuffle\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `random_shuffle(begin, end)` with `shuffle(begin, end, g)`** where `g` is a random engine.

3. **Add `#include <random>`** for `std::mt19937` and `std::random_device`.

4. **Create the random engine once** and reuse it for multiple shuffles.

5. **For reproducibility**, use a fixed seed instead of `std::random_device`.

6. **For test code**, always use a fixed seed so tests are deterministic.

## Related Deprecations

- [rand → arc4random]({{< relref "/deprecated/c/rand" >}}) — C random number deprecation.
- [bind1st → lambda]({{< relref "/deprecated/cpp/bind1st" >}}) — functional programming modernization.
- [auto_ptr → unique_ptr]({{< relref "/deprecated/cpp/auto_ptr" >}}) — smart pointer modernization.
