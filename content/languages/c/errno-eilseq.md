---
title: "[Solution] C errno EILSEQ — Invalid or incomplete multibyte Fix"
description: "Fix C EILSEQ (Invalid or incomplete multibyte) by handling locale settings, using proper encoding, and validating input."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eilseq", "invalid-multibyte", "encoding", "locale", "wchar"]
weight: 5
---

# [Solution] C errno EILSEQ — Invalid or incomplete multibyte Fix

When a multibyte character encoding function (`mbtowc()`, `wctomb()`, `mbrtowc()`, etc.) encounters an invalid or incomplete multibyte sequence, the function returns an error and sets `errno` to `EILSEQ`. This error occurs when the byte sequence does not form a valid character in the current locale encoding.

## Common Causes

- The input byte sequence is not valid UTF-8 (or the current locale's encoding).
- A multibyte character is truncated — the string ends in the middle of a character.
- The locale is not set to a multibyte-capable encoding (e.g., `"C"` or `"POSIX"`).
- Binary data is passed to string functions that expect text.

## How to Fix

Set a proper locale and validate input encoding. Use `mbrtowc()` for safe incremental conversion.

```c
#include <locale.h>
#include <wchar.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    setlocale(LC_ALL, "en_US.UTF-8");

    const char *invalid = "\xff\xfe";
    mbstate_t state = {0};
    wchar_t wc;
    size_t ret = mbrtowc(&wc, invalid, 2, &state);

    if (ret == (size_t)-1) {
        if (errno == EILSEQ) {
            fprintf(stderr, "Invalid multibyte sequence\n");
        }
    } else if (ret == (size_t)-2) {
        fprintf(stderr, "Incomplete multibyte sequence\n");
    }
    return 0;
}
```

## Examples

Converting invalid UTF-8:

```c
#include <wchar.h>
#include <stdio.h>
#include <errno.h>
#include <locale.h>

int main(void) {
    setlocale(LC_ALL, "en_US.UTF-8");

    // 0x80 is an invalid start byte in UTF-8
    char bad[] = { 0x80, 0x00 };
    mbstate_t st = {0};
    wchar_t wc;

    size_t n = mbrtowc(&wc, bad, 1, &st);
    if (n == (size_t)-1 && errno == EILSEQ) {
        fprintf(stderr, "Invalid UTF-8 byte (errno %d)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-84 EILSEQ]({{< relref "/languages/c/errno-eILSEQ" >}}) — invalid multibyte sequence (numeric).
- [errno-22 EINVAL](/languages/c/errno-eilseq/) — invalid argument.
- [errno-84 EILSEQ]({{< relref "/languages/c/errno-eILSEQ" >}}) — invalid or incomplete multibyte.
