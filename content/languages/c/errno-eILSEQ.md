---
title: "[Solution] C errno EILSEQ — Invalid multibyte sequence Fix"
description: "Fix C EILSEQ (Invalid multibyte sequence) by setting proper locales, validating input, and handling encoding errors."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eilseq", "invalid-multibyte-sequence", "encoding", "locale", "utf8"]
weight: 5
---

# [Solution] C errno EILSEQ — Invalid multibyte sequence Fix

When a multibyte character conversion function encounters a byte sequence that does not form a valid character in the current locale encoding, the function fails and sets `errno` to `EILSEQ`. This error is common when processing UTF-8 text with invalid byte sequences.

## Common Causes

- Input data contains invalid UTF-8 byte sequences (e.g., lone continuation bytes).
- The locale is set to a multibyte encoding but the input is ASCII-only or binary.
- File content was read with the wrong encoding assumption.
- Network data contains truncated or corrupted multibyte characters.

## How to Fix

Set the correct locale and validate input encoding. Use `mbrtowc()` for safe incremental conversion.

```c
#include <locale.h>
#include <wchar.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    setlocale(LC_ALL, "en_US.UTF-8");

    const char *text = "Hello \xff World";
    mbstate_t state = {0};
    size_t len = strlen(text);
    size_t i = 0;

    while (i < len) {
        wchar_t wc;
        size_t ret = mbrtowc(&wc, text + i, len - i, &state);
        if (ret == (size_t)-1) {
            if (errno == EILSEQ) {
                fprintf(stderr, "Invalid multibyte at position %zu\n", i);
            }
            break;
        } else if (ret == (size_t)-2) {
            fprintf(stderr, "Incomplete sequence at position %zu\n", i);
            break;
        }
        i += ret;
    }
    return 0;
}
```

## Examples

Converting invalid UTF-8 with `mbtowc()`:

```c
#include <stdlib.h>
#include <wchar.h>
#include <stdio.h>
#include <errno.h>
#include <locale.h>

int main(void) {
    setlocale(LC_ALL, "en_US.UTF-8");

    // 0xFE is never valid in UTF-8
    char bad[] = {0xFE, 0x00};
    wchar_t wc;

    if (mbtowc(&wc, bad, 1) == -1 && errno == EILSEQ) {
        fprintf(stderr, "Invalid multibyte sequence (errno %d)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-84 EILSEQ]({{< relref "/languages/c/errno-eilseq" >}}) — invalid or incomplete multibyte (primary).
- [errno-22 EINVAL](/languages/c/errno-eILSEQ/) — invalid argument.
- [errno-84 EILSEQ]({{< relref "/languages/c/errno-eilseq" >}}) — invalid multibyte sequence.
