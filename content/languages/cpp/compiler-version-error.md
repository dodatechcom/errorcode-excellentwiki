---
title: "C++ Standard Version Mismatch - Fix"
description: "Fix C++ standard version mismatch errors by setting -std=c++XX flags correctly, checking __cplusplus, and using feature test macros."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 962
---

# C++ Standard Version Mismatch - Fix

C++ standard version mismatch occurs when code compiled with one C++ standard uses features or headers compiled with a different standard. This causes compile errors when language features are not available, or linking errors when ABI differs between standards.

## Common Causes

```cpp
// Cause 1: Compiling C++17 code without -std=c++17
int main() {
    std::string_view sv = "hello";  // C++17 feature
    auto v = std::filesystem::path("/tmp");  // C++17 feature
    return 0;
}
// g++ main.cpp  -- error: std::string_view not in C++14 mode
```

```cpp
// Cause 2: Mixing C++17 and C++20 objects
// a.cpp compiled with: g++ -std=c++17 -c a.cpp
// b.cpp compiled with: g++ -std=c++20 -c b.cpp
// g++ a.o b.o -o main  -- ABI mismatch possible
```

```cpp
// Cause 3: Using C++20 features without compiler support
int main() {
    std::span<int> s;       // C++20
    std::format("{}", 42);  // C++20 (not in older compilers)
    return 0;
}
// g++ 9 -std=c++20 main.cpp  -- error: std::format not available
```

```cpp
// Cause 4: Feature test macros in mixed-standard projects
// If a library was compiled with C++14 and your app uses C++17:
// constexpr lambdas are C++17 but library might not support them
```

```cpp
// Cause 5: MSVC and GCC different default standards
// MSVC 2022 defaults to C++14 (or C++17 in newer versions)
// GCC 12 defaults to C++17 (or C++20 in latest versions)
// Clang defaults to C++14 or C++17 depending on version
```

## How to Fix

### Fix 1: Specify the correct standard flag

```bash
# C++11
g++ -std=c++11 main.cpp -o main

# C++14
g++ -std=c++14 main.cpp -o main

# C++17
g++ -std=c++17 main.cpp -o main

# C++20
g++ -std=c++20 main.cpp -o main

# C++23 (supported in newer compilers)
g++ -std=c++23 main.cpp -o main

# GNU extensions with the std version:
g++ -std=gnu++17 main.cpp -o main
```

### Fix 2: Check __cplusplus at compile time

```cpp
#include <iostream>

int main() {
    #if __cplusplus >= 202002L
        std::cout << "C++20 or later" << std::endl;
    #elif __cplusplus >= 201703L
        std::cout << "C++17" << std::endl;
    #elif __cplusplus >= 201402L
        std::cout << "C++14" << std::endl;
    #elif __cplusplus >= 201103L
        std::cout << "C++11" << std::endl;
    #else
        std::cout << "Pre-C++11" << std::endl;
    #endif
    return 0;
}
```

### Fix 3: Use feature test macros

```cpp
#include <iostream>

int main() {
    // Check for specific features, not just standard version
    #ifdef __cpp_lib_filesystem
        std::cout << "filesystem available (v" << __cpp_lib_filesystem << ")" << std::endl;
    #endif

    #ifdef __cpp_lib_format
        std::cout << "std::format available" << std::endl;
    #endif

    #ifdef __cpp_lib_span
        std::cout << "std::span available" << std::endl;
    #endif

    #ifdef __cpp_lib_ranges
        std::cout << "std::ranges available" << std::endl;
    #endif

    return 0;
}
```

### Fix 4: Compile all sources with the same standard

```bash
# Build everything consistently:
g++ -std=c++17 -c a.cpp -o a.o
g++ -std=c++17 -c b.cpp -o b.o
g++ -std=c++17 a.o b.o -o main
```

### Fix 5: Use conditional compilation for compatibility

```cpp
#include <iostream>
#include <string>
#include <vector>

// C++17 check for string_view
#if __cpp_lib_string_view >= 201606L
    #include <string_view>
    using StringView = std::string_view;
#else
    using StringView = const std::string&;
#endif

// C++17 check for optional
#if __cpp_lib_optional >= 201606L
    #include <optional>
    template <typename T>
    using Optional = std::optional<T>;
#else
    // Fallback implementation
    template <typename T>
    struct Optional {
        T value_;
        bool has_value_ = false;
        Optional() = default;
        Optional(T v) : value_(v), has_value_(true) {}
        explicit operator bool() const { return has_value_; }
        T& operator*() { return value_; }
    };
#endif

void process(StringView sv) {
    std::cout << sv << std::endl;
}

int main() {
    process("hello world");
    return 0;
}
```

## Examples

```cpp
// Real-world: cross-standard compatibility
#include <iostream>

// Detect and adapt to available C++ standard
#if __cplusplus >= 201703L
    #include <filesystem>
    namespace fs = std::filesystem;
#else
    #include <experimental/filesystem>
    namespace fs = std::experimental::filesystem;
#endif

// C++14 compatible make_unique
#if __cplusplus < 201402L
    namespace std {
        template <typename T, typename... Args>
        unique_ptr<T> make_unique(Args&&... args) {
            return unique_ptr<T>(new T(std::forward<Args>(args)...));
        }
    }
#endif

int main() {
    auto path = fs::current_path();
    std::cout << path << std::endl;
    return 0;
}
```

## Related Errors

- [ABI incompatible]({{< relref "/languages/cpp/linker-abi-incompatible" >}})
- [libstdc++ error]({{< relref "/languages/cpp/linker-libstdc-error" >}})
- [Macro redefinition]({{< relref "/languages/cpp/macro-redefinition-cpp" >}})
