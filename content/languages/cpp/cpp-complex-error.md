---
title: "[Solution] C++ std::complex Error — How to Fix"
description: "Fix C++ std::complex errors including domain errors, illegal operations, and precision loss in complex number computations."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ std::complex Error — How to Fix

`std::complex` operations can produce domain errors when dividing by zero, taking logarithms of zero, or performing operations that yield mathematically undefined results for complex numbers.

## Why It Happens

Complex number errors arise from division by a zero complex number, computing `std::log` or `std::pow` with a zero argument, using integer template parameters which lose precision, or relying on non-standard specializations that don't exist.

## Common Error Messages

1. `error: 'std::complex' not supported for integer types`
2. `runtime error: division by zero in complex division`
3. `error: domain error in 'std::log(complex)'`
4. `error: no matching function for call to 'real(std::complex<int>)'`

## How to Fix It

### Fix 1: Use Floating-Point Template Parameters

```cpp
#include <complex>
#include <iostream>

int main() {
    // WRONG — integer complex is not supported
    // std::complex<int> ci{1, 2};

    // CORRECT — use floating-point types
    std::complex<double> cd{1.0, 2.0};
    std::complex<float> cf{1.0f, 2.0f};

    std::cout << "cd = " << cd << "\n";
    std::cout << "cf = " << cf << "\n";
    return 0;
}
```

### Fix 2: Guard Against Division by Zero

```cpp
#include <complex>
#include <iostream>
#include <cmath>

int main() {
    std::complex<double> a{3.0, 4.0};
    std::complex<double> b{0.0, 0.0};

    // CORRECT — check before dividing
    if (std::abs(b) > 1e-15) {
        auto result = a / b;
        std::cout << "Result: " << result << "\n";
    } else {
        std::cout << "Cannot divide by zero complex number\n";
    }
    return 0;
}
```

### Fix 3: Handle Log and Pow Domain Errors

```cpp
#include <complex>
#include <iostream>
#include <cmath>

int main() {
    std::complex<double> z{0.0, 0.0};

    // log(0) is undefined — check first
    if (z != std::complex<double>{0.0, 0.0}) {
        auto result = std::log(z);
        std::cout << "log(z) = " << result << "\n";
    } else {
        std::cout << "log(0) is undefined\n";
    }

    // pow with negative real base and non-integer exponent
    std::complex<double> base{-2.0, 0.0};
    std::complex<double> exp{0.5, 0.0};
    auto result = std::pow(base, exp);  // complex pow handles this
    std::cout << "pow(-2, 0.5) = " << result << "\n";

    return 0;
}
```

### Fix 4: Use Proper Accessor Functions

```cpp
#include <complex>
#include <iostream>

int main() {
    std::complex<double> z{3.0, 4.0};

    // CORRECT — use .real() and .imag() member functions
    double r = z.real();
    double i = z.imag();
    double mag = std::abs(z);

    std::cout << "Real: " << r << ", Imag: " << i << ", Mag: " << mag << "\n";
    return 0;
}
```

## Common Scenarios

- **Integer complex**: Using `std::complex<int>` causes compilation errors because the standard only supports floating-point specializations.
- **Lossy operations**: `std::norm` returns the squared magnitude, which can overflow before `std::abs` does.
- **Polar construction**: Using `std::polar(inf, nan)` produces undefined results.

## Prevent It

1. Always use `std::complex<double>` or `std::complex<float>` — never integer types.
2. Check for zero denominators before complex division to avoid domain errors.
3. Use `std::norm(z)` instead of `std::abs(z) * std::abs(z)` to avoid unnecessary intermediate overflow.

## Related Errors

- [Domain error]({{< relref "/languages/cpp/domain-error-sqrt" >}}) — mathematical domain violations.
- [Overflow error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.
- [Invalid argument]({{< relref "/languages/cpp/invalid-argument" >}}) — bad function parameters.
