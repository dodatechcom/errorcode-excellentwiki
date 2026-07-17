---
title: "[Solution] C++ std::bad_typeid - null pointer to typeid"
description: "Fix C++ std::bad_typeid when using typeid on a null pointer dereference."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-typeid", "bad_typeid", "typeid", "type-info", "polymorphism"]
weight: 5
---

# std::bad_typeid - null pointer to typeid

`std::bad_typeid` is thrown when you apply `typeid` to a dereferenced null pointer. This is undefined behavior caught by the runtime.

## Common Causes

```cpp
// Cause 1: typeid on null pointer
Base* ptr = nullptr;
const std::type_info& ti = typeid(*ptr); // throws std::bad_typeid

// Cause 2: Null reference through pointer
Base* p = get_object(); // may return nullptr
typeid(*p); // throws if null
```

## How to Fix

### Fix 1: Check for null before typeid

```cpp
if (ptr != nullptr) {
    const std::type_info& ti = typeid(*ptr);
}
```

### Fix 2: Use pointer cast with typeid

```cpp
if (Derived* d = dynamic_cast<Derived*>(ptr)) {
    std::cout << typeid(*d).name() << std::endl;
}
```

### Fix 3: Use std::type_index for storage

```cpp
#include <typeindex>

std::type_index get_type(Base* ptr) {
    if (!ptr) throw std::invalid_argument("null pointer");
    return std::type_index(typeid(*ptr));
}
```

## Related Errors

- [std::bad_cast]({{< relref "/languages/cpp/bad-cast-dynamic" >}}) — failed dynamic_cast.
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — any_cast failure.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong variant type.
