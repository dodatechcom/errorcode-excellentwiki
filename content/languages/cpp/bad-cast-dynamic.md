---
title: "[Solution] C++ std::bad_cast - failed dynamic_cast"
description: "Fix C++ std::bad_cast from failed dynamic_cast. Use correct type hierarchy for casting."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-cast", "bad_cast", "dynamic-cast", "polymorphism", "type-cast"]
weight: 5
---

# std::bad_cast - failed dynamic_cast

`std::bad_cast` is thrown when `dynamic_cast` fails for reference types. Unlike pointer casts which return `nullptr`, reference casts throw this exception.

## Common Causes

```cpp
// Cause 1: Wrong type in cast
class Base { virtual void f() {} };
class Derived1 : public Base {};
class Derived2 : public Base {};

Base* b = new Derived1;
Derived2& d = dynamic_cast<Derived2&>(*b); // throws std::bad_cast

// Cause 2: Casting non-polymorphic type
class NotVirtual { int x; };
NotVirtual nv;
Base& b = dynamic_cast<Base&>(nv); // undefined behavior
```

## How to Fix

### Fix 1: Use pointer cast instead

```cpp
Derived2* d = dynamic_cast<Derived2*>(b);
if (d != nullptr) {
    // cast succeeded
} else {
    // cast failed
}
```

### Fix 2: Use try-catch

```cpp
try {
    Derived2& d = dynamic_cast<Derived2&>(*b);
} catch (const std::bad_cast& e) {
    std::cerr << "Bad cast: " << e.what() << std::endl;
}
```

### Fix 3: Use typeid to check

```cpp
if (typeid(*b) == typeid(Derived1)) {
    Derived1& d = static_cast<Derived1&>(*b);
}
```

## Related Errors

- [std::bad_typeid]({{< relref "/languages/cpp/bad-typeid" >}}) — null pointer to typeid.
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — any_cast failure.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong variant type.
