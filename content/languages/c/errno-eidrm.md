---
title: "[Solution] C errno EIDRM — Identifier removed Fix"
description: "Fix C EIDRM (Identifier removed) by checking IPC resource existence before accessing and handling removed resources."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eidrm", "identifier-removed", "ipc", "shared-memory", "semaphore"]
weight: 5
---

# [Solution] C errno EIDRM — Identifier removed Fix

When a process attempts to access an IPC resource (message queue, semaphore set, or shared memory segment) that has been removed by another process, the system call fails and sets `errno` to `EIDRM`. This is a race condition in multi-process applications.

## Common Causes

- Another process called `msgctl(IPC_RMID)`, `semctl(IPC_RMID)`, or `shmctl(IPC_RMID)` to remove the IPC resource.
- A race condition where one process removes the IPC resource while another is still using it.
- The IPC resource was removed during a blocking operation (e.g., `msgrcv()` waiting).
- Process cleanup code removes IPC resources prematurely.

## How to Fix

Check for the existence of IPC resources before accessing them. Use signal handlers or cleanup routines carefully.

```c
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    key_t key = ftok("/tmp", 'S');
    int shmid = shmget(key, 1024, IPC_CREAT | 0644);
    if (shmid == -1) {
        fprintf(stderr, "shmget failed: %s\n", strerror(errno));
        return 1;
    }

    // Another process might remove it before we attach
    void *ptr = shmat(shmid, NULL, 0);
    if (ptr == (void *)-1) {
        if (errno == EIDRM) {
            fprintf(stderr, "Shared memory segment was removed\n");
        } else {
            fprintf(stderr, "shmat failed: %s\n", strerror(errno));
        }
        return 1;
    }

    shmdt(ptr);
    return 0;
}
```

## Examples

Accessing a removed message queue:

```c
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int msqid = msgget(IPC_PRIVATE, IPC_CREAT | 0644);
    msgctl(msqid, IPC_RMID, NULL);  // Remove immediately

    struct { long mtype; char mtext[256]; } msg;
    if (msgrcv(msqid, &msg, sizeof(msg.mtext), 0, 0) == -1) {
        if (errno == EIDRM) {
            fprintf(stderr, "Message queue was removed (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-43 EIDRM](/languages/c/errno-eidrm/) — identifier removed (numeric).
- [errno-22 EINVAL](/languages/c/errno-eidrm/) — invalid argument.
- [errno-11 EAGAIN](/languages/c/errno-eidrm/) — resource unavailable, try again.
