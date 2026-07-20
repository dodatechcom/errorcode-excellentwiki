---
title: "[Solution] C++ ABI Incompatible — Linker Error Fix"
description: "Fix C++ ABI incompatibility errors by matching compiler versions, using the same C++ stdlib, and managing the GLIBCXX ABI flag."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 905
---

# C++ ABI Incompatible — Linker Error Fix

ABI (Application Binary Interface) incompatibility occurs when object files or libraries compiled with different compilers, compiler versions, or C++ standard library implementations are linked together. The linker cannot resolve symbols because their binary representations differ.

## Common Causes

```cpp
// Cause 1: Mixing GCC and Clang compiled objects
// object1.cpp (compiled with g++ 11)
// object2.cpp (compiled with clang++ 14)
// g++ object1.o object2.o -o main  ← ABI may differ

// Example: std::string has different layouts between some GCC/Clang versions
```

```cpp
// Cause 2: Mixing different GCC major versions
// Library compiled with g++ 7 (C++11 ABI)
// Application compiled with g++ 12 (C++11 ABI default but different internal layout)
// g++-12 main.cpp -L./lib -loldlib  ← linker errors or runtime crashes
```

```cpp
// Cause 3: GLIBCXX ABI flag mismatch
// Library built with: g++ -D_GLIBCXX_USE_CXX11_ABI=1 lib.cpp
// App built with:     g++ -D_GLIBCXX_USE_CXX11_ABI=0 main.cpp
// Mismatched std::string and other types → linker errors
```

```cpp
// Cause 4: Mixing libstdc++ and libc++
// Clang with libc++: clang++ -stdlib=libc++ main.cpp
// GCC library built with libstdc++
// Linking them together → undefined references
```

```cpp
// Cause 5: Different C++ standard levels affecting ABI
// Library: g++ -std=c++17 lib.cpp  (uses std::string_view with new ABI)
// App:     g++ -std=c++14 main.cpp  (different type layout)
```

## How to Fix

### Fix 1: Use the Same Compiler and Version

```bash
# Ensure all translation units use the same compiler
# Check which compiler built an object file:
objdump -t object.o | c++filt | head

# Rebuild everything with the same compiler
g++ --version  # verify single compiler
g++ -std=c++17 main.cpp lib.cpp -o main

# If using third-party libraries, rebuild them with your compiler
```

### Fix 2: Match the C++ Standard Library

```bash
# Check which stdlib an object uses:
readelf -d object.o | grep NEEDED

# Ensure consistent stdlib choice:
# For GCC (default is libstdc++):
g++ main.cpp -o main

# For Clang with libc++:
clang++ -stdlib=libc++ main.cpp -o main

# Never mix -stdlib=libc++ objects with libstdc++ objects
```

### Fix 3: Set the GLIBCXX ABI Flag Consistently

```bash
# Check current ABI setting:
echo '#include <string>' | g++ -x c++ -E -dM - | grep CXX11_ABI

# Build everything with the same ABI flag:
g++ -D_GLIBCXX_USE_CXX11_ABI=1 main.cpp -o main  # new ABI (default since GCC 5)
g++ -D_GLIBCXX_USE_CXX11_ABI=0 main.cpp -o main  # old ABI (for legacy libraries)

# Match whatever the library was built with
```

### Fix 4: Verify ABI Compatibility Before Linking

```cpp
// Check ABI at compile time
#include <string>
#include <iostream>

int main() {
#ifdef _GLIBCXX_USE_CXX11_ABI
    std::cout << "CXX11 ABI: " << _GLIBCXX_USE_CXX11_ABI << std::endl;
#else
    std::cout << "CXX11 ABI: not defined (old ABI)" << std::endl;
#endif

    std::cout << "Compiler: " << __cplusplus << std::endl;
    return 0;
}
```

### Fix 5: Use Symbol Visibility and Versioning

```cpp
// library.h
#pragma once

// Ensure consistent symbol export
#ifdef BUILDING_LIB
    #define LIB_API __attribute__((visibility("default")))
#else
    #define LIB_API
#endif

LIB_API int compute(int x);

// Compile with consistent flags:
// g++ -fvisibility=hidden -fPIC -shared -o lib.so library.cpp
```

## Examples

```cpp
// Real-world: checking ABI compatibility of linked libraries
// check_abi.cpp
#include <string>
#include <vector>
#include <iostream>

struct ABIInfo {
    std::string compiler;
    int cxx_version;
    bool cxx11_abi;
};

int main() {
    ABIInfo info;
    info.compiler = __VERSION__;
    info.cxx_version = __cplusplus;
#ifdef _GLIBCXX_USE_CXX11_ABI
    info.cxx11_abi = _GLIBCXX_USE_CXX11_ABI;
#else
    info.cxx11_abi = false;
#endif

    std::cout << "Compiler: " << info.compiler << std::endl;
    std::cout << "C++ std: " << info.cxx_version << std::endl;
    std::cout << "CXX11 ABI: " << info.cxx11_abi << std::endl;

    // If linking against a pre-built library, compare these values
    // with what the library was compiled with
    return 0;
}
```

## Related Errors

- [Undefined reference]({{< relref "/languages/cpp/linker-undefined-reference-cpp" >}}) — symbol not found at link time.
- [libstdc++ error]({{< relref "/languages/cpp/linker-libstdc-error" >}}) — stdlib linking issues.
- [Compiler version error]({{< relref "/languages/cpp/compiler-version-error" >}}) — C++ standard version mismatch.
