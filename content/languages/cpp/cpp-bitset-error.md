---
title: "[Solution] C++ std::bitset Error — How to Fix"
description: "Fix C++ std::bitset errors including out-of-range access, invalid character in constructor, and bitshift overflow issues."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ std::bitset Error — How to Fix

`std::bitset` is a fixed-size sequence of bits that can throw `out_of_range` on invalid index access, fail during construction from invalid strings, or produce unexpected results from bitshift operations exceeding the bit width.

## Why It Happens

Bitset errors occur when accessing bits at positions greater than or equal to `N`, constructing from strings containing characters other than `'0'` and `'1'`, shifting by amounts larger than the bitset size, or using `to_ulong()` when the value exceeds `unsigned long` range.

## Common Error Messages

1. `std::out_of_range: bitset::operator[]`
2. `std::invalid_argument: invalid bitset string`
3. `std::overflow_error: bitset value too large for to_ulong`
4. `error: shift count >= width of type`

## How to Fix It

### Fix 1: Bounds-Check Index Access

```cpp
#include <bitset>
#include <iostream>

int main() {
    std::bitset<8> bs(0b10101010);

    // WRONG — unchecked access can be dangerous in debug
    // bool val = bs[10];  // undefined if unchecked

    // CORRECT — use .test() for bounds-checked access
    try {
        bool val = bs.test(3);
        std::cout << "Bit 3: " << val << "\n";
        bs.test(10);  // throws out_of_range
    } catch (const std::out_of_range& e) {
        std::cout << "Error: " << e.what() << "\n";
    }
    return 0;
}
```

### Fix 2: Validate Construction Strings

```cpp
#include <bitset>
#include <iostream>
#include <string>

int main() {
    std::string valid = "10101010";
    std::string invalid = "10102010";

    // CORRECT — catch invalid construction
    try {
        std::bitset<8> bs1(valid);
        std::cout << "Valid: " << bs1 << "\n";

        std::bitset<8> bs2(invalid);  // throws
    } catch (const std::invalid_argument& e) {
        std::cout << "Error: " << e.what() << "\n";
    }
    return 0;
}
```

### Fix 3: Handle Shift Overflow Safely

```cpp
#include <bitset>
#include <iostream>

int main() {
    std::bitset<8> bs(0b00000001);

    // WRONG — shift by >= size is undefined
    // auto shifted = bs << 8;

    // CORRECT — validate shift amount
    std::size_t shift = 3;
    if (shift < bs.size()) {
        auto shifted = bs << shift;
        std::cout << "Shifted: " << shifted << "\n";
    }
    return 0;
}
```

### Fix 4: Safe Conversion to Integer

```cpp
#include <bitset>
#include <iostream>
#include <limits>

int main() {
    std::bitset<64> bs(0b1111111111111111111111111111111111111111111111111111111111111111);

    // WRONG — to_ulong may overflow
    // unsigned long val = bs.to_ulong();

    // CORRECT — check against max value first
    if (bs.to_ullong() <= std::numeric_limits<unsigned long>::max()) {
        unsigned long val = bs.to_ulong();
        std::cout << "Value: " << val << "\n";
    } else {
        std::cout << "Value too large for unsigned long\n";
    }
    return 0;
}
```

## Common Scenarios

- **String construction**: Passing a string with non-binary characters throws `invalid_argument`.
- **Large shifts**: Shifting a bitset by its own width or more produces undefined behavior.
- **to_ulong overflow**: Converting a bitset with high bits set to `unsigned long` throws `overflow_error`.

## Prevent It

1. Always use `.test()` instead of `operator[]` when the index may be out of range.
2. Validate shift amounts are less than the bitset width before shifting.
3. Use `to_ullong()` on 64-bit bitsets or check against `std::numeric_limits` before converting.

## Related Errors

- [Out of range]({{< relref "/languages/cpp/out-of-range-2" >}}) — container index violations.
- [Invalid argument]({{< relref "/languages/cpp/invalid-argument" >}}) — bad function parameters.
- [Overflow error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.
