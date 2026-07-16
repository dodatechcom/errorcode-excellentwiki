---
title: "[Solution] C errno ENOKEY — Required key not available Fix"
description: "Fix C ENOKEY (Required key not available) by managing kernel keyrings, adding required keys, and checking key permissions."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enokey", "required-key-not-available", "keyring", "kernel-keyring", "keyctl"]
weight: 5
---

# [Solution] C errno ENOKEY — Required key not available Fix

When a process attempts to access a required encryption key or authentication key from the kernel keyring that does not exist, the operation fails and sets `errno` to `ENOKEY`. This error is associated with the Linux kernel key management facility.

## Common Causes

- The required key has not been added to the kernel keyring.
- The key was expired or revoked and is no longer available.
- The process does not have permission to access the key in the keyring.
- NFS or Kerberos authentication requires a key that is missing.

## How to Fix

Add the required key to the kernel keyring using `keyctl()` or the `keyctl` command.

```c
#include <keyutils.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Check if a key exists
    key_serial_t key = request_key("user", "my-key", NULL, KEY_SPEC_USER_KEYRING);
    if (key == -1) {
        if (errno == ENOKEY) {
            fprintf(stderr, "Required key not available — adding key\n");
            // Add the key
            key = add_key("user", "my-key", "secret-data", 11, KEY_SPEC_USER_KEYRING);
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

Requesting a missing key:

```c
#include <keyutils.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    key_serial_t key = request_key("user", "nfs-key", NULL, KEY_SPEC_SESSION_KEYRING);
    if (key == -1) {
        if (errno == ENOKEY) {
            fprintf(stderr, "NFS key not found in keyring (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-126 ENOKEY]({{< relref "/languages/c/errno-eNOKEY" >}}) — required key not available (numeric).
- [errno-127 EKEYEXPIRED]({{< relref "/languages/c/errno-eKEYEXPIRED" >}}) — key has expired.
- [errno-128 EKEYREVOKED]({{< relref "/languages/c/errno-eKEYREVOKED" >}}) — key has been revoked.
