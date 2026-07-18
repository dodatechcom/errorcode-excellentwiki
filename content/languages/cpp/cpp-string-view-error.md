---
title: "[Solution] C++ String View Error — How to Fix"
description: "Fix C++ std::string_view errors including dangling references, null termination issues, and lifetime management problems with string_view."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ String View Error — How to Fix

`std::string_view` provides a non-owning reference to a string, but dangling views from destroyed temporaries, missing null termination, and incorrect lifetime management cause undefined behavior and crashes.

## Why It Happens

String view errors occur when the view outlives the string it references, when temporary strings are bound to string_view and destroyed at end of expression, when accessing the null terminator position, or when creating views from temporary `std::string` objects.

## Common Error Messages

1. `runtime error: string_view accessing uninitialized memory`
2. `error: dangling reference — string_view outlives source`
3. `error: no matching function for call to 'string_view' from char*`
4. `warning: temporary whose address is used as string_view will dangle`

## How to Fix It

### Fix 1: Don't Store string_view to Temporary Strings

```cpp
#include <string_view>
#include <iostream>
#include <string>

int main() {
    // WRONG — dangling view
    // std::string_view sv = std::string("hello");
    // std::cout << sv << "\n";  // undefined behavior

    // CORRECT — view lives as long as the source string
    std::string str = "hello";
    std::string_view sv = str;
    std::cout << sv << "\n";  // safe

    return 0;
}
```

### Fix 2: Use string_view for Function Parameters

```cpp
#include <string_view>
#include <iostream>
#include <string>

// CORRECT — accepts both std::string and string_view
void print(std::string_view sv) {
    std::cout << sv << "\n";
}

int main() {
    print("hello");            // from const char*
    print(std::string("hi"));  // from std::string
    std::string_view sv = "view";
    print(sv);                 // from string_view

    return 0;
}
```

### Fix 3: Be Careful with substr

```cpp
#include <string_view>
#include <iostream>

int main() {
    std::string_view sv = "Hello, World!";

    // CORRECT — substr creates a new view into the same data
    std::string_view sub = sv.substr(7, 5);
    std::cout << sub << "\n";  // World

    // WRONG — substr beyond bounds is undefined
    // std::string_view bad = sv.substr(0, 100);

    // CORRECT — check bounds
    if (sv.size() >= 12) {
        std::string_view safe = sv.substr(7, 5);
        std::cout << safe << "\n";
    }

    return 0;
}
```

### Fix 4: Don't Use string_view with Null-Terminated APIs

```cpp
#include <string_view>
#include <iostream>
#include <cstring>

int main() {
    std::string_view sv = "hello";

    // WRONG — string_view is not guaranteed null-terminated
    // printf("%s", sv.data());  // may print garbage after "hello"

    // CORRECT — use .data() only if you know it's null-terminated
    // Or construct from a null-terminated source
    std::string str = "hello";
    std::string_view sv2 = str;
    // sv2.data() IS null-terminated because str is

    // CORRECT — use .size() with write operations
    std::cout.write(sv.data(), sv.size());
    std::cout << "\n";

    return 0;
}
```

## Common Scenarios

- **Dangling from temporary**: `string_view sv = get_string();` where `get_string()` returns by value.
- **Missing null terminator**: `string_view` from a substring doesn't preserve the null terminator.
- **STL algorithms**: Using `string_view::data()` with C-string functions that expect null termination.

## Prevent It

1. Never create a `string_view` from a temporary `std::string` that will be destroyed immediately.
2. Use `.data()` only when you're certain the underlying data is null-terminated.
3. Prefer `string_view` for read-only function parameters but return `std::string` from functions.

## Related Errors

- [String view locale]({{< relref "/languages/cpp/cpp-locale-error" >}}) — encoding issues.
- [Out of range]({{< relref "/languages/cpp/out-of-range-string" >}}) — string access violations.
- [Runtime error]({{< relref "/languages/cpp/runtimeerror" >}}) — runtime failures.
