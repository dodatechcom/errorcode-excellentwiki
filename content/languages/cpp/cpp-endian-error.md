---
title: "[Solution] C++ Endian Error — How to Fix"
description: "Fix C++ endianness errors including byte order mismatches in serialization, network protocol failures, and platform-dependent binary data issues."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Endian Error — How to Fix

Endianness differences between platforms cause binary data serialized on one architecture to be misinterpreted on another, leading to corrupted values in network protocols, file formats, and cross-platform data exchange.

## Why It Happens

Endian errors occur when reading or writing multi-byte values without considering the platform's byte order, when network protocols assume big-endian but the platform is little-endian, when memory-mapped files are read on a different architecture, or when using `memcpy` with incorrect byte ordering.

## Common Error Messages

1. `runtime error: incorrect value after deserialization — byte order mismatch`
2. `error: network byte order conversion missing`
3. `warning: implicit conversion changes endianness`
4. `error: padding bytes included in serialized data`

## How to Fix It

### Fix 1: Use Byte Swap Functions for Cross-Platform Data

```cpp
#include <iostream>
#include <cstdint>
#include <bit>

int main() {
    uint32_t value = 0x12345678;

    // CORRECT — use C++23 std::byteswap
    // uint32_t swapped = std::byteswap(value);

    // Portable byte swap (C++17/20)
    auto byteswap32 = [](uint32_t v) -> uint32_t {
        return ((v & 0xFF000000) >> 24) |
               ((v & 0x00FF0000) >> 8)  |
               ((v & 0x0000FF00) << 8)  |
               ((v & 0x000000FF) << 24);
    };

    uint32_t swapped = byteswap32(value);
    std::cout << std::hex << "Original: 0x" << value << "\n";
    std::cout << "Swapped:  0x" << swapped << "\n";

    return 0;
}
```

### Fix 2: Use htonl/ntohl for Network Programming

```cpp
#include <iostream>
#include <cstdint>
#include <arpa/inet.h>

int main() {
    uint32_t host_value = 12345;

    // CORRECT — convert to network byte order (big-endian)
    uint32_t net_value = htonl(host_value);
    std::cout << "Network: " << std::hex << net_value << "\n";

    // CORRECT — convert back to host byte order
    uint32_t back = ntohl(net_value);
    std::cout << "Host: " << std::dec << back << "\n";

    return 0;
}
```

### Fix 3: Use Portable Serialization

```cpp
#include <iostream>
#include <cstdint>
#include <fstream>
#include <cstring>

struct Record {
    uint32_t id;
    uint16_t type;
    uint32_t value;
};

void serialize(std::ofstream& out, const Record& r) {
    // CORRECT — write in big-endian format
    auto write_be32 = [&](uint32_t v) {
        uint8_t bytes[4] = {
            static_cast<uint8_t>((v >> 24) & 0xFF),
            static_cast<uint8_t>((v >> 16) & 0xFF),
            static_cast<uint8_t>((v >> 8) & 0xFF),
            static_cast<uint8_t>(v & 0xFF)
        };
        out.write(reinterpret_cast<char*>(bytes), 4);
    };

    auto write_be16 = [&](uint16_t v) {
        uint8_t bytes[2] = {
            static_cast<uint8_t>((v >> 8) & 0xFF),
            static_cast<uint8_t>(v & 0xFF)
        };
        out.write(reinterpret_cast<char*>(bytes), 2);
    };

    write_be32(r.id);
    write_be16(r.type);
    write_be32(r.value);
}

int main() {
    std::ofstream out("data.bin", std::ios::binary);
    Record r{42, 1, 100};
    serialize(out, r);
    return 0;
}
```

### Fix 4: Use std::endian from <bit> Header

```cpp
#include <bit>
#include <iostream>

int main() {
    if constexpr (std::endian::native == std::endian::little) {
        std::cout << "Little-endian platform\n";
    } else if constexpr (std::endian::native == std::endian::big) {
        std::cout << "Big-endian platform\n";
    } else {
        std::cout << "Mixed-endian platform\n";
    }

    return 0;
}
```

## Common Scenarios

- **Network protocols**: TCP/IP uses big-endian; most x86 systems are little-endian.
- **File formats**: Binary file formats may specify endianness (e.g., WAV is little-endian).
- **Struct padding**: Different compilers may add padding bytes that break serialization.

## Prevent It

1. Always use `htonl`/`ntohl` for network data and explicit byte swapping for file I/O.
2. Use `std::endian` to detect platform byte order at compile time.
3. Serialize structures field-by-field with explicit byte ordering instead of `memcpy` of the entire struct.

## Related Errors

- [Bit manipulation error]({{< relref "/languages/cpp/cpp-bit-manip-error" >}}) — bitwise operation issues.
- [Filesystem error]({{< relref "/languages/cpp/filesystemerror" >}}) — file operation failures.
- [Sanitizer error]({{< relref "/languages/cpp/cpp-sanitizer-error" >}}) — memory safety issues.
