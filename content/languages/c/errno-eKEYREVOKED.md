---
title: "[Solution] C errno EKEYREVOKED — Key has been revoked Fix"
description: "Fix C EKEYREVOKED (Key has been revoked) by obtaining new keys and checking revocation status."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EKEYREVOKED — Key has been revoked Fix

When a process attempts to use a key from the kernel keyring that has been explicitly revoked, the operation fails and sets `errno` to `EKEYREVOKED`. A revoked key cannot be used and must be replaced.

## Common Causes

- An administrator revoked the key via `keyctl revoke()`.
- The key was automatically revoked due to a security policy.
- A parent keyring was revoked, cascading revocation to child keys.
- Kerberos ticket was revoked by the KDC.

## How to Fix

Obtain a new key to replace the revoked one. Do not attempt to use revoked keys.

```c
#include <keyutils.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    key_serial_t key = request_key("user", "auth-key", NULL, KEY_SPEC_USER_KEYRING);
    if (key == -1) {
        if (errno == EKEYREVOKED) {
            fprintf(stderr, "Key has been revoked — obtaining new key\n");
            key = add_key("user", "auth-key", "new-credentials", 14, KEY_SPEC_USER_KEYRING);
            if (key == -1) {
                perror("add_key");
                return 1;
            }
        } else {
            perror("request_key");
            return 1;
        }
    }
    return 0;
}
```

## Examples

Detecting a revoked key:

```c
#include <keyutils.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    key_serial_t key = request_key("user", "old-key", NULL, KEY_SPEC_SESSION_KEYRING);
    if (key == -1) {
        if (errno == EKEYREVOKED) {
            fprintf(stderr, "Key was revoked (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-128 EKEYREVOKED]({{< relref "/languages/c/errno-eKEYREVOKED" >}}) — key has been revoked (numeric).
- [errno-126 ENOKEY]({{< relref "/languages/c/errno-eNOKEY" >}}) — required key not available.
- [errno-127 EKEYEXPIRED]({{< relref "/languages/c/errno-eKEYEXPIRED" >}}) — key has expired.
