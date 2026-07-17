---
title: "[Solution] C errno EKEYREJECTED — Key was rejected Fix"
description: "Fix C EKEYREJECTED (Key was rejected) by verifying key ownership, permissions, and re-adding keys correctly."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EKEYREJECTED — Key was rejected Fix

When a process attempts to add or use a key that the kernel rejects (due to ownership mismatch, permission violation, or policy denial), the operation fails and sets `errno` to `EKEYREJECTED`. This error indicates the key was explicitly refused by the system.

## Common Causes

- The key ownership or UID does not match the requesting process.
- A keyring permission check failed — the process lacks write permission.
- The key type or description is invalid or conflicts with an existing key.
- A kernel security module (SELinux, AppArmor) denied the key operation.

## How to Fix

Verify key ownership and permissions. Ensure the process has the correct UID and keyring access.

```c
#include <keyutils.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Try adding a key with correct permissions
    key_serial_t key = add_key("user", "my-key", "data", 4, KEY_SPEC_USER_KEYRING);
    if (key == -1) {
        if (errno == EKEYREJECTED) {
            fprintf(stderr, "Key was rejected — check permissions and ownership\n");
        } else {
            perror("add_key");
        }
        return 1;
    }
    printf("Key added: %d\n", key);
    return 0;
}
```

## Examples

Key rejected due to permission issue:

```c
#include <keyutils.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Attempting to add to a keyring we don't own
    key_serial_t key = add_key("user", "other-key", "data", 4, KEY_SPEC_PROCESS_KEYRING);
    if (key == -1) {
        if (errno == EKEYREJECTED) {
            fprintf(stderr, "Key was rejected by kernel (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-129 EKEYREJECTED]({{< relref "/languages/c/errno-eKEYREJECTED" >}}) — key was rejected (numeric).
- [errno-13 EACCES]({{< relref "/languages/c/errno-eacces" >}}) — permission denied.
- [errno-13 EPERM](/languages/c/errno-eKEYREJECTED/) — operation not permitted.
