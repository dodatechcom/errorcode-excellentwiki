---
title: "[Solution] C++ std::bad_optional_access - empty optional"
description: "Fix C++ std::bad_optional_access when accessing an empty std::optional. Check has_value() before use."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::bad_optional_access - empty optional

`std::bad_optional_access` is thrown when you call `std::optional::value()` on an empty optional.

## Common Causes

```cpp
// Cause 1: value() on empty optional
std::optional<int> opt;
int val = opt.value(); // throws

// Cause 2: * operator on empty optional
std::optional<int> opt;
int val = *opt; // undefined behavior

// Cause 3: Optional not set conditionally
std::optional<std::string> name;
if (condition) {
    name = "Alice";
}
std::string n = name.value(); // throws if condition was false
```

## How to Fix

### Fix 1: Check has_value()

```cpp
std::optional<int> opt = get_value();
if (opt.has_value()) {
    int val = opt.value();
}
```

### Fix 2: Use value_or()

```cpp
int val = opt.value_or(0); // returns 0 if empty
```

### Fix 3: Use operator* with check

```cpp
if (opt) {
    int val = *opt;
}
```

## Related Errors

- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong variant type.
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — any_cast failure.
- [std::bad_function_call]({{< relref "/languages/cpp/bad-function-call" >}}) — empty function.
