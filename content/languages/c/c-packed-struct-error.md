---
title: "[Solution] C Packed Struct Error — How to Fix"
description: "Fix C packed struct alignment issues, performance penalties, and undefined behavior from misaligned access."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Packed Struct Error — How to Fix

Packed structs remove padding between members, but this can cause misaligned memory access. On architectures requiring aligned access (ARM, SPARC), reading a multi-byte member from an unaligned address causes a bus error or performance penalty. Common mistakes include using packed structs for memory-mapped I/O without understanding alignment.

## Common Error Messages

- `Bus error (SIGBUS) from misaligned access in packed struct`
- `Segmentation fault on ARM from unaligned struct member read`
- `Performance penalty from packed struct misalignment`
- `Undefined behavior from casting packed struct pointer to int*`

## How to Fix It

### Use packed structs only for serialization

```c
#include <stdio.h>
#include <stdint.h>

#pragma pack(push, 1)
typedef struct {
    uint8_t  type;
    uint16_t value;
    uint32_t id;
} Packet;
#pragma pack(pop)

int main(void) {
    printf("sizeof(Packet): %zu\n", sizeof(Packet));
    uint8_t raw[] = {0x01, 0x00, 0x2A, 0x00, 0x00, 0x00, 0x01};
    Packet p;
    memcpy(&p, raw, sizeof(p));
    printf("type=%d value=%d id=%d\n", p.type, p.value, p.id);
    return 0;
}
```

### Access packed members through memcpy

```c
#include <stdio.h>
#include <string.h>
#include <stdint.h>

#pragma pack(push, 1)
typedef struct { uint8_t type; uint16_t value; uint32_t id; } Packet;
#pragma pack(pop)

int main(void) {
    uint8_t raw[] = {0x01, 0x00, 0x2A, 0x00, 0x00, 0x00, 0x01};
    Packet p;
    memcpy(&p, raw, sizeof(p));
    printf("type=%d value=%d id=%d\n", p.type, p.value, p.id);
    return 0;
}
```

### Use aligned attributes when needed

```c
#include <stdio.h>
#include <stdint.h>

typedef struct __attribute__((aligned(4))) {
    uint8_t  type;
    uint16_t value;
    uint32_t id;
} AlignedPacket;

int main(void) {
    printf("sizeof: %zu alignof: %zu\n",
           sizeof(AlignedPacket), _Alignof(AlignedPacket));
    return 0;
}
```

### Use compiler-specific attributes for safe packed access

```c
#include <stdio.h>
#include <stdint.h>

typedef struct __attribute__((packed)) {
    uint8_t  flags;
    uint32_t data;
} __attribute__((aligned(1))) SafePacked;

int main(void) {
    printf("sizeof: %zu alignof: %zu\n",
           sizeof(SafePacked), _Alignof(SafePacked));
    return 0;
}
```

## Common Scenarios

### Scenario 1: Accessing multi-byte members of packed structs directly causing alignment faults

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using packed structs for memory-mapped hardware registers without alignment

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Casting a pointer to a packed struct member to a larger type

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Only use packed structs for data serialization, not in-memory processing
- **Tip 2:** Use memcpy to access members of packed structs to avoid alignment issues
- **Tip 3:** Test packed struct code on target architecture to catch alignment problems
