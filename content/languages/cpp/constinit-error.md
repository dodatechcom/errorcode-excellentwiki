---
title: "constinit Init Not Constant - Fix"
description: "constinit requires a constant expression. Use constexpr constructors or switch to static/thread_local const if variable cannot be constant."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 953
---

# constinit Init Not Constant - Fix

constinit forces a variable to be initialized with a constant expression. Unlike const or constexpr, the variable can be modified later, but only if its initial value is constant.

## Common Causes

```cpp
// Non-constant initialization
int read_val() { return 42; }
constinit int x = read_val(); // error: read_val is not constexpr
```

```cpp
// Runtime value can't be used
int f() { static int val = 42; return val; }
constinit int y = f(); // error: f() not constexpr
```

```cpp
// Reference to non-constexpr global
int global = some_runtime_function();
constinit int& ref = global; // error: global not constant init
```

```cpp
// constexpr origin not sufficient for constinit
struct Point { double x, y; };
constexpr Point origin = {0, 0};
// constinit Point p = origin; // OK if origin is constexpr
```

## How to Fix

### Fix 1: Use constinit only with constexpr/consteval

```cpp
constexpr long long fib(int n) {
    return n <= 2 ? 1 : fib(n-1) + fib(n-2);
}
constinit const long long my_fib = fib(10);
```

### Fix 2: constexpr struct constructors

```cpp
struct Pair {
    int x; int y;
    constexpr Pair(int a, int b) : x(a), y(b) {}
};
consteval Pair make_pair(int a, int b) {
    return {a + 1, b + 1};
}
constinit Pair p = make_pair(3, 3);
```

### Fix 3: Use static/thread_local if not constant

```cpp
int runtime_init() {
    auto x = complex_calculation();
    return x;
}
// Not constinit but works:
static int x = runtime_init();
int& get_global() {
    static int val = runtime_init();
    return val;
}
```

### Fix 4: constinit const vs static const

```cpp
consteval int f() { return 42; }
constinit const int a = f();
static const int a = f();
```

## Examples

```cpp
#include <iostream>
consteval int compute() { return 42; }
constinit int g_arr[] = {1,2,3,4,5};
constinit const int GLOBAL = compute();

struct Complex {
    int a, b;
    constexpr Complex(int x, int y) noexcept : a(x), b(y) {}
};
constinit const Complex GLOBAL_POINT(10, 20);

int main() {
    std::cout << GLOBAL << std::endl;
    return 0;
}
```

## Related Errors

- [consteval-call-constexpr]({{< relref "/languages/cpp/consteval-call-constexpr" >}})
- [constexpr-function-limit]({{< relref "/languages/cpp/constexpr-function-limit" >}})
- [ctad-deduction-failure]({{< relref "/languages/cpp/ctad-deduction-failure" >}})
