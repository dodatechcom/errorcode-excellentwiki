---
title: "[Solution] C rand() Deprecated — Replace with arc4random() or arc4random_buf()"
description: "Replace rand()/srand() with arc4random() in C for better randomness and no seeding required. Migration guide with code examples."
deprecated_function: "rand"
replacement_function: "arc4random"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["rand", "arc4random", "random", "security", "c"]
weight: 5
---

# [Solution] C rand() Deprecated — Replace with arc4random() or arc4random_buf()

The `rand()` and `srand()` functions are deprecated in secure coding guidelines because they produce predictable, low-quality pseudo-random numbers. The linear congruential algorithm used by most implementations has known statistical biases and short periods. For security-sensitive uses, `arc4random()` (available on BSD, macOS, and glibc 2.36+) provides cryptographic-quality randomness without seeding.

## What You'll See

Compiler warnings with certain security flags:

```
warning: 'rand' is deprecated: use arc4random() instead for better randomness
```

## Why Deprecated

`rand()` is deprecated because:

- **Predictable output**: The sequence is deterministic given the seed, making it useless for security.
- **Short period**: Many implementations have periods of only 2^31 or less.
- **Statistical bias**: Low bits often have shorter periods, and the distribution is not uniform.
- **Requires seeding**: `srand(time(NULL))` gives only second-resolution seeds, making the sequence predictable.
- **Not thread-safe**: Shared global state causes data races in multithreaded programs.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand(time(NULL));  // Weak seeding — predictable

    for (int i = 0; i < 5; i++) {
        int r = rand() % 100;  // Biased modulo, weak randomness
        printf("%d ", r);
    }
    printf("\n");
    return 0;
}
```

## New Code — arc4random() Replacement

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // arc4random() requires no seeding — uses kernel entropy
    for (int i = 0; i < 5; i++) {
        uint32_t r = arc4random_uniform(100);  // Uniform [0, 99]
        printf("%u ", r);
    }
    printf("\n");
    return 0;
}
```

## New Code — arc4random_buf() for Arbitrary Random Data

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    // Generate a random 32-byte token
    unsigned char token[32];
    arc4random_buf(token, sizeof(token));

    // Print as hex
    for (size_t i = 0; i < sizeof(token); i++) {
        printf("%02x", token[i]);
    }
    printf("\n");

    // Generate a random password
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    char password[17];
    for (size_t i = 0; i < sizeof(password) - 1; i++) {
        password[i] = charset[arc4random_uniform(sizeof(charset) - 1)];
    }
    password[sizeof(password) - 1] = '\0';
    printf("Password: %s\n", password);

    return 0;
}
```

## Migration Steps

1. **Find all rand() and srand() calls**:

```bash
grep -rn "\brandom\s*\|\bsrand\s*\|\brand\s*(" --include="*.c" /path/to/project/
```

2. **Remove all `srand()` calls** — `arc4random()` does not need seeding.

3. **Replace `rand() % n` with `arc4random_uniform(n)`** — `arc4random_uniform()` eliminates modulo bias.

4. **Replace `rand()` with `arc4random()`** for general-purpose randomness.

5. **Replace buffer-filling loops** with `arc4random_buf(buf, size)`.

6. **Check platform availability** — `arc4random()` is available on BSD, macOS, and glibc 2.36+. For older glibc, use `getrandom()` as an alternative.

## Related Deprecations

- [tmpnam → mkstemp]({{< relref "/deprecated/c/tmpnam" >}}) — predictable temp file names.
- [signal → sigaction]({{< relref "/deprecated/c/signal" >}}) — unreliable signal handling.
- [system → exec family]({{< relref "/deprecated/c/system" >}}) — shell injection risk.
