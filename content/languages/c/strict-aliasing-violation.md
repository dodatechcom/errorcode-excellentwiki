---
title: "[Solution] C STRICT_ALIASING_VIOLATION — Strict aliasing violation"
description: "Fix C strict aliasing violations by using char* for byte access, unions for type punning, or -fno-strict-aliasing. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 816
---

# C STRICT_ALIASING_VIOLATION — Strict aliasing violation

The C standard states that an object can only be accessed through a compatible type, a signed/unsigned variant, or `char*`/`unsigned char*`/`void*`. Accessing an object through an incompatible pointer type is undefined behavior. GCC enables strict aliasing optimizations by default (`-fstrict-aliasing`).

## Common Causes

```c
// Cause 1: Type punning through pointer cast
float f = 3.14f;
int *ip = (int *)&f;  // strict aliasing violation: accessing float through int*
printf("%d\n", *ip);
```

```c
// Cause 2: Accessing struct member through wrong type
struct Point { int x; int y; };
struct Point p = {1, 2};
int *arr = (int *)&p;  // undefined if struct has padding or different layout
```

```c
// Cause 3: Casting between unrelated struct types
struct Animal { int type; char name[32]; };
struct Vehicle { int type; int wheels; };

struct Animal a = {1, "dog"};
struct Vehicle *v = (struct Vehicle *)&a;  // strict aliasing violation
```

```c
// Cause 4: Union type punning (UB in C, defined in C11 with restrictions)
union Converter {
    float f;
    int i;
};
union Converter c;
c.f = 3.14f;
printf("%d\n", c.i);  // implementation-defined in C11, UB in strict reading
```

```c
// Cause 5: Accessing buffer through wrong pointer type
void process(double *data, int n) {
    unsigned char *bytes = (unsigned char *)data;
    for (int i = 0; i < n * sizeof(double); i++) {
        bytes[i] = 0;  // strict aliasing violation if compiler assumes double* and unsigned char* don't alias
    }
}
```

## How to Fix

### Fix 1: Use memcpy for type punning

```c
#include <string.h>

float f = 3.14f;
int i;
memcpy(&i, &f, sizeof(i));  // well-defined: char* (from memcpy) can alias anything
printf("%d\n", i);

// Reverse: int to float
int bits = 0x4048f5c3;
float result;
memcpy(&result, &bits, sizeof(result));
printf("%f\n", result);  // 3.14
```

### Fix 2: Use unions for type punning (C11 Annex J)

```c
#include <stdio.h>

union FloatInt {
    float f;
    int i;
};

int main(void) {
    union FloatInt fi;
    fi.f = 3.14f;
    printf("%f -> %d\n", fi.f, fi.i);  // defined behavior in C11
    return 0;
}
```

### Fix 3: Use char* / unsigned char* for byte-level access

```c
#include <stdio.h>

void print_bytes(const void *ptr, size_t size) {
    const unsigned char *bytes = (const unsigned char *)ptr;
    for (size_t i = 0; i < size; i++) {
        printf("%02x ", bytes[i]);
    }
    printf("\n");
}

int main(void) {
    int x = 0x01020304;
    print_bytes(&x, sizeof(x));  // well-defined
    return 0;
}
```

### Fix 4: Disable strict aliasing optimization when needed

```bash
# Disable strict aliasing for the entire project
gcc -fno-strict-aliasing main.c -o app

# Or per-file
gcc -fno-strict-aliasing legacy_code.c -c
```

### Fix 5: Use accessor functions instead of pointer casts

```c
// WRONG: type punning through cast
float f = 1.0f;
int i = *(int *)&f;

// CORRECT: use a function with memcpy
#include <string.h>
static inline int float_to_bits(float f) {
    int i;
    memcpy(&i, &f, sizeof(i));
    return i;
}

static inline float bits_to_float(int i) {
    float f;
    memcpy(&f, &i, sizeof(f));
    return f;
}
```

## Examples

```c
// Real-world: network protocol parsing
#include <string.h>
#include <stdint.h>
#include <stdio.h>

// WRONG: strict aliasing violation
uint32_t read_uint32(const unsigned char *buf) {
    uint32_t val;
    val = *(uint32_t *)buf;  // aliasing violation: unsigned char* → uint32_t*
    return val;
}

// CORRECT: well-defined
uint32_t read_uint32_safe(const unsigned char *buf) {
    uint32_t val;
    memcpy(&val, buf, sizeof(val));
    return val;
}
```

```c
// Real-world: binary serialization
#include <string.h>
#include <stdio.h>

struct Config {
    int width;
    int height;
    float scale;
};

void serialize(const struct Config *cfg, unsigned char *buf) {
    memcpy(buf, cfg, sizeof(*cfg));  // well-defined: copies bytes
}

void deserialize(struct Config *cfg, const unsigned char *buf) {
    memcpy(cfg, buf, sizeof(*cfg));  // well-defined: copies bytes
}
```

## Related Errors

- [C SEQUENCE_POINT_VIOLATION](/languages/c/sequence-point-violation) — Sequence point violation
- [C SIGNED_INTEGER_OVERFLOW](/languages/c/signed-integer-overflow-ub) — Signed integer overflow UB
- [C USE_AFTER_FREE_C](/languages/c/use-after-free-c) — Use after free UB
