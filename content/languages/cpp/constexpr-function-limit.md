---
title: "C++ constexpr Function Iteration Limit - Fix"
description: "Fix constexpr function iteration & complexity limits by reducing recursion, using consteval, or C++14 relaxed constexpr rules."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 951
---

# C++ constexpr Function Iteration Limit - Fix

Compilers impose limits on constexpr function complexity to prevent infinite loops. Exceeding them produces errors like "constexpr evaluation depth" or "fatal error: recursive constexpr call".

## Common Causes

```cpp
// Cause: constexpr recursion depth too high
#include <iostream>
constexpr int fibonacci(int n) {
    return n <= 1 ? n : fibonacci(n - 1) + fibonacci(n - 2);
}
int main() {
    constexpr int fib50 = fibonacci(50);  // WAY too deep
    std::cout << fib50 << std::endl;
    return 0;
}
```

```cpp
// Cause: constexpr loop with too many iterations
constexpr int sum_n(int n) {
    int s = 0;
    for (int i = 0; i < n; ++i) { s += i; }
    return s;
}
constexpr int s = sum_n(100000);  // may exceed limit
```

```cpp
// Cause: Template instantiation depth
template <int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};
template <> struct Factorial<0> { static constexpr int value = 1; };
constexpr int f = Factorial<10000>::value;  // extreme compile times
```

## How to Fix

### Fix 1: Iterate Instead of Recurse

```cpp
#include <iostream>
constexpr long long fibonacci_iter(int n) {
    if (n <= 1) return n;
    long long a = 0, b = 1;
    for (int i = 2; i <= n; ++i) { long long t = a + b; a = b; b = t; }
    return b;
}
int main() {
    constexpr long long fib50 = fibonacci_iter(50);
    std::cout << fib50 << std::endl; // 12586269025
    return 0;
}
```

### Fix 2: Use consteval

```cpp
#include <iostream>
consteval int factorial(int n) {
    int r = 1;
    for (int i = 2; i <= n; ++i) r *= i;
    return r;
}
int main() {
    constexpr int f = factorial(10); // evaluated at compile time
    std::cout << f << std::endl;
    return 0;
}
```

### Fix 3: constexpr tables via C++14 loops

```cpp
#include <array>
#include <iostream>

template<int N>
constexpr std::array<int, N> fib_lookup()
{
    std::array<int, N> arr{};
    int a = 0, b = 1;
    for (int i = 0; i < N; ++i) {
        if (i == 0) arr[i] = a;
        else if (i == 1) arr[i] = b;
        else { int t = a + b; arr[i] = t; a = b; b = t; }
    }
    return arr;
}

int main()
{
    constexpr auto lookup = fib_lookup<50>();
    std::cout << lookup[20] << std::endl;
    return 0;
}
```

### Fix 4: Move high-complexity to runtime

```cpp
#include <iostream>

constexpr int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int fib_big(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) { int c = a + b; a = b; b = c; }
    return b;
}
```

## Examples

```cpp
// constexpr binary search for sorted lookup
#include <array>
#include <iostream>

template <typename T, size_t N>
constexpr bool cexpr_binary_search(const std::array<T, N>& a, T v) {
    size_t l = 0, r = N;
    while (l < r) {
        size_t m = l + (r - l) / 2;
        if (a[m] < v) l = m + 1;
        else if (a[m] > v) r = m;
        else return true;
    }
    return false;
}

int main() {
    constexpr std::array<int, 5> a{1, 2, 3, 4, 5};
    constexpr bool f = cexpr_binary_search(a, 3);
    static_assert(f);
}
```

## Related Errors

- [consteval call constexpr]({{< relref "/languages/cpp/consteval-call-constexpr" >}})
- [constinit error]({{< relref "/languages/cpp/constinit-error" >}})
- [ctad-deduction-failure]({{< relref "/languages/cpp/ctad-deduction-failure" >}})
