---
title: "[Solution] C fgets Error — How to Fix"
description: "Fix C fgets issues including newline handling, buffer size miscalculation, and EOF detection for safe line reading."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C fgets Error — How to Fix

The `fgets` function reads a line from a stream but includes the newline character in the buffer. Common errors include not stripping the trailing newline, using a buffer size that is one byte too small, and not handling the case where fgets returns NULL due to EOF or error. Mixing fgets with stdin after scanf leaves residual characters.

## Common Error Messages

- `fgets returns NULL on EOF or error`
- `Newline character not removed from fgets buffer`
- `fgets reads incomplete line — buffer too small`
- `Input buffer corruption from mixing fgets and scanf`

## How to Fix It

### Strip the trailing newline

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[128];
    if (fgets(buf, sizeof(buf), stdin)) {
        buf[strcspn(buf, "\n")] = '\0';
        printf("Read: %s\n", buf);
    }
    return 0;
}
```

### Handle NULL return from fgets

```c
#include <stdio.h>

int main(void) {
    char buf[128];
    while (fgets(buf, sizeof(buf), stdin) != NULL) {
        buf[strcspn(buf, "\n")] = '\0';
        printf("Line: %s\n", buf);
    }
    if (ferror(stdin))
        fprintf(stderr, "Error reading input\n");
    return 0;
}
```

### Clear input buffer before switching to fgets

```c
#include <stdio.h>

int clear_stdin_buffer(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
    return c;
}

int main(void) {
    int num;
    scanf("%d", &num);
    clear_stdin_buffer();
    char buf[128];
    fgets(buf, sizeof(buf), stdin);
    buf[strcspn(buf, "\n")] = '\0';
    printf("Number: %d, String: %s\n", num, buf);
    return 0;
}
```

### Use getline for dynamically sized input

```c
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char *line = NULL;
    size_t len = 0;
    ssize_t nread;
    while ((nread = getline(&line, &len, stdin)) != -1)
        printf("Read %zd bytes: %s", nread, line);
    free(line);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Forgetting that fgets includes the newline character in the buffer

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Not checking for NULL return when fgets encounters EOF or error

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using fgets after scanf without clearing the input buffer first

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always strip the newline with buf[strcspn(buf, "\n")] = '\0' after fgets
- **Tip 2:** Check fgets return value for NULL and use ferror to distinguish EOF from error
- **Tip 3:** Use getline instead of fgets when line length is unknown
