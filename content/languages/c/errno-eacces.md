---
title: "[Solution] C errno EACCES — Permission denied Fix"
description: "Fix C EACCES (Permission denied) by correcting file permissions, checking access rights, and using proper file modes."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EACCES — Permission denied Fix

When a process attempts to access a file, directory, or perform an operation without the required permissions, the system call fails and sets `errno` to `EACCES`. This error occurs when the file's permission bits, ownership, or access control lists (ACLs) prevent the requested operation.

## Common Causes

- The file or directory does not grant the required permission bits (read, write, or execute) to the calling process.
- The process does not have root privileges and attempts to access a restricted resource.
- The file is on a read-only filesystem or mounted with the `nosuid`/`noexec` option.
- Permission is denied by an access control list (ACL) or mandatory access control (SELinux, AppArmor).

## How to Fix

Check the file permissions with `ls -l` and adjust them using `chmod` or change ownership with `chown`. In code, verify access before performing the operation.

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int main(void) {
    if (access("/etc/shadow", R_OK) == -1) {
        fprintf(stderr, "access denied: %s (errno %d)\n", strerror(errno), errno);
        return 1;
    }
    FILE *fp = fopen("/etc/shadow", "r");
    if (fp == NULL) {
        fprintf(stderr, "fopen failed: %s\n", strerror(errno));
        return 1;
    }
    fclose(fp);
    return 0;
}
```

## Examples

Trying to write to a file without write permission:

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/root/secret.txt", O_WRONLY | O_CREAT, 0644);
    if (fd == -1) {
        perror("open");  // "open: Permission denied"
        fprintf(stderr, "errno: %d (EACCES)\n", errno);
    }
    return 0;
}
```

Trying to bind to a privileged port without root:

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    addr.sin_addr.s_addr = INADDR_ANY;
    if (bind(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        perror("bind");  // "bind: Permission denied"
    }
    return 0;
}
```

## Related Errors

- [errno-13 EPERM](/languages/c/errno-eacces/) — operation not permitted.
- [errno-13 EPERM](/languages/c/errno-eacces/) — not owner (different from EACCES).
- [errno-2 ENOENT](/languages/c/errno-eacces/) — no such file or directory.
