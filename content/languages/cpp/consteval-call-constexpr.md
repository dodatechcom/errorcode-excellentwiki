---
title: "consteval in non-constexpr context - Fix"
description: "consteval called in non-constexpr context. Make the enclosing function constexpr, use constinit, or separate the runtime path."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 952
---

# consteval in non-constexpr context - Fix

A consteval function can only be called in contexts that are evaluated at compile time. Attempting to call it from a runtime context produces a compile error. You must either ensure compile-time usage or split your code into separate paths.

## Common Causes

```cpp
// Error: consteval function called in a variable-length runtime argument
#include <iostream>
#include <array>

consteval int square(int x) { return x * x; }

int read_value() { int x; std::cin >> x; return x; }
int g() {
    return square(read_value());  // error: read_value() is not constexpr
}
```

```cpp
// This cannot be fixed unless read_value gives a compile time value:
int g2() {
    constexpr int v = 2; // compile-time
    return square(v); // OK
}
```

```

```cpp
// consteval in a function that is not constexpr
consteval int triple(int x) { return 3 * x; }

struct Foo {
    int x;
    Foo() : x(triple(read_val)) { } // error: call of consteval is in a non-constexpr constructor
};
```

```cpp
// passing a runtime variable to a consteval function
consteval int double_it(int x) { return x * 2; }

int main() {
    int y = double_it(y); // error
}
```

```

## How to Fix

### Fix 1: Make the enclosing function constexpr/consteval

```cpp
consteval int triple(int x) { return 3 * x; }

consteval int f() {
    return triple(10); // OK inside consteval/consteval
}

int main() {
    constexpr int result = f(); // OK
}
```

### Fix 2: use constinit for global constructors

```cpp
consteval int init_val() {
    return 42;
}

// constinit ensures constant init at load-time
constinit int val = init_val();
```

### Fix 3: separate runtime and compile-time paths

```cpp
consteval int compile_time_compute(int x) { return x * x; }

int runtime_compute(int x) { return x * x; }

int g(bool cond) {
    if (cond) {
        return runtime_compute(42);
    } else {
        return compile_time_compute(42); // OK: the argument 42 is constant
    }
}
```

### Fix 4: constexpr lambda wrapper

```cpp
consteval int square(int x) { return x * x; }

int main() {
    constexpr auto lam = [](int x) consteval { return x * 2; };
    int y = lam(read_int()); // not allowed
    // but:
    constexpr int z = lam(10); // OK

    return 0;
}
```

### Fix 5: static_assert for compile time inspection

```cpp
consteval int fact(int n) {
    int r = 1;
    for (int i = 1; i <= n; ++i) r *= i;
    return r;
}

static_assert(fact(5) == 120); // ok
```

```cpp
consteval int prime_at(int n) {
    // heavy but completely compile-time
    int cnt = 0;
    for (int i = 2; ; i++) { 
        bool is_prime = true;
        for (int j = 2; j * j <= i; j++) { 
            if (i % j == 0) { is_prime = false; break; }
        }
        if (is_prime) {
            cnt++;
            if (cnt == n) return i;
        }
    }
}
int main() {
    constexpr int p = prime_at(100); // 100th prime compile-time
}
```

## Examples

```cpp
#include <iostream>

// lookup table generated at compile time
consteval auto build_lookup() {
    std::array<int, 10> arr{};
    for (int i = 0; i < 10; ++i) arr[i] = i * i;
    return arr;
}

int main() {
    constexpr auto lu = build_lookup();
    int idx = 4; // read at runtime
    std::cout << lu[idx] << std::endl;

    // lookup might also be used as:
    static_assert(lu[5] == 25);
    return 0;
}
```

## Related Errors

- [constexpr-function-limit]({{< relref "/languages/cpp/constexpr-function-limit" >}})
- [constinit error]({{< relref "/languages/cpp/constinit-error" >}})
- [ctad-deduction-failure]({{< relref "/languages/cpp/ctad-deduction-failure" >}})
