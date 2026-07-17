---
title: "[Solution] C errno 43 EIDRM — Identifier removed"
description: "Fix C errno 43 EIDRM (Identifier removed) by checking if IPC resource exists before use, handling removal signals, and using proper cleanup."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 43 EIDRM — Identifier removed

Identifier removed occurs when a system call fails and sets `errno` to 43. This error indicates that the requested operation cannot be performed due to the specific condition described by EIDRM.

## Common Causes

- Trying to access a System V IPC resource (semaphore, shared memory, message queue) that has been removed.
- Using a semaphore ID after semctl(IPC_RMID) was called.
- Accessing a shared memory segment after shmctl(IPC_RMID).
- Race condition between resource creation and removal.

## How to Fix

```c
#include <sys/sem.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int semid = semget(IPC_PRIVATE, 1, 0600);
    if (semid == -1) {
        perror("semget");
        return 1;
    }
    semctl(semid, 0, IPC_RMID);
    // Now try to use the removed semaphore
    struct sembuf op = {0, 1, 0};
    if (semop(semid, &op, 1) == -1) {
        fprintf(stderr, "semop failed: %s (errno %d)\n", strerror(errno), errno);
    }
    return 0;
}
```

## Examples

```c
#include <sys/shm.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int shmid = shmget(IPC_PRIVATE, 4096, IPC_CREAT | 0600);
    if (shmid == -1) {
        perror("shmget");
        return 1;
    }
    shmctl(shmid, IPC_RMID, NULL);
    char *ptr = shmat(shmid, NULL, 0);
    if (ptr == (void *)-1 && errno == EIDRM) {
        fprintf(stderr, "Shared memory segment removed\n");
    }
    return 0;
}
```

## Related Errors

- [errno-11 EAGAIN]({{< relref "/languages/c/errno-11" >}}) — resource unavailable.
- [errno-43 EIDRM]({{< relref "/languages/c/errno-43" >}}) — identifier removed (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
