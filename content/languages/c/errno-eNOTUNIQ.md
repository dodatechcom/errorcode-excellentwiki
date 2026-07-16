---
title: "[Solution] C errno ENOTUNIQ — Name not unique on network Fix"
description: "Fix C ENOTUNIQ (Name not unique on network) by using unique identifiers, adjusting name resolution, and handling duplicate names."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enotuniq", "name-not-unique", "network-name", "duplicate-name"]
weight: 5
---

# [Solution] C errno ENOTUNIQ — Name not unique on network Fix

When a network name or address operation encounters a duplicate name on the network, the system call fails and sets `errno` to `ENOTUNIQ`. This error occurs when a hostname or network name is not unique within the network domain.

## Common Causes

- Two hosts on the network share the same hostname.
- DNS or name resolution returns a duplicate entry.
- NetBIOS name conflict on a local network segment.
- The specified name conflicts with an existing network resource.

## How to Fix

Ensure unique naming across the network. Use fully qualified domain names (FQDNs) to avoid ambiguity.

```c
#include <netdb.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct addrinfo hints = {0}, *result;
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;

    int ret = getaddrinfo("myhost", NULL, &hints, &result);
    if (ret != 0) {
        if (errno == ENOTUNIQ) {
            fprintf(stderr, "Hostname is not unique on the network\n");
        } else {
            fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(ret));
        }
        return 1;
    }
    freeaddrinfo(result);
    return 0;
}
```

## Examples

Duplicate hostname on the network:

```c
#include <netdb.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct hostent *he = gethostbyname("duplicate-host");
    if (he == NULL) {
        if (h_errno == ENOTUNIQ) {
            fprintf(stderr, "Name not unique on network\n");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-64 ENOTUNIQ]({{< relref "/languages/c/errno-eNOTUNIQ" >}}) — name not unique on network (numeric).
- [errno-3 ENOENT](/languages/c/errno-eNOTUNIQ/) — no such host.
- [errno-22 EINVAL](/languages/c/errno-eNOTUNIQ/) — invalid argument.
