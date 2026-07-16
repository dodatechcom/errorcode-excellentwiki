---
title: "[Solution] C++ std::codecvt — Character Conversion Error Fix"
description: "Fix C++ std::codecvt errors during character encoding conversion. Handle UTF-8, UTF-16, and locale conversion failures."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["codecvt", "encoding", "utf8", "conversion"]
weight: 5
---

# [Solution] C++ std::codecvt — Character Conversion Error Fix

A `std::codecvt` error occurs when character encoding conversion fails — such as converting between UTF-8 and UTF-16 with invalid byte sequences, or when using deprecated `std::codecvt` facets with incompatible encodings. Errors manifest as `std::runtime_error` or `std::range_error`.

## Why codecvt Errors Occur

Common causes include invalid UTF-8 byte sequences (truncated or malformed multibyte characters), encoding mismatches between source and target, buffer sizes too small for the conversion, and deprecated C++17 codecvt facets producing errors.

## Wrong: Converting Invalid UTF-8 Sequence

```cpp
// WRONG — invalid UTF-8 produces error
#include <codecvt>
#include <locale>
#include <string>
#include <iostream>

int main() {
    std::string invalid_utf8 = "\x80\x81";  // invalid leading bytes

    try {
        std::wstring_convert<std::codecvt_utf8<wchar_t>> converter;
        std::wstring ws = converter.from_bytes(invalid_utf8);  // may throw
    } catch (const std::range_error& e) {
        std::cerr << "Conversion error: " << e.what() << std::endl;
    }
    return 0;
}
```

## Correct: Validate UTF-8 Before Conversion

```cpp
// CORRECT — validate before converting
#include <string>
#include <iostream>
#include <stdexcept>

bool is_valid_utf8(const std::string& s) {
    size_t i = 0;
    while (i < s.size()) {
        unsigned char c = s[i];
        int bytes = 0;

        if (c <= 0x7F) bytes = 1;
        else if ((c & 0xE0) == 0xC0) bytes = 2;
        else if ((c & 0xF0) == 0xE0) bytes = 3;
        else if ((c & 0xF8) == 0xF0) bytes = 4;
        else return false;

        if (i + bytes > s.size()) return false;

        for (int j = 1; j < bytes; j++) {
            if ((s[i + j] & 0xC0) != 0x80) return false;
        }
        i += bytes;
    }
    return true;
}

int main() {
    std::string text = "hello world";

    if (is_valid_utf8(text)) {
        std::cout << "Valid UTF-8: " << text << std::endl;
    } else {
        std::cerr << "Invalid UTF-8 detected" << std::endl;
    }
    return 0;
}
```

## Safe Wide String Conversion

```cpp
// CORRECT — handle conversion errors gracefully
#include <string>
#include <iostream>
#include <locale>
#include <codecvt>

std::wstring safe_to_wstring(const std::string& utf8) {
    try {
        std::wstring_convert<std::codecvt_utf8<wchar_t>> conv;
        return conv.from_bytes(utf8);
    } catch (const std::range_error&) {
        return L"[invalid encoding]";
    }
}

int main() {
    std::string valid = "Hello, World!";
    std::string invalid = "\xFF\xFE";

    std::cout << "Valid: " << std::wstring(safe_to_wstring(valid).begin(),
                                              safe_to_wstring(valid).end()) << std::endl;
    std::wstring result = safe_to_wstring(invalid);
    std::wcout << L"Invalid: " << result << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Validate encoding before conversion | When input may contain invalid bytes |
| Catch `range_error`/`runtime_error` | When converting between encodings |
| Use third-party libraries (ICU) | For production-grade encoding support |
| Check buffer sizes | When converting to fixed-size buffers |

## Related Errors

- [std::locale error]({{< relref "/languages/cpp/locale-error" >}}) — locale construction failures.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-failure" >}}) — stream I/O errors.
