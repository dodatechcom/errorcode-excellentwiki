---
title: "[Solution] C PCRE/PCRE2 Regex Error — How to Fix"
description: "Fix C PCRE/PCRE2 regex compilation and matching errors."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C PCRE/PCRE2 Regex Error — How to Fix

PCRE errors occur during pattern compilation or matching. Common issues include invalid regex syntax, insufficient match data, and not freeing compiled patterns.

## Common Error Messages

- `PCRE: ERRNNN at offset N: description`
- `pcre_exec: no match`
- `pcre_compile failed: unmatched parentheses`
- `pcre: buffer too small for substring`

## How to Fix It

### Check pcre_compile return

```c
#include <pcre.h>
#include <stdio.h>

int main(void) {
    const char *pattern = "^[a-z]+@[a-z]+\\.[a-z]+$";
    const char *error;
    int erroffset;
    pcre *re = pcre_compile(pattern, 0, &error, &erroffset, NULL);
    if (!re) {
        fprintf(stderr, "PCRE error: %s at %d\n", error, erroffset);
        return 1;
    }
    pcre_free(re);
    return 0;
}
```

### Check match with pcre_exec

```c
#include <pcre.h>
#include <stdio.h>

int main(void) {
    pcre *re = pcre_compile("[0-9]+", 0, NULL, 0, NULL);
    if (!re) return 1;
    int ovector[30];
    int rc = pcre_exec(re, NULL, "hello 42 world", 14, 0, 0, ovector, 30);
    if (rc > 0) {
        printf("Match at %d-%d\n", ovector[0], ovector[1]);
    }
    pcre_free(re);
    return 0;
}
```

### Use pcre2 for modern regex

```c
#define PCRE2_CODE_UNIT_WIDTH 0
#include <pcre2.h>
#include <stdio.h>

int main(void) {
    int errnum;
    PCRE2_SIZE erroff;
    pcre2_code *re = pcre2_compile("^[a-z]+", PCRE2_CASELESS, &errnum, &erroff, NULL);
    if (!re) {
        fprintf(stderr, "Error at %zu\n", erroff);
        return 1;
    }
    pcre2_code_free(re);
    return 0;
}
```

### Extract captured groups

```c
#include <pcre.h>
#include <stdio.h>

void extract_email(const char *input) {
    pcre *re = pcre_compile("([a-z]+)@([a-z]+\\.[a-z]+)", 0, NULL, 0, NULL);
    if (!re) return;
    int ovector[30];
    if (pcre_exec(re, NULL, input, strlen(input), 0, 0, ovector, 30) >= 3) {
        char user[64], domain[128];
        pcre_copy_substring(input, ovector, 30, 1, user, sizeof(user));
        pcre_copy_substring(input, ovector, 30, 2, domain, sizeof(domain));
        printf("User: %s, Domain: %s\n", user, domain);
    }
    pcre_free(re);
}
```

## Common Scenarios

### Scenario 1: Invalid regex pattern causing compile failure

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Match data buffer too small for captures

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Memory leak from not freeing compiled pattern

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check pcre_compile return and error offset
- **Tip 2:** Free pcre objects with pcre_free when done
- **Tip 3:** Use pcre2 for new code as PCRE1 is in maintenance mode
